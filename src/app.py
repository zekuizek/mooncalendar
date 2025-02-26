"""
Flask application to display the moon calendar.
"""
import calendar
import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request
from database import init_db, get_month_data

app = Flask(__name__)

@app.route('/')
def index():
    """
    Display the moon calendar for the current and next month.
    """
    # Get the current date
    today = datetime.date.today()
    
    # Get the month to display (default to current month)
    month_param = request.args.get('month', today.month)
    year_param = request.args.get('year', today.year)
    
    try:
        month = int(month_param)
        year = int(year_param)
    except ValueError:
        month = today.month
        year = today.year
    
    # Calculate the next month
    next_month_date = datetime.date(year, month, 1) + relativedelta(months=1)
    next_month = next_month_date.month
    next_month_year = next_month_date.year
    
    # Get calendar data from the database
    current_month_dict = get_month_data(year, month)
    next_month_dict = get_month_data(next_month_year, next_month)
    
    # Get calendar information
    cal = calendar.monthcalendar(year, month)
    next_cal = calendar.monthcalendar(next_month_year, next_month)
    
    # Get month names
    month_name = calendar.month_name[month]
    next_month_name = calendar.month_name[next_month]
    
    return render_template(
        'index.html',
        today=today,
        year=year,
        month=month,
        month_name=month_name,
        calendar=cal,
        month_data=current_month_dict,
        next_month=next_month,
        next_month_year=next_month_year,
        next_month_name=next_month_name,
        next_calendar=next_cal,
        next_month_data=next_month_dict
    )


if __name__ == '__main__':
    # Initialize the database
    init_db()
    
    # Run the Flask app
    app.run(debug=True)
