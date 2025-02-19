# Read input file and store data in a list
with open("divide_by_4.dat", "r") as infile:
    lines = []
    for line in infile:
        parts = line.strip().split()  # Split each line into two columns
        if len(parts) == 2:  # Ensure valid input
            address = int(parts[0], 16)  # Convert address to integer for sorting
            data = parts[1]  # Keep data as string
            lines.append((address, data))  # Store as tuple (address, data)

# Sort the list based on the address (first element of tuple)
lines.sort(key=lambda x: x[0])

# Write sorted data to output file
with open("sorted_addresses.dat", "w") as outfile:
    for address, data in lines:
        outfile.write(f"{hex(address)} {data}\n")  # Convert address back to hex format

