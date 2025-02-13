import unittest
import sys
import os

# Ajouter le répertoire courant au PATH pour éviter les erreurs d'import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import des fonctions à tester depuis health_utils.py
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        """Test du calcul du BMI"""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr_male(self):
        """Test du calcul du BMR pour un homme (height en cm)"""
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, "male"), 1724.05, places=2)  # Valeur ajustée

    def test_calculate_bmr_female(self):
        """Test du calcul du BMR pour une femme (height en cm)"""
        self.assertAlmostEqual(calculate_bmr(160, 55, 25, "female"), 1343.61, places=2)  # Valeur ajustée

if __name__ == "__main__":
    unittest.main()
