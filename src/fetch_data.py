"""
Script to fetch or generate moon data for the calendar.
"""
import datetime
import random
import sqlite3
from dateutil.relativedelta import relativedelta
from database import init_db, save_calendar_data

# Moon phases in order
MOON_PHASES = [
    "New Moon", 
    "Waxing Crescent", 
    "First Quarter", 
    "Waxing Gibbous", 
    "Full Moon", 
    "Waning Gibbous", 
    "Last Quarter", 
    "Waning Crescent"
]

# Zodiac signs in order
ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", 
    "Leo", "Virgo", "Libra", "Scorpio", 
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def generate_sample_data(start_date, num_days=30):
    """
    Generate sample moon data for a given period.
    
    Args:
        start_date (datetime.date): The start date
        num_days (int): Number of days to generate data for
        
    Returns:
        list: List of dictionaries with moon data
    """
    # Initialize the database
    init_db()
    
    # Set initial moon phase and zodiac sign
    current_phase_index = random.randint(0, len(MOON_PHASES) - 1)
    current_sign_index = random.randint(0, len(ZODIAC_SIGNS) - 1)
    
    # Generate data for each day
    for day_offset in range(num_days):
        current_date = start_date + datetime.timedelta(days=day_offset)
        
        # Change moon phase every 3-4 days
        if day_offset % random.randint(3, 4) == 0 and day_offset > 0:
            current_phase_index = (current_phase_index + 1) % len(MOON_PHASES)
        
        # Change zodiac sign every 2-3 days
        if day_offset % random.randint(2, 3) == 0 and day_offset > 0:
            current_sign_index = (current_sign_index + 1) % len(ZODIAC_SIGNS)
        
        # Generate random illumination percentage based on moon phase
        if MOON_PHASES[current_phase_index] == "New Moon":
            illumination = f"{random.randint(0, 5)}%"
        elif MOON_PHASES[current_phase_index] == "Full Moon":
            illumination = f"{random.randint(95, 100)}%"
        elif "Crescent" in MOON_PHASES[current_phase_index]:
            illumination = f"{random.randint(10, 40)}%"
        elif "Quarter" in MOON_PHASES[current_phase_index]:
            illumination = f"{random.randint(45, 55)}%"
        elif "Gibbous" in MOON_PHASES[current_phase_index]:
            illumination = f"{random.randint(60, 90)}%"
        
        # Generate random moon age (0-29 days)
        moon_age = f"{random.randint(0, 29)} days"
        
        # Generate random moon distance
        moon_distance = f"{random.randint(356000, 406000)} km"
        
        # Save to database
        save_calendar_data(
            current_date,
            MOON_PHASES[current_phase_index],
            illumination,
            moon_age,
            moon_distance,
            ZODIAC_SIGNS[current_sign_index]
        )

def fetch_api_data(start_date, num_days=30):
    """
    Fetch moon data from an API for a given period.
    This is a placeholder for future API integration.
    
    Args:
        start_date (datetime.date): The start date
        num_days (int): Number of days to fetch data for
    """
    # This would be implemented with actual API calls
    # For now, we'll use the sample data generator
    generate_sample_data(start_date, num_days)

if __name__ == "__main__":
    # Generate data for the current month and the next month
    today = datetime.date.today()
    first_day_current_month = today.replace(day=1)
    first_day_next_month = (first_day_current_month + relativedelta(months=1))
    
    # Generate two months of data
    generate_sample_data(first_day_current_month, 31)  # Current month
    generate_sample_data(first_day_next_month, 31)     # Next month
    
    print("Sample moon data generated for the current and next month.")
