from backend.src.parser_generic import MedicalDocParser
import re

class PatientDetailsParser(MedicalDocParser):
    def __init__(self,text):
        self.text=text

    

    def parse(self):
        return {
            'patient_name' : self.get_name(),
            'phone_number' : self.get_phone(),
            'medical_problems' : self.get_medical_problems(),
            'hepatitis_b_vaccination' : self.get_hepatitis_b_vaccination()
        }

    def get_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        match = matches[0].strip().replace('Birth Date','')
        date_pattern = '((Jan|feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern,match)
        date = date_matches[0][0]
        match = match.replace(date,'').strip()
        return match 
    
    def get_phone(self):
        pattern = '\(\d{3}\) \d{3}-\d{4}'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        number = matches[0].strip()
        return number
    
    def get_medical_problems(self):
        pattern = r'List any Medical Problems.*?:\s*\n*(.*)'
        matches = re.findall(pattern,self.text)
        return matches[0].strip()
    
    def get_hepatitis_b_vaccination(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern,self.text,flags=re.DOTALL)
        return matches[0].strip()
