import json

def get_employee_names(json_str):
    data = json.loads(json_str)
    names = [emp["name"] for emp in data["employees"]]
    return names


# Example
json_str = '{"employees": [{"name": "Alice", "dept": "HR"}, {"name": "Bob", "dept": "Engineering"}]}'
print(get_employee_names(json_str))
# Output: ['Alice', 'Bob']

