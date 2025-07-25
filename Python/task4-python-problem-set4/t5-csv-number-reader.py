import csv
import math

def process_numbers():
    try:
        with open("numbers.csv", "r") as infile, open("sqrt_results.csv", "w", newline="") as outfile:
            reader = csv.reader(infile)
            next(reader) 

            writer = csv.writer(outfile)
            writer.writerow(["Number", "SquareRoot"])

            for row in reader:
                try:
                    num = float(row[0])
                    if num < 0:
                        print(f"Skipping invalid or negative entry: {row[0]}")
                    else:
                        result = math.sqrt(num)
                        print(f"Square root of {int(num)} is {result}")
                        writer.writerow([int(num), result])
                except:
                    print(f"Skipping invalid or non-numeric entry: {row[0]}")

        return "Task completed."

    except:
        return "Error with file handling."

result = process_numbers()
print(result)