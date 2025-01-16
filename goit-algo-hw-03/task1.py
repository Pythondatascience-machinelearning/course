from datetime import datetime, date

def get_days_from_today(input_date):
    
    try:
        date_object = datetime.strptime(input_date, "%Y-%m-%d").date()
        delta = date.today() - date_object
        return delta.days
    except ValueError:
        return None
    if not input_date:
        return None

dates = ["2024-12-30", "2025-01-01", "invalid-date", ""]
results = []
for d in dates:
    result = get_days_from_today(d)
    if result is not None:
        results.append(f"Date: {d}, Days Difference: {result}")
    else:
        results.append(f"invalid format")
print("\n".join(results))






