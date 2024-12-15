# Duplicate-Frequency-Analyzer

This script processes a CSV file containing numeric values, identifies duplicates, and writes the duplicates along with their frequencies to an output CSV file.

Features
Reads input data from a CSV file where each row contains a single integer.
Counts the frequency of each unique number.
Filters out numbers that occur only once (ignores non-duplicates).
Sorts the duplicate numbers by their frequency in descending order.
Outputs the results (number and its count) to a new CSV file.
Requirements
Python 3.x
Usage
Run the script with the following command:

bash
Copy code
python pa4.py input_filename output_filename
Parameters:
input_filename: The name of the input CSV file (should contain one integer per row).
output_filename: The name of the output CSV file where duplicate numbers and their counts will be stored.
Example Command:
bash
Copy code
python pa4.py numbers.csv duplicates.csv
Input File Format
The input file should be a CSV where each row contains a single integer. For example:

Copy code
5
3
5
7
3
7
7
Output File Format
The output file will be a CSV where each row contains a number and its count, sorted by count in descending order. For example, given the input above, the output would look like this:

Copy code
7,3
5,2
3,2
Script Breakdown
Functions
process_input(input_filename, output_filename)
This function performs the main operations:

Reads the input file and counts the occurrences of each number.
Sorts the counts in descending order based on frequency.
Filters out numbers with a count of 1, as they are not duplicates.
Writes the results (number and count) to the output file.
Execution Flow
The script checks for correct usage (exactly 2 command-line arguments).
If the arguments are valid, it calls process_input() to process the input and generate the output.
Error Handling
The script will exit with an error message if the incorrect number of arguments is provided.
