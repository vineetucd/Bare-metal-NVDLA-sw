def process_weights(input_file, output_file):
    # Open input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Process each line in the input file
        for line in infile:
            # Extract the second column and remove '0x'
            data = line.split()[1][2:]
            # Write the modified data to the output file
            outfile.write(f"{data}\n")

# Input and output file names
input_file = 'all_addresses.dat'
output_file = 'mem_init.mem'

# Process the files
process_weights(input_file, output_file)

print(f"Processed data written to {output_file}")

