# Moon Calendar

A 2-month calendar application that displays moon phases and astrological signs for each day.

## Features

- Fetches moon phase and astrological sign data from a free API
- Stores data in a local SQLite database
- Displays a 2-month calendar with the collected information

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the data fetcher to populate the database:
   ```
   python src/fetch_data.py
   ```

3. Run the calendar application:
   ```
   python src/app.py
   ```

## API Used

This project uses the ViewBits Moon Phase API, which provides:
- Moon phase information
- Moon illumination percentage
- Moon age
- Moon distance from Earth
- Moon's zodiac sign

## Database Schema

The application uses a simple SQLite database with a single table:
- `calendar_data`: Stores date, moon phase, and zodiac sign information
