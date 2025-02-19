# Define the address range
start_address = 0x0
end_address = 0x3c000

# Read the input file and store existing addresses with data values
address_data = {}

with open("sorted_addresses.dat", "r") as infile:
    for line in infile:
        parts = line.strip().split()  # Split line into address and data
        if len(parts) == 2:  # Ensure valid input
            address = int(parts[0], 16)  # Convert address to integer
            data = parts[1]  # Keep data as string
            address_data[address] = data  # Store in dictionary

# Write all addresses, filling missing ones with 0x00000000
with open("all_addresses.dat", "w") as outfile:
    for addr in range(start_address, end_address + 1):
        # If address is missing, use 0x00000000 as data
        data = address_data.get(addr, "0x00000000")
        outfile.write(f"{hex(addr)} {data}\n")

