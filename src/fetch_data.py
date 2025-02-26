"""
Script to generate sample moon phase and zodiac sign data for testing.
"""
import datetime
from dateutil.relativedelta import relativedelta
from database import init_db, save_calendar_data

def generate_sample_data():
    """
    Generate sample moon phase and zodiac sign data for one month.
    """
    # Initialize the database
    init_db()
    
    # Calculate start and end dates
    today = datetime.date.today()
    end_date = today + relativedelta(months=1)
    
    # Sample moon phases in order
    moon_phases = [
        "New Moon", 
        "Waxing Crescent", 
        "First Quarter", 
        "Waxing Gibbous", 
        "Full Moon", 
        "Waning Gibbous", 
        "Last Quarter", 
        "Waning Crescent"
    ]
    
    # Sample zodiac signs
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", 
        "Leo", "Virgo", "Libra", "Scorpio", 
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    
    # Generate data for each day
    current_date = today
    phase_index = 0
    zodiac_index = today.month % 12
    
    all_data = []
    
    while current_date < end_date:
        # Get moon phase (changes every ~3.5 days)
        if current_date.day % 4 == 0:
            phase_index = (phase_index + 1) % len(moon_phases)
        
        # Get zodiac sign (changes every ~2.5 days)
        if current_date.day % 3 == 0:
            zodiac_index = (zodiac_index + 1) % len(zodiac_signs)
        
        # Calculate illumination based on moon phase
        if moon_phases[phase_index] == "New Moon":
            illumination = "0%"
        elif moon_phases[phase_index] == "Full Moon":
            illumination = "100%"
        elif "Waxing" in moon_phases[phase_index]:
            illumination = f"{25 + (moon_phases.index(moon_phases[phase_index]) * 15)}%"
        else:
            illumination = f"{100 - (moon_phases.index(moon_phases[phase_index]) * 15)}%"
        
        # Create sample data
        day_data = {
            "date": current_date.strftime('%Y-%m-%d'),
            "phase": moon_phases[phase_index],
            "illumination": illumination,
            "moon_age": f"{current_date.day % 30} days",
            "moon_distance": f"{356000 + (current_date.day * 1000)} km",
            "moon_sign": zodiac_signs[zodiac_index]
        }
        
        # Save to database
        save_calendar_data(
            date_obj=current_date,
            moon_phase=day_data['phase'],
            illumination=day_data['illumination'],
            moon_age=day_data['moon_age'],
            moon_distance=day_data['moon_distance'],
            moon_sign=day_data['moon_sign']
        )
        
        all_data.append(day_data)
        current_date += datetime.timedelta(days=1)
    
    return all_data


if __name__ == "__main__":
    print("Generating sample moon phase and zodiac sign data for one month...")
    data = generate_sample_data()
    print(f"Successfully generated and stored sample data for {len(data)} days.")
    print("Data is stored in the SQLite database and will be available for future runs.")
