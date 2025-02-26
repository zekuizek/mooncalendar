"""
Module containing biodynamic farming data and relationships with zodiac signs.
"""

# Zodiac signs grouped by element and corresponding plant part
ZODIAC_ELEMENTS = {
    # Earth signs - Root
    "Virgo": {"element": "Earth", "plant_part": "Root"},
    "Capricorn": {"element": "Earth", "plant_part": "Root"},
    "Taurus": {"element": "Earth", "plant_part": "Root"},
    
    # Water signs - Leaf
    "Scorpio": {"element": "Water", "plant_part": "Leaf"},
    "Pisces": {"element": "Water", "plant_part": "Leaf"},
    "Cancer": {"element": "Water", "plant_part": "Leaf"},
    
    # Air signs - Flower
    "Libra": {"element": "Air", "plant_part": "Flower"},
    "Aquarius": {"element": "Air", "plant_part": "Flower"},
    "Gemini": {"element": "Air", "plant_part": "Flower"},
    
    # Fire signs - Fruit/Seed
    "Sagittarius": {"element": "Fire", "plant_part": "Fruit/Seed"},
    "Aries": {"element": "Fire", "plant_part": "Fruit/Seed"},
    "Leo": {"element": "Fire", "plant_part": "Fruit/Seed"}
}

# Plants grouped by the part that is harvested
PLANT_CATEGORIES = {
    "Root": [
        "Carrot", "Potato", "Beetroot", "Parsnip", "Turnip", 
        "Swede", "Onion", "Shallot", "Garlic", "Radish"
    ],
    "Leaf": [
        "Spinach", "Lettuce", "Kale", "Cabbage", "Swiss Chard", 
        "Rocket", "Watercress", "Collard Greens", "Herbs"
    ],
    "Flower": [
        "Ornamental Flowers", "Broccoli", "Cauliflower", 
        "Brussels Sprouts", "Artichoke"
    ],
    "Fruit/Seed": [
        "Tomatoes", "Beans", "Pepper", "Cucumber", "Aubergine", 
        "Courgette", "Pumpkin", "Squash", "Apples", "Plums"
    ]
}

def get_element_for_sign(zodiac_sign):
    """
    Get the element associated with a zodiac sign.
    
    Args:
        zodiac_sign (str): The zodiac sign
        
    Returns:
        str: The element (Earth, Water, Air, Fire) or None if not found
    """
    sign_data = ZODIAC_ELEMENTS.get(zodiac_sign)
    return sign_data.get("element") if sign_data else None

def get_plant_part_for_sign(zodiac_sign):
    """
    Get the plant part associated with a zodiac sign.
    
    Args:
        zodiac_sign (str): The zodiac sign
        
    Returns:
        str: The plant part (Root, Leaf, Flower, Fruit/Seed) or None if not found
    """
    sign_data = ZODIAC_ELEMENTS.get(zodiac_sign)
    return sign_data.get("plant_part") if sign_data else None

def get_plants_for_sign(zodiac_sign):
    """
    Get the plants associated with a zodiac sign.
    
    Args:
        zodiac_sign (str): The zodiac sign
        
    Returns:
        list: List of plants or empty list if not found
    """
    plant_part = get_plant_part_for_sign(zodiac_sign)
    return PLANT_CATEGORIES.get(plant_part, [])

def get_biodynamic_info(zodiac_sign):
    """
    Get complete biodynamic information for a zodiac sign.
    
    Args:
        zodiac_sign (str): The zodiac sign
        
    Returns:
        dict: Dictionary with element, plant_part, and plants
    """
    element = get_element_for_sign(zodiac_sign)
    plant_part = get_plant_part_for_sign(zodiac_sign)
    plants = get_plants_for_sign(zodiac_sign)
    
    return {
        "element": element,
        "plant_part": plant_part,
        "plants": plants
    }
