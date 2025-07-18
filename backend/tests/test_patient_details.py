import pytest 
from backend.src.parser_patient_details import PatientDetailsParser

@pytest.fixture()
def pd_1():
    text = '''
    17/12/2020

    Patient Medical Record

    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 .
    United States Height:
    190
    In Casc of Emergency
    7 ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone

    Genera! Medical History

    a

    a

    a ea A CE i a

    Chicken Pox (Varicella): Measies:

    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?
    No

    List any Medical Problems (asthma, seizures, headaches}:

    Migraine

    CO
    aa

    .

    ‘Name of Insurance Company:

    Random Insuarance Company - 4789 Bollinger Rd
    Jersey City, New Jersey, 07030

    a Policy Number:
    ra 1520731 3 Expiry Date:

    . 30 December 2020
    Do you have medical insurance?

    Yes:

    Medical Insurance Details

    List any allergies:

    Peanuts

    List any medication taken regularly:
    Triptans'''
    return PatientDetailsParser(text)

def test_get_name(doc_2_maria):
    assert doc_2_maria.get_name() == 'Kathy Crawford'

def test_get_phone(doc_2_maria):
    assert doc_2_maria.get_address() == '(737) 988-0851'

def get_medical_problems(doc_2_maria):
    assert doc_2_maria.get_medicine() == 'Migraine'

def test_hepatitis_b_vaccination(doc_2_maria):
    assert doc_2_maria.get_directions() == 'Yes'