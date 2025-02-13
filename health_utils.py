def calculate_bmi(height, weight):
    """Calcule le BMI."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """Calcule le BMR selon la formule Harris-Benedict."""
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight, and age must be positive values.")
    
    # Supprimer la multiplication par 100 puisque `height` est déjà en centimètres
    # height_in_cm = height * 100  # À retirer
    
    if gender.lower() == "male":
        # Formule de Harris-Benedict pour les hommes
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == "female":
        # Formule de Harris-Benedict pour les femmes
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'")
