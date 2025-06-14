"""
Database module for medicine information storage and retrieval.
"""
from typing import Dict, List, Optional

class MedicineDatabase:
    def __init__(self):
        # Initialize pregnancy categories with descriptions
        self._pregnancy_categories = {
            "A": "Adequate studies show no risk",
            "B": "Animal studies show no risk but human studies inadequate, or animal studies show risk but human studies show no risk",
            "C": "Animal studies show adverse effects but human studies inadequate, or no studies available",
            "D": "Evidence of human fetal risk exists, but benefits may outweigh risks in serious situations",
            "X": "Contraindicated in pregnancy due to evidence of fetal risk that outweighs any benefit"
        }
        
        # Initialize lactation safety categories
        self._lactation_categories = {
            "safe": "Compatible with breastfeeding",
            "moderate_safe": "Usually compatible, monitor infant",
            "caution": "Limited data available, use with caution",
            "unsafe": "Not recommended during breastfeeding"
        }

        # Common condition aliases for better search results
        self._condition_aliases = {
            "high blood pressure": ["hypertension"],
            "diabetes": ["type 1 diabetes", "type 2 diabetes", "diabetes mellitus"],
            "high cholesterol": ["hypercholesterolemia"],
            "stomach ulcer": ["gastric ulcers", "duodenal ulcers"],
            "chest pain": ["angina"],
            "blood sugar": ["glucose"],
            "heart problems": ["cardiovascular disease", "heart disease"],
            "stomach acid": ["acid reflux", "GERD"],
            "bipolar": ["bipolar disorder"],
            "pain": ["chronic pain", "acute pain"],
            "infections": ["bacterial infections", "viral infections"],
            "liver problems": ["hepatitis", "cirrhosis", "fatty liver"],
            "eye problems": ["glaucoma", "eye infection", "conjunctivitis"],
            "skin problems": ["eczema", "psoriasis", "dermatitis", "acne"],
            "bone problems": ["osteoporosis", "arthritis", "joint pain"],
            "sleep problems": ["insomnia", "sleep apnea", "narcolepsy"],
            "allergies": ["hay fever", "seasonal allergies", "allergic rhinitis"]
        }
        
        # Medicine categories for better organization
        self._categories = {
            "antibiotics": ["amoxicillin", "azithromycin", "ciprofloxacin", "doxycycline", "metronidazole"],
            "painkillers": ["paracetamol", "ibuprofen", "tramadol"],
            "antidepressants": ["fluoxetine", "sertraline", "venlafaxine", "escitalopram"],
            "blood_pressure": ["amlodipine", "losartan", "hydrochlorothiazide"],
            "diabetes": ["metformin", "insulin"],
            "stomach": ["omeprazole", "pantoprazole", "metoclopramide"],
            "anti_inflammatory": ["ibuprofen", "prednisone"],
            "heart": ["clopidogrel", "warfarin", "atorvastatin", "simvastatin"],
            "respiratory": ["salbutamol", "montelukast"],
            "anticonvulsants": ["gabapentin", "carbamazepine"],
            "hormones": ["levothyroxine", "insulin", "prednisone"],
            "vitamins_supplements": ["folic_acid"],
            "antihistamines": ["cetirizine", "loratadine"],
            "antifungals": ["fluconazole", "terbinafine"],
            "antivirals": ["acyclovir", "oseltamivir"],
            "muscle_relaxants": ["cyclobenzaprine", "baclofen"],
            "eye_medications": ["timolol", "latanoprost"],
            "dermatologicals": ["hydrocortisone", "betamethasone"],
            "sleep_aids": ["zolpidem", "melatonin"],
            "antacids": ["omeprazole", "pantoprazole", "ranitidine"]
        }
        
        # Initialize medicine database with enhanced information
        self._medicines: Dict[str, Dict] = {
            "paracetamol": {
                "uses": ["fever reduction", "pain relief", "headache treatment"],
                "conditions": ["fever", "common cold", "headache", "muscle pain", "arthritis"],
                "description": "Common pain reliever and fever reducer. Also known as acetaminophen.",
                "dosage": {
                    "adult": "500-1000 mg every 4-6 hours as needed (max 4000 mg/day)",
                    "child": "Based on weight and age, consult physician",
                    "form": ["tablet", "syrup", "suppository"]
                },
                "contraindications": [
                    "Severe liver disease",
                    "Alcohol dependence",
                    "Known hypersensitivity"
                ],
                "side_effects": [
                    "Rare liver problems with high doses",
                    "Nausea",
                    "Rash (rare)"
                ],
                "precautions": [
                    "Avoid alcohol while taking this medication",
                    "Do not exceed recommended dose",
                    "Consult doctor if pregnant or breastfeeding"
                ],
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy when used as directed",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding, minimal amount in breast milk"
            },
            "amoxicillin": {
                "uses": ["bacterial infection treatment"],
                "conditions": ["respiratory tract infections", "ear infections", "sinusitis", "pneumonia", "bronchitis"],
                "description": "Broad-spectrum antibiotic for treating various bacterial infections.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Safe during breastfeeding, monitor infant for diarrhea"
            },
            "ibuprofen": {
                "uses": ["pain relief", "inflammation reduction", "fever reduction"],
                "conditions": ["arthritis", "headache", "fever", "menstrual pain", "back pain", "dental pain"],
                "description": "Non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Avoid in third trimester, use with caution in first and second trimesters",
                "lactation_category": "moderate_safe",
                "lactation_safety": "Compatible with breastfeeding, monitor infant for GI effects"
            },
            "metformin": {
                "uses": ["blood sugar control", "diabetes management"],
                "conditions": ["type 2 diabetes", "insulin resistance", "prediabetes"],
                "description": "First-line medication for treating type 2 diabetes.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding"
            },
            "omeprazole": {
                "uses": ["acid reduction", "stomach protection"],
                "conditions": ["gastric ulcers", "acid reflux", "GERD", "heartburn", "stomach ulcers"],
                "description": "Proton pump inhibitor that reduces stomach acid production.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "amlodipine": {
                "uses": ["blood pressure reduction", "angina treatment"],
                "conditions": ["hypertension", "angina", "coronary artery disease"],
                "description": "Calcium channel blocker used to treat high blood pressure and chest pain.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "salbutamol": {
                "uses": ["bronchodilation", "asthma relief"],
                "conditions": ["asthma", "COPD", "bronchitis", "breathing difficulties"],
                "description": "Bronchodilator that relaxes airways to improve breathing. Also known as albuterol.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "metronidazole": {
                "uses": ["antibiotic treatment", "antiprotozoal treatment"],
                "conditions": ["bacterial infections", "parasitic infections", "dental infections", "rosacea"],
                "description": "Antibiotic and antiprotozoal medication for various infections.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Safe during breastfeeding"
            },
            "fluoxetine": {
                "uses": ["depression treatment", "anxiety treatment"],
                "conditions": ["depression", "anxiety disorders", "panic disorder", "OCD", "bulimia nervosa"],
                "description": "Selective serotonin reuptake inhibitor (SSRI) antidepressant.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "losartan": {
                "uses": ["blood pressure control", "kidney protection"],
                "conditions": ["hypertension", "diabetic nephropathy", "heart failure"],
                "description": "Angiotensin receptor blocker for blood pressure control.",
                "pregnancy_category": "D",
                "pregnancy_safety": "Contraindicated in pregnancy, especially in the second and third trimesters",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "methotrexate": {
                "uses": ["immune system suppression", "cancer treatment"],
                "conditions": ["rheumatoid arthritis", "psoriasis", "certain cancers"],
                "description": "Immunosuppressant and chemotherapy medication.",
                "pregnancy_category": "X",
                "pregnancy_safety": "Contraindicated in pregnancy due to high risk of fetal abnormalities",
                "lactation_category": "unsafe",
                "lactation_safety": "Not recommended during breastfeeding"
            },
            "insulin": {
                "uses": ["blood sugar control", "diabetes management"],
                "conditions": ["type 1 diabetes", "type 2 diabetes", "gestational diabetes"],
                "description": "Hormone for controlling blood glucose levels in diabetes.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding"
            },
            "levothyroxine": {
                "uses": ["thyroid hormone replacement"],
                "conditions": ["hypothyroidism", "goiter", "thyroid cancer"],
                "description": "Synthetic thyroid hormone for treating thyroid hormone deficiency.",
                "pregnancy_category": "A",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding"
            },
            "azithromycin": {
                "uses": ["bacterial infection treatment"],
                "conditions": ["respiratory infections", "skin infections", "ear infections", "sexually transmitted infections"],
                "description": "Macrolide antibiotic for various bacterial infections.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Safe during breastfeeding"
            },
            "warfarin": {
                "uses": ["blood clot prevention", "stroke prevention"],
                "conditions": ["deep vein thrombosis", "pulmonary embolism", "atrial fibrillation"],
                "description": "Anticoagulant (blood thinner) to prevent blood clots.",
                "pregnancy_category": "X",
                "pregnancy_safety": "Contraindicated in pregnancy due to risk of fetal bleeding and malformations",
                "lactation_category": "unsafe",
                "lactation_safety": "Not recommended during breastfeeding"
            },
            "prednisone": {
                "uses": ["inflammation reduction", "immune system suppression"],
                "conditions": ["severe allergies", "asthma", "arthritis", "lupus", "skin conditions"],
                "description": "Corticosteroid used to treat various inflammatory conditions.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "sertraline": {
                "uses": ["depression treatment", "anxiety treatment"],
                "conditions": ["depression", "panic disorder", "social anxiety disorder", "PTSD"],
                "description": "SSRI antidepressant for various mental health conditions.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "atorvastatin": {
                "uses": ["cholesterol reduction", "cardiovascular disease prevention"],
                "conditions": ["high cholesterol", "heart disease risk", "atherosclerosis"],
                "description": "Statin medication for reducing cholesterol levels.",
                "pregnancy_category": "X",
                "pregnancy_safety": "Contraindicated in pregnancy due to risk of fetal harm",
                "lactation_category": "unsafe",
                "lactation_safety": "Not recommended during breastfeeding"
            },
            "ciprofloxacin": {
                "uses": ["bacterial infection treatment"],
                "conditions": ["urinary tract infections", "skin infections", "bone infections", "joint infections", "gastroenteritis"],
                "description": "Broad-spectrum fluoroquinolone antibiotic for treating various bacterial infections.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "hydrochlorothiazide": {
                "uses": ["blood pressure reduction", "fluid retention treatment"],
                "conditions": ["hypertension", "edema", "heart failure", "kidney stones"],
                "description": "Thiazide diuretic used to treat high blood pressure and fluid retention.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "simvastatin": {
                "uses": ["cholesterol reduction", "cardiovascular disease prevention"],
                "conditions": ["high cholesterol", "cardiovascular disease", "atherosclerosis"],
                "description": "Statin medication that lowers cholesterol and triglycerides in the blood.",
                "pregnancy_category": "X",
                "pregnancy_safety": "Contraindicated in pregnancy due to risk of fetal harm",
                "lactation_category": "unsafe",
                "lactation_safety": "Not recommended during breastfeeding"
            },
            "escitalopram": {
                "uses": ["depression treatment", "anxiety treatment"],
                "conditions": ["major depressive disorder", "generalized anxiety disorder", "social anxiety disorder", "panic disorder"],
                "description": "Selective serotonin reuptake inhibitor (SSRI) for depression and anxiety disorders.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "pantoprazole": {
                "uses": ["acid reduction", "ulcer treatment"],
                "conditions": ["gastric ulcers", "duodenal ulcers", "GERD", "Zollinger-Ellison syndrome"],
                "description": "Proton pump inhibitor that reduces stomach acid production.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "montelukast": {
                "uses": ["asthma prevention", "allergy treatment"],
                "conditions": ["asthma", "seasonal allergies", "exercise-induced bronchoconstriction"],
                "description": "Leukotriene receptor antagonist for asthma and allergy prevention.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Safe during breastfeeding"
            },
            "gabapentin": {
                "uses": ["nerve pain treatment", "seizure prevention"],
                "conditions": ["neuropathic pain", "epilepsy", "postherpetic neuralgia", "restless legs syndrome"],
                "description": "Anticonvulsant and nerve pain medication.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "tramadol": {
                "uses": ["pain relief"],
                "conditions": ["moderate to severe pain", "chronic pain", "post-surgical pain"],
                "description": "Opioid pain medication for moderate to severe pain.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "venlafaxine": {
                "uses": ["depression treatment", "anxiety treatment"],
                "conditions": ["major depressive disorder", "generalized anxiety disorder", "panic disorder", "social anxiety disorder"],
                "description": "Serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "allopurinol": {
                "uses": ["uric acid reduction", "gout prevention"],
                "conditions": ["gout", "kidney stones", "high uric acid levels"],
                "description": "Medication that reduces uric acid production in the body.",
                "pregnancy_category": "C",
                "pregnancy_safety": "Use only if benefit outweighs risk in pregnancy",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "metoclopramide": {
                "uses": ["nausea treatment", "gastric motility improvement"],
                "conditions": ["nausea", "vomiting", "gastroparesis", "acid reflux"],
                "description": "Anti-nausea medication that also improves gut motility.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding"
            },
            "carbamazepine": {
                "uses": ["seizure prevention", "nerve pain treatment"],
                "conditions": ["epilepsy", "trigeminal neuralgia", "bipolar disorder"],
                "description": "Anticonvulsant and mood stabilizing medication.",
                "pregnancy_category": "D",
                "pregnancy_safety": "Evidence of human fetal risk exists, use only if benefit outweighs risk",
                "lactation_category": "caution",
                "lactation_safety": "Limited data available, consult healthcare provider"
            },
            "clopidogrel": {
                "uses": ["blood clot prevention"],
                "conditions": ["heart attack prevention", "stroke prevention", "peripheral artery disease"],
                "description": "Antiplatelet medication that prevents blood clots.",
                "pregnancy_category": "B",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Safe during breastfeeding"
            },
            "doxycycline": {
                "uses": ["bacterial infection treatment", "malaria prevention"],
                "conditions": ["bacterial infections", "acne", "malaria", "respiratory tract infections", "sexually transmitted infections"],
                "description": "Broad-spectrum tetracycline antibiotic.",
                "pregnancy_category": "D",
                "pregnancy_safety": "Contraindicated in pregnancy due to risk of fetal harm",
                "lactation_category": "unsafe",
                "lactation_safety": "Not recommended during breastfeeding"
            },
            "folic_acid": {
                "uses": ["vitamin supplementation", "anemia prevention"],
                "conditions": ["folate deficiency", "pregnancy", "anemia", "neural tube defects prevention"],
                "description": "B-vitamin supplement essential for cell growth and DNA synthesis.",
                "pregnancy_category": "A",
                "pregnancy_safety": "Generally considered safe during pregnancy",
                "lactation_category": "safe",
                "lactation_safety": "Compatible with breastfeeding"
            }
        }
        
        # Update existing medicines with default safety info
        self._update_medicine_info()

    def _update_medicine_info(self):
        """Updates existing medicines with dosage, contraindications, and safety info."""
        default_info = {
            "dosage": {
                "adult": "Consult physician for proper dosing",
                "child": "Consult physician for proper dosing",
                "form": ["tablet"]
            },
            "contraindications": [
                "Known hypersensitivity",
                "Consult physician for complete list"
            ],
            "side_effects": [
                "Consult physician or package insert for complete list"
            ],
            "precautions": [
                "Consult physician before use",
                "Follow prescribed dosage carefully"
            ],
            "pregnancy_category": "C",
            "pregnancy_safety": "Insufficient data available, use only if benefit outweighs risk",
            "lactation_category": "caution",
            "lactation_safety": "Limited data available, consult healthcare provider"
        }
        
        # Update all medicines with default info if not present
        for medicine in self._medicines.values():
            for key, value in default_info.items():
                if key not in medicine:
                    medicine[key] = value

    def search_by_condition(self, condition: str) -> List[Dict]:
        """
        Search for medicines that treat a specific condition.
        
        Args:
            condition: The medical condition or symptom to search for
            
        Returns:
            List of medicines that can treat the condition
        """
        condition_lower = condition.lower()
        result = []
        
        # Check for condition aliases
        search_terms = [condition_lower]
        for alias, variants in self._condition_aliases.items():
            if condition_lower in alias.lower() or any(condition_lower in v.lower() for v in variants):
                search_terms.extend([v.lower() for v in variants])
                search_terms.append(alias.lower())
        
        # Search through medicines with all possible terms
        for generic_name, info in self._medicines.items():
            conditions_lower = [c.lower() for c in info['conditions']]
            if any(term in conditions_lower or 
                  any(term in c for c in conditions_lower) 
                  for term in search_terms):
                result.append({
                    "generic_name": generic_name,
                    **info
                })
        return result

    def search_by_category(self, category: str) -> List[Dict]:
        """
        Search for medicines by their category.
        
        Args:
            category: The category to search for (e.g., 'antibiotics', 'painkillers')
            
        Returns:
            List of medicines in that category
        """
        category_lower = category.lower()
        result = []
        
        # Find matching category
        for cat, medicines in self._categories.items():
            if category_lower in cat.lower():
                # Get all medicines in this category
                for medicine in medicines:
                    if medicine in self._medicines:
                        result.append({
                            "generic_name": medicine,
                            "category": cat,
                            **self._medicines[medicine]
                        })
        return result

    def get_all_categories(self) -> List[str]:
        """
        Get a list of all available medicine categories.
        
        Returns:
            List of category names
        """
        return list(self._categories.keys())

    def get_medicine_info(self, generic_name: str) -> Optional[Dict]:
        """
        Get detailed information about a medicine by its generic name.
        
        Args:
            generic_name: The generic name of the medicine
            
        Returns:
            Dictionary containing medicine information or None if not found
        """
        if generic_name.lower() in self._medicines:
            return {
                "generic_name": generic_name.lower(),
                **self._medicines[generic_name.lower()]
            }
        return None

    def add_medicine(self, generic_name: str, uses: List[str], 
                    conditions: List[str], description: str) -> None:
        """
        Add a new medicine to the database.
        
        Args:
            generic_name: The generic name of the medicine
            uses: List of uses for the medicine
            conditions: List of conditions the medicine treats
            description: Detailed description of the medicine
        """
        self._medicines[generic_name.lower()] = {
            "uses": uses,
            "conditions": conditions,
            "description": description
        }

    def search_by_side_effect(self, side_effect: str) -> List[Dict]:
        """
        Search for medicines by a specific side effect.
        
        Args:
            side_effect: The side effect to search for
            
        Returns:
            List of medicines that may cause this side effect
        """
        side_effect_lower = side_effect.lower()
        result = []
        
        for generic_name, info in self._medicines.items():
            if any(side_effect_lower in s.lower() for s in info.get('side_effects', [])):
                result.append({
                    "generic_name": generic_name,
                    **info
                })
        return result

    def search_by_form(self, form: str) -> List[Dict]:
        """
        Search for medicines by their form (tablet, syrup, etc.).
        
        Args:
            form: The form to search for
            
        Returns:
            List of medicines available in that form
        """
        form_lower = form.lower()
        result = []
        
        for generic_name, info in self._medicines.items():
            if 'dosage' in info and 'form' in info['dosage']:
                if any(form_lower in f.lower() for f in info['dosage']['form']):
                    result.append({
                        "generic_name": generic_name,
                        **info
                    })
        return result

    def get_contraindications(self, generic_name: str) -> List[str]:
        """
        Get contraindications for a specific medicine.
        
        Args:
            generic_name: The generic name of the medicine
            
        Returns:
            List of contraindications
        """
        info = self.get_medicine_info(generic_name)
        if info and 'contraindications' in info:
            return info['contraindications']
        return []

    def get_dosage_info(self, generic_name: str) -> Optional[Dict]:
        """
        Get dosage information for a specific medicine.
        
        Args:
            generic_name: The generic name of the medicine
            
        Returns:
            Dictionary containing dosage information or None if not found
        """
        info = self.get_medicine_info(generic_name)
        if info and 'dosage' in info:
            return info['dosage']
        return None

    def get_pregnancy_safety(self, generic_name: str) -> Dict:
        """
        Get pregnancy safety information for a medicine.
        
        Args:
            generic_name: The generic name of the medicine
            
        Returns:
            Dictionary containing pregnancy category and safety information
        """
        info = self.get_medicine_info(generic_name)
        if info:
            return {
                "category": info.get("pregnancy_category"),
                "category_description": self._pregnancy_categories.get(info.get("pregnancy_category", ""), ""),
                "safety_info": info.get("pregnancy_safety")
            }
        return None

    def get_lactation_safety(self, generic_name: str) -> Dict:
        """
        Get breastfeeding safety information for a medicine.
        
        Args:
            generic_name: The generic name of the medicine
            
        Returns:
            Dictionary containing lactation category and safety information
        """
        info = self.get_medicine_info(generic_name)
        if info:
            return {
                "category": info.get("lactation_category"),
                "category_description": self._lactation_categories.get(info.get("lactation_category", ""), ""),
                "safety_info": info.get("lactation_safety")
            }
        return None

    def search_safe_in_pregnancy(self, category: str = "A") -> List[Dict]:
        """
        Search for medicines that are safe during pregnancy by category.
        
        Args:
            category: The pregnancy category to search for (A, B, C, D, or X)
            
        Returns:
            List of medicines in that pregnancy category
        """
        result = []
        for generic_name, info in self._medicines.items():
            if info.get("pregnancy_category", "") == category.upper():
                result.append({
                    "generic_name": generic_name,
                    "pregnancy_category": category.upper(),
                    "pregnancy_safety": info.get("pregnancy_safety"),
                    "description": info.get("description")
                })
        return result

    def search_safe_in_lactation(self, category: str = "safe") -> List[Dict]:
        """
        Search for medicines that are safe during breastfeeding by category.
        
        Args:
            category: The lactation category to search for
            
        Returns:
            List of medicines in that lactation category
        """
        result = []
        for generic_name, info in self._medicines.items():
            if info.get("lactation_category", "") == category.lower():
                result.append({
                    "generic_name": generic_name,
                    "lactation_category": category.lower(),
                    "lactation_safety": info.get("lactation_safety"),
                    "description": info.get("description")
                })
        return result
