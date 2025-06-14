"""
Comprehensive example of the Pharmatech library functionality.
This example demonstrates all major features of the library.
"""
from pharmatech import pharma

def print_divider(text=""):
    print(f"\n{text}")
    print("=" * 50)

def print_medicine_info(generic_name: str):
    """Print comprehensive information about a medicine."""
    print(f"\nDetailed information for: {generic_name.upper()}")
    print("-" * 50)
    
    # Basic information
    info = pharma.get_medicine_details(generic_name)
    if not info:
        print(f"No information found for {generic_name}")
        return
    
    print("BASIC INFORMATION:")
    print(f"Description: {info['description']}")
    print(f"Uses: {', '.join(info['uses'])}")
    print(f"Conditions: {', '.join(info['conditions'])}")
    
    # Dosage information
    dosage = pharma.get_medicine_dosage(generic_name)
    if dosage:
        print("\nDOSAGE INFORMATION:")
        print(f"Adult dosing: {dosage['adult']}")
        print(f"Child dosing: {dosage['child']}")
        print(f"Available forms: {', '.join(dosage['form'])}")
    
    # Safety information
    print("\nSAFETY INFORMATION:")
    contraindications = pharma.get_medicine_contraindications(generic_name)
    if contraindications:
        print("Contraindications:")
        for item in contraindications:
            print(f"- {item}")
    
    if 'side_effects' in info:
        print("\nPossible side effects:")
        for effect in info['side_effects']:
            print(f"- {effect}")
    
    # Pregnancy and breastfeeding information
    preg_safety = pharma.get_pregnancy_safety(generic_name)
    if preg_safety:
        print("\nPREGNANCY SAFETY:")
        print(f"Category: {preg_safety['category']}")
        print(f"Safety Information: {preg_safety['safety_info']}")
    
    lact_safety = pharma.get_lactation_safety(generic_name)
    if lact_safety:
        print("\nBREASTFEEDING SAFETY:")
        print(f"Category: {lact_safety['category']}")
        print(f"Safety Information: {lact_safety['safety_info']}")
    print("-" * 50)

def main():
    # 1. Show available medicine categories
    print_divider("AVAILABLE MEDICINE CATEGORIES")
    categories = pharma.get_available_categories()
    for category in categories:
        print(f"- {category}")

    # 2. Search by condition example
    print_divider("SEARCH BY CONDITION: 'headache'")
    headache_meds = pharma.find_medicines_for_condition("headache")
    for med in headache_meds:
        print(f"- {med['generic_name']}: {med['description']}")

    # 3. Search by category example
    print_divider("SEARCH BY CATEGORY: 'antibiotics'")
    antibiotics = pharma.find_medicines_by_category("antibiotics")
    for med in antibiotics:
        print(f"- {med['generic_name']}: {med['description']}")

    # 4. Search medicines by form
    print_divider("SEARCH BY FORM: 'syrup'")
    syrup_meds = pharma.find_medicines_by_form("syrup")
    for med in syrup_meds:
        print(f"- {med['generic_name']}")

    # 5. Search pregnancy-safe medicines
    print_divider("PREGNANCY-SAFE MEDICINES (Category B)")
    safe_in_pregnancy = pharma.find_pregnancy_safe_medicines("B")
    for med in safe_in_pregnancy:
        print(f"- {med['generic_name']}: {med['pregnancy_safety']}")

    # 6. Search breastfeeding-safe medicines
    print_divider("BREASTFEEDING-SAFE MEDICINES")
    safe_in_lactation = pharma.find_breastfeeding_safe_medicines("safe")
    for med in safe_in_lactation:
        print(f"- {med['generic_name']}: {med['lactation_safety']}")

    # 7. Detailed information for specific medicines
    print_divider("DETAILED MEDICINE INFORMATION")
    medicines_to_detail = ["paracetamol", "ibuprofen", "amoxicillin"]
    for medicine in medicines_to_detail:
        print_medicine_info(medicine)

if __name__ == "__main__":
    main()
