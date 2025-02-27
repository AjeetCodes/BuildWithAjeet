import json

# JSON String to Python Dictionary
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
python_dict = json.loads(json_data)
print("Loaded JSON:", python_dict)

# Convert Python Dictionary to JSON String
data = {"name": "Bob", "age": 30, "city": "London"}
json_string = json.dumps(data, indent=4)
print("\nJSON String:\n", json_string)

# Write JSON to a File
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
print("\nData written to 'output.json'")

# Read JSON from a File
with open("output.json", "r") as file:
    file_data = json.load(file)
print("\nData read from 'output.json':", file_data)
