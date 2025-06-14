"""
Pharmatech - A Python Library for Medicine Information

This module provides functionality to search and retrieve information about medicines,
their uses, and safety information including pregnancy and breastfeeding considerations.
"""

__version__ = "0.1.0"

from .medicine_db import MedicineDatabase

class PharmaTech:
    def __init__(self):
        self._db = MedicineDatabase()

    def find_medicines_for_condition(self, condition: str):
        """Find medicines that can treat a specific condition."""
        return self._db.search_by_condition(condition)

    def find_medicines_by_category(self, category: str):
        """Find medicines in a specific category."""
        return self._db.search_by_category(category)

    def find_medicines_by_side_effect(self, side_effect: str):
        """Find medicines that may cause a specific side effect."""
        return self._db.search_by_side_effect(side_effect)

    def find_medicines_by_form(self, form: str):
        """Find medicines available in a specific form (tablet, syrup, etc.)."""
        return self._db.search_by_form(form)

    def get_medicine_details(self, generic_name: str):
        """Get detailed information about a medicine."""
        return self._db.get_medicine_info(generic_name)

    def get_medicine_contraindications(self, generic_name: str):
        """Get contraindications for a specific medicine."""
        return self._db.get_contraindications(generic_name)

    def get_medicine_dosage(self, generic_name: str):
        """Get dosage information for a specific medicine."""
        return self._db.get_dosage_info(generic_name)

    def get_pregnancy_safety(self, generic_name: str):
        """Get pregnancy safety information for a specific medicine."""
        return self._db.get_pregnancy_safety(generic_name)

    def get_lactation_safety(self, generic_name: str):
        """Get breastfeeding safety information for a specific medicine."""
        return self._db.get_lactation_safety(generic_name)

    def find_pregnancy_safe_medicines(self, category: str = "A"):
        """Find medicines that are safe during pregnancy by category."""
        return self._db.search_safe_in_pregnancy(category)

    def find_breastfeeding_safe_medicines(self, category: str = "safe"):
        """Find medicines that are safe during breastfeeding by category."""
        return self._db.search_safe_in_lactation(category)

    def get_available_categories(self):
        """Get a list of all available medicine categories."""
        return self._db.get_all_categories()

# Create a default instance for easier usage
pharma = PharmaTech()
