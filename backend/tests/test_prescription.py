from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_2_maria():
    text = '''
        Dr John >mith, M.D

        2 Non-Important street,
        New York, Phone (900)-323- ~2222

        Name:  Virat Kohli Date: 2/05/2022

        Address: 2 cricket blvd, New Delhi

        | Omeprazole 40 mg

        Directions: Use two tablets daily for three months

        Refill: 3 times'''
    return PrescriptionParser(text)

def test_get_name(doc_2_maria):
    assert doc_2_maria.get_name() == 'Virat Kohli'

def test_get_address(doc_2_maria):
    assert doc_2_maria.get_address() == '2 cricket blvd, New Delhi'

def get_get_medicine(doc_2_maria):
    assert doc_2_maria.get_medicine() == 'Omeprazole 40 mg'

def test_get_directions(doc_2_maria):
    assert doc_2_maria.get_directions() == 'Use two tablets daily for three months'

def get_get_refill(doc_2_maria):
    assert doc_2_maria.get_refill() == '3 times'



