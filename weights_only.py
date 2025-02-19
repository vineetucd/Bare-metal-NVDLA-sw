def filter_addresses(input_file, output_file):
    # Define the address range in hexadecimal
    start_address = 0xc0016000
    end_address = 0xc001787c

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Extract address from each line (assuming address is the first element in the line)
            parts = line.split()
            if len(parts) > 0:
                try:
                    address = int(parts[0], 16)  # Convert address to integer (base 16)
                    # Write line only if address is outside the specified range
                    if not (start_address <= address <= end_address):
                        outfile.write(line)
                except ValueError:
                    # Write lines that do not start with a valid address
                    outfile.write(line)

# Input and output file paths
input_file = 'weights.dat'
output_file = 'weights_only.dat'

# Process the files
filter_addresses(input_file, output_file)

