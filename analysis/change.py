import csv

input_path = "./analysis/TMSE_detailed.csv"
output_path = "./analysis/TMSE_detailed_change.csv"

group_mapping = {
    "1": "5",
    "2": "6",
    "3": "7",
    "4": "2",
    "5": "3",
    "6": "4",
    "7": "1",
    
}

with open(input_path, newline="", encoding="utf-8") as infile, \
     open(output_path, mode="w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header
    header = next(reader)
    writer.writerow(header)

    for row in reader:
        if row and row[0] in group_mapping:
            row[0] = group_mapping[row[0]]
        writer.writerow(row)

print(" mapping completed. Output saved to:", output_path)
