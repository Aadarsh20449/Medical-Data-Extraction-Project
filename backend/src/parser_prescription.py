from backend.src.parser_generic import MedicalDocParser
import re
import sys
import os

# (Optional) Add project root to sys.path for testing convenience
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        self.text = text  # Fix: use instance variable

    def parse(self):
        return {
            'patient_name' : self.get_name(),
            'patient_address' : self.get_address(),
            'medicines' : self.get_medicine(),
            'Directions' : self.get_directions(),
            'Refill' : self.get_refill()
        }

    def get_name(self):
        pattern = r'Name:(.*)Date'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()

    def get_address(self):
        pattern = r'Address:(.*)\n'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()
        
    def get_medicine(self):
        pattern = r'\|\s*(.+?mg|ml|units)\b'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()
        return None
    def get_directions(self):
        pattern = r'Directions:(.*)\n'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()
    
    def get_refill(self):
        pattern = r'Refill:\s*(.*)'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()
