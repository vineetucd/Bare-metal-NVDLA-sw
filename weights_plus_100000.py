def update_addresses(input_file, output_file, increment):
    try:
        # Open the input file for reading and the output file for writing
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Read each line of the input file
            for line in infile:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Split the line into address and data
                parts = line.split()
                addr = parts[0]  # Address is the first part
                data = parts[1]  # Data is the second part

                # Convert the address to an integer, add the increment, and convert it back to hex
                addr_int = int(addr, 16)  # Convert address to integer
                updated_addr_int = addr_int + increment  # Add the increment
                updated_addr = hex(updated_addr_int)  # Convert back to hex

                # Write the updated address and the original data to the output file
                outfile.write(f"{updated_addr} {data}\n")

            print(f"Updated addresses written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Input and output file paths
input_file = 'weights_only.dat'  # Input file containing the address and data pairs
output_file = 'weights_only_plus_100000.dat'  # Output file to store updated addresses

# Increment value (0x00100000)
increment = 0x00100000

# Call the function to update the addresses
update_addresses(input_file, output_file, increment)

