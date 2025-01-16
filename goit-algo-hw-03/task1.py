from datetime import datetime, date, timedelta

def get_days_from_today(input_date):
    try:
        date_object= datetime.strptime(input_date, "%Y-%m-%d").date()
        delta= date.today() - date_object
        return delta.days
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    

print(get_days_from_today("2024-12-30"))






