# Open input and output files
with open("weights_only_modified.dat", "r") as infile, open("divide_by_4.dat", "w") as outfile:
    # Process each line in the input file
    for line in infile:
        parts = line.strip().split()  # Split line into columns
        if len(parts) != 2:  # Skip lines that don't have exactly two columns
            continue
        
        # Extract columns
        first_col, second_col = parts[0], parts[1]

        # Convert the first column from hexadecimal to integer, divide by 4, and convert back to hexadecimal
        first_col_div4 = hex(int(first_col, 16) // 4)

        # Write the modified line to the output file
        outfile.write(f"{first_col_div4} {second_col}\n")

