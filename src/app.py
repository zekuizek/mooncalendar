"""
Flask application for the Moon Calendar.
"""
import datetime
import calendar
from flask import Flask, render_template, request
from database import get_month_data, init_db
from biodynamic_data import ZODIAC_ELEMENTS, PLANT_CATEGORIES

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the calendar page.
    """
    # Get the requested month and year, default to current month
    today = datetime.date.today()
    month = int(request.args.get('month', today.month))
    year = int(request.args.get('year', today.year))
    
    # Calculate next month for navigation
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    # Calculate previous month for navigation
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    
    # Get the calendar data for current and next month
    months_data = []
    
    # Current month
    month_data = {
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
        'days_in_month': calendar.monthrange(year, month)[1],
        'first_day_weekday': calendar.monthrange(year, month)[0],
        'calendar_data': get_month_data(year, month)
    }
    months_data.append(month_data)
    
    # Next month
    next_month_data = {
        'year': next_year,
        'month': next_month,
        'month_name': calendar.month_name[next_month],
        'days_in_month': calendar.monthrange(next_year, next_month)[1],
        'first_day_weekday': calendar.monthrange(next_year, next_month)[0],
        'calendar_data': get_month_data(next_year, next_month)
    }
    months_data.append(next_month_data)
    
    return render_template(
        'index.html',
        months=months_data,
        today=today,
        prev_month=prev_month,
        prev_year=prev_year,
        next_month=next_month,
        next_year=next_year,
        zodiac_elements=ZODIAC_ELEMENTS,
        plant_categories=PLANT_CATEGORIES
    )

if __name__ == '__main__':
    # Initialize the database
    init_db()
    app.run(debug=True, port=5001)
