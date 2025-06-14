"""Test suite for the pharmatech package medicine database."""
import pytest
from pharmatech.medicine_db import MedicineDatabase

def test_search_by_condition():
    db = MedicineDatabase()
    results = db.search_by_condition("fever")
    assert len(results) > 0
    assert "paracetamol" in [med["generic_name"] for med in results]

def test_get_medicine_info():
    db = MedicineDatabase()
    info = db.get_medicine_info("paracetamol")
    assert info is not None
    assert info["generic_name"] == "paracetamol"
    assert "fever" in info["conditions"]

def test_add_medicine():
    db = MedicineDatabase()
    db.add_medicine(
        "ibuprofen",
        uses=["pain relief", "inflammation"],
        conditions=["arthritis", "headache", "fever"],
        description="Non-steroidal anti-inflammatory drug (NSAID)"
    )
    info = db.get_medicine_info("ibuprofen")
    assert info is not None
    assert "arthritis" in info["conditions"]

def test_medicine_not_found():
    db = MedicineDatabase()
    info = db.get_medicine_info("nonexistentmedicine")
    assert info is None
