# Moon Calendar

A 2-month calendar application that displays moon phases and astrological signs for each day.

## Features

- **Moon Phase Tracking**: Displays the current moon phase for each day with appropriate icons
- **Zodiac Sign Display**: Shows the zodiac sign for each day
- **Biodynamic Farming Guide**: Color-coded calendar days based on the element (Earth, Water, Air, Fire) associated with each zodiac sign
- **Plant Recommendations**: Suggests which plants to work with based on the zodiac sign's element
- **Interactive Calendar UI**: Easy-to-use interface with navigation between months
- **Local SQLite Database Storage**: Stores moon phase and zodiac data locally
- Fetches moon phase and astrological sign data from a free API

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

## Biodynamic Farming Information

The calendar includes biodynamic farming information based on astrological signs:

- **Earth Signs (Virgo, Capricorn, Taurus)**: Best for root vegetables (Carrot, Potato, Beetroot, etc.)
- **Water Signs (Scorpio, Pisces, Cancer)**: Best for leafy vegetables (Spinach, Lettuce, Kale, etc.)
- **Air Signs (Libra, Aquarius, Gemini)**: Best for flowering plants (Broccoli, Cauliflower, etc.)
- **Fire Signs (Sagittarius, Aries, Leo)**: Best for fruits and seeds (Tomatoes, Beans, Peppers, etc.)

## Database Schema

The application uses a simple SQLite database with a single table:
- `calendar_data`: Stores date, moon phase, and zodiac sign information
