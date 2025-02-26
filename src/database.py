"""
Database module for the Moon Calendar application using direct SQLite3 instead of SQLAlchemy.
"""
import os
import sqlite3
import datetime
from biodynamic_data import get_biodynamic_info

# Create the database directory if it doesn't exist
os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'), exist_ok=True)

# Define the database connection
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'moon_calendar.db')

def get_connection():
    """
    Get a new database connection.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_db():
    """
    Initialize the database by creating all tables.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create the calendar_data table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calendar_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL UNIQUE,
        moon_phase TEXT NOT NULL,
        illumination TEXT,
        moon_age TEXT,
        moon_distance TEXT,
        moon_sign TEXT NOT NULL,
        element TEXT,
        plant_part TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def save_calendar_data(date_obj, moon_phase, illumination, moon_age, moon_distance, moon_sign):
    """
    Save or update calendar data in the database.
    
    Args:
        date_obj (datetime.date): The date
        moon_phase (str): The moon phase
        illumination (str): The moon illumination percentage
        moon_age (str): The moon age
        moon_distance (str): The moon distance from Earth
        moon_sign (str): The zodiac sign
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Convert date to string format
    date_str = date_obj.strftime('%Y-%m-%d')
    
    # Get biodynamic information based on the zodiac sign
    biodynamic_info = get_biodynamic_info(moon_sign)
    element = biodynamic_info.get('element', '')
    plant_part = biodynamic_info.get('plant_part', '')
    
    # Check if the date already exists
    cursor.execute('SELECT id FROM calendar_data WHERE date = ?', (date_str,))
    existing = cursor.fetchone()
    
    if existing:
        # Update existing entry
        cursor.execute('''
        UPDATE calendar_data
        SET moon_phase = ?, illumination = ?, moon_age = ?, moon_distance = ?, moon_sign = ?,
            element = ?, plant_part = ?
        WHERE date = ?
        ''', (moon_phase, illumination, moon_age, moon_distance, moon_sign, 
              element, plant_part, date_str))
    else:
        # Insert new entry
        cursor.execute('''
        INSERT INTO calendar_data 
        (date, moon_phase, illumination, moon_age, moon_distance, moon_sign, element, plant_part)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date_str, moon_phase, illumination, moon_age, moon_distance, moon_sign,
              element, plant_part))
    
    conn.commit()
    conn.close()

def get_month_data(year, month):
    """
    Get calendar data for a specific month.
    
    Args:
        year (int): The year
        month (int): The month (1-12)
        
    Returns:
        dict: Dictionary with day numbers as keys and data as values
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Calculate the first and last day of the month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    start_date = f"{year}-{month:02d}-01"
    end_date = f"{next_year}-{next_month:02d}-01"
    
    cursor.execute('''
    SELECT * FROM calendar_data
    WHERE date >= ? AND date < ?
    ORDER BY date
    ''', (start_date, end_date))
    
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to a dictionary with day numbers as keys
    result = {}
    for row in rows:
        day = datetime.datetime.strptime(row['date'], '%Y-%m-%d').day
        result[day] = dict(row)
    
    return result


if __name__ == "__main__":
    # Initialize the database if this script is run directly
    init_db()
    print(f"Database initialized at {DB_PATH}")
