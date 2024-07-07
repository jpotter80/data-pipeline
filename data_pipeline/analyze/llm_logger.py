import json
import os
from datetime import datetime

class LLMLogger:
    def __init__(self, log_dir='llm_logs'):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    def log_interaction(self, prompt, response, analysis_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{analysis_type}_{timestamp}.json"
        log_entry = {
            "timestamp": timestamp,
            "analysis_type": analysis_type,
            "prompt": prompt,
            "response": response
        }
        with open(os.path.join(self.log_dir, filename), 'w') as f:
            json.dump(log_entry, f, indent=2)
        return filename

    def read_log(self, filename):
        with open(os.path.join(self.log_dir, filename), 'r') as f:
            return json.load(f)