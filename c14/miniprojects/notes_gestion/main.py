import os
import json

class App:
    def __init__(self):
        self.etudiants = []
        self.file = 'students.json'

        self.load()
    
    def load(self):
        if os.path.isfile(self.file):
            with open(self.file, 'w+') as f:
                self.etudiants = json.load(f)
        return

    def add_student(self):
        :
            
