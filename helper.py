import json
import os

class Helper:
    def __init__(self):
        self.database = None
    
    def load_data(self):
        with open(os.path.join(os.getcwd(), "data.json"), "r") as f:
            self.database = json.load(f)
        return self.database