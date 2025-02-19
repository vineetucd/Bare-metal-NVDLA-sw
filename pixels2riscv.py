def generate_riscv_program(input_file, output_file):
    try:
        # Open the input and output files
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Read each line of the input file
            for line in infile:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Split the line into address and data
                parts = line.split()
                addr = parts[0]  # First part is the address
                data = parts[1]  # Second part is the data

                # Write the RISC-V instructions to the output file with hex format
                outfile.write(f"li t0, {addr}     # Load address {addr}\n")
                outfile.write(f"li t1, {data}     # Load data {data}\n")
                outfile.write(f"sw t1, 0(t0)      # Store data at address {addr}\n\n")

            print(f"RISC-V program successfully written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file paths
input_file = 'image_n_addresses.dat'  # Input file containing the address and data pairs
output_file = 'im2riscv.s'  # Output file where the RISC-V program will be written

# Call the function to generate the RISC-V program
generate_riscv_program(input_file, output_file)

