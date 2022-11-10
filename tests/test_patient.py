"""Tests for the Patient model."""


def test_create_patient():
    """Test to check a patient is correctly given a name."""
    from inflammation.models import Patient
    name = 'Alice'
    pat = Patient(name=name)
    assert pat.name == name

def test_patient_is_person():
    """Test to check patient is a person."""
    from inflammation.models import Patient, Person
    pat = Patient("Alice")
    assert isinstance(pat, Person)

def test_create_doctor():
    """Test to check doctor is correctly given a name."""
    from inflammation.models import Doctor
    name = 'Jeff'
    doc = Doctor(name=name)
    assert doc.name == name

def test_doctor_is_person():
    """Test to check doctor is a person."""
    from inflammation.models import Doctor, Person
    doc = Doctor("Jeff")
    assert isinstance(doc, Person)

def test_patients_added_correctly():
    """Check patients are being added correctly by a doctor. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    assert doc.patients is not None
    assert len(doc.patients) == 1

def test_no_duplicate_patients():
    """Check adding the same patient to the same doctor twice does not result in duplicates. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    doc.add_patient(alice)
    assert len(doc.patients) == 1 
