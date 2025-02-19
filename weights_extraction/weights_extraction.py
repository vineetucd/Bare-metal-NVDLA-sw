# Open the original log file and extract relevant data
with open('sc.log', 'r') as infile, open('weights_only.dat', 'w') as outfile:
    # Define the address range in hexadecimal
    start_address = 0xc0016000
    end_address = 0xc001787c

    # Iterate through each line in the input file
    for line in infile:
        # Process lines containing 'nvdla.dbb_adaptor' and 'iswrite=0'
        if 'nvdla.dbb_adaptor' in line and 'iswrite=0' in line:
            try:
                # Extract addr and data values
                addr_start = line.find("addr=") + len("addr=")
                addr_end = line.find(" ", addr_start)
                addr = int(line[addr_start:addr_end], 16)

                # Find the data values
                data_start = line.find("data=0x") + len("data=0x")
                data_values = line[data_start:].split()[:2]  # Extract two words of data

                if len(data_values) == 2:
                    # Write data only if address is outside the specified range
                    if not (start_address <= addr <= end_address):
                        outfile.write(f"{hex(addr)} 0x{data_values[0]}\n")
                    if not (start_address <= addr + 4 <= end_address):
                        outfile.write(f"{hex(addr + 4)} 0x{data_values[1]}\n")
            except ValueError:
                # Skip lines that don't match expected format
                continue

print("Processing complete. Output written to weights_only.dat.")
