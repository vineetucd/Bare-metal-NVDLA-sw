import struct

def store_64bit_data_to_memory(file_path, output_file):
    # Starting memory address
    memory_start_address = 0x00216000

    # Read the input file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize memory as a dictionary to simulate address-value mapping
    memory = {}

    # Address offset
    offset = 0

    for line in lines:
        # Remove whitespace and ensure valid input
        line = line.strip()
        if len(line) != 16:
            print(f"Skipping invalid line: {line}")
            continue

        # Parse 64-bit hex string into lower and upper 32-bit integers
        full_64_bit = int(line, 16)
        lower_32 = full_64_bit & 0xFFFFFFFF
        upper_32 = (full_64_bit >> 32) & 0xFFFFFFFF

        # Store values in simulated memory
        memory[memory_start_address + offset] = lower_32
        memory[memory_start_address + offset + 4] = upper_32

        # Move to the next pair of addresses
        offset += 8

    # Write memory contents to output file
    with open(output_file, 'w') as out_file:
        for address in sorted(memory.keys()):
            out_file.write(f"0x{address:08X} 0x{memory[address]:08X}\n")

    return memory

# Call the function with the provided input and output files
input_file = 'image2array.dat'
output_file = 'image_n_addresses.dat'
memory_contents = store_64bit_data_to_memory(input_file, output_file)

