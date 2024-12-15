#Christian Bae
import csv
import sys

def process_input(input_filename, output_filename):
    counts = {}
    with open(input_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            number = int(row[0])
            counts[number] = counts.get(number, 0) + 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    filtered_counts = [(num, count) for num, count in sorted_counts if count > 1]

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        if filtered_counts:
            for num, count in filtered_counts:
                writer.writerow([num, count])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pa4.py input_filename output_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    process_input(input_filename, output_filename)
