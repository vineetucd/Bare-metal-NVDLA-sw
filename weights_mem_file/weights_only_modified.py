# Open input and output files
with open("weights_only.dat", "r") as infile, open("weights_only_modified.dat", "w") as outfile:
    # Process each line in the input file
    for line in infile:
        parts = line.strip().split()  # Split line into columns
        if len(parts) != 2:  # Skip lines that don't have exactly two columns
            continue
        
        # Extract columns
        first_col, second_col = parts[0], parts[1]

        # Check and replace based on the condition
        if first_col.startswith("0xc01"):
            first_col = "0x000" + first_col[5:]
        elif first_col.startswith("0xc000"):
            first_col = "0x0005" + first_col[6:]

        # Write the modified line to output
        outfile.write(f"{first_col} {second_col}\n")

