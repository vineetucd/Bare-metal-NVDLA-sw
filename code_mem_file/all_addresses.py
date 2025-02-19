# File paths
input_file = 'machine_code_5_lenet.txt'
output_file = 'all_addresses.txt'

# Define the address range
start_address = 0x0
end_address = 0x00007fff

# Read the input file and extract existing addresses
def parse_address(line):
    try:
        start = line.find("32'h") + 4
        end = line.find("]")
        return int(line[start:end], 16)
    except (ValueError, IndexError):
        return None

existing_data = {}
with open(input_file, 'r') as infile:
    for line in infile:
        address = parse_address(line)
        if address is not None:
            existing_data[address] = line.strip()

# Generate all addresses and add missing ones with zero values
with open(output_file, 'w') as outfile:
    for address in range(start_address, end_address + 1):
        if address in existing_data:
            outfile.write(existing_data[address] + '\n')
        else:
            outfile.write(f"RAM[32'h{address:08X}] = 32'h00000000;\n")

