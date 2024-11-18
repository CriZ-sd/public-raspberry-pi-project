import csv

# Read the CSV file
csv_file = "temperature_humidity_data.csv"
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Temperature: {row['Temperature']}°C, Humidity: {row['Humidity']}%")
