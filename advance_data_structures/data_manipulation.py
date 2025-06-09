# Data Manipulation – Clean & Aggregate Data

sales_data = [
    {"date": "2025-06-01", "region": "West", "sales": 200},
    {"date": "2025-06-01", "region": "East", "sales": None},
    {"date": "2025-06-02", "region": "West", "sales": 300},
    {"date": "2025-06-02", "region": "East", "sales": 150},
]

# Write a function to:
# Remove entries with missing sales values.
# Compute total sales per region.

def total_sales_by_region(data):
    cleaned = [entry for entry in data if entry['sales'] is not None]
    result = {}
    for entry in cleaned:
        region = entry['region']
        result[region] = result.get(region, 0) + entry['sales']
    return result

print(total_sales_by_region(sales_data))
