import csv


def add_record_to_csv(file_path, record):
    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the record as a new row in the CSV file
        writer.writerow(record)


# Example usage
file_path = 'data.csv'  # Replace with the path to your CSV file
# Replace with your new record data
new_record = ['Karnataka', 'Nan', '', '', '02-07-2023', 150.5]

add_record_to_csv(file_path, new_record)
