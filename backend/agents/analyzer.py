import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from agents.prompts import SYSTEM_PROMPT


load_dotenv()

class LogAnalyzer:
    def __init__(self):
        
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4-1106-preview" 

    def analyze(self, raw_logs: str):
        """
        Processes Jenkins logs and returns a structured diagnostic.
        """
  
        refined_logs = raw_logs[-3000:] if len(raw_logs) > 3000 else raw_logs

        try:
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Analyze these logs and provide the fix:\n\n{refined_logs}"}
                ],
                response_format={"type": "json_object"}
            )

            
            analysis_content = response.choices[0].message.content
            return json.loads(analysis_content)

        except Exception as e:
        
            return {
                "error_type": "Analysis_Failure",
                "root_cause": f"The AI agent encountered an error: {str(e)}",
                "suggested_fix": "Check your OpenAI API quota and logs manually.",
                "confidence_score": 0.0
            }

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    test_logs = "npm ERR! missing script: build-missing-script"
    print(analyzer.analyze(test_logs))