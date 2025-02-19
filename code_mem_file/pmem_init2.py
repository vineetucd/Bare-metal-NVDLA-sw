# Define the input and output file paths
input_file = 'pmem_init.mem'
output_file = 'pmem_init_digit5_lenet.mem'

# Open the input file and read the lines
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Open the output file and write the modified lines
with open(output_file, 'w') as outfile:
    for line in lines:
        # Remove the '32'h' prefix and strip any extra whitespace
        modified_line = line.strip().replace("32'h", "")
        outfile.write(modified_line + '\n')

print(f"Processed file saved as {output_file}")

