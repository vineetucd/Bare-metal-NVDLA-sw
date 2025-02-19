# File paths
input_file = 'all_addresses.txt'
output_file = 'pmem_init.mem'

# Open the input file and process each line
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Extract data values
data_values = []
for line in lines:
    try:
        data_value = line.split('=')[1].strip().rstrip(';')  # Extract the part after '=' and remove ';'
        data_values.append(data_value)
    except IndexError:
        continue  # Skip lines that do not match the format

# Write the data values to the output file
with open(output_file, 'w') as outfile:
    outfile.write('\n'.join(data_values) + '\n')

