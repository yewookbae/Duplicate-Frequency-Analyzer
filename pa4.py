#Christian Bae
import csv
import sys

def process_input(input_filename, output_filename):
    # Dictionary to store the count of each number
    counts = {}
    # Open the input CSV file for reading
    with open(input_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert the first element of each row to an integer
            number = int(row[0])
            # Increment the count for the number in the dictionary
            counts[number] = counts.get(number, 0) + 1

    # Sort the dictionary items by count in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # Filter out numbers with a count of 1 (non-duplicates)
    filtered_counts = [(num, count) for num, count in sorted_counts if count > 1]

    # Open the output CSV file for writing
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write each number and its count to the output file
        if filtered_counts:
            for num, count in filtered_counts:
                writer.writerow([num, count])

if __name__ == "__main__":
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python pa4.py input_filename output_filename")
        sys.exit(1)

    # Get input and output file names from command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Process the input file and generate the output file
    process_input(input_filename, output_filename)
