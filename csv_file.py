import csv

# Data to be written
data = [
    ['Name', 'Age', 'Country'],
    ['John', 25, 'USA'],
    ['Alice', 30, 'Canada'],
    ['Bob', 28, 'UK']
]

# Open the CSV file
with open('data.csv', 'w', newline='') as file:
    # Create a CSV writer
    writer = csv.writer(file)

    # Write data to the file
    writer.writerows(data)

# Open the CSV file 
with open('data.csv', 'r') as file: 

   # Create a CSV reader 
   reader = csv.reader(file) 

   # Skip header if needed
   # next(reader)

   # Iterate over the rows 
   for row in reader: 
      # Access the data in each row 
      print(row)