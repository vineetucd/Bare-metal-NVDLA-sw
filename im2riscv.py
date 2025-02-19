from PIL import Image
import numpy as np

def generate_riscv_from_image(image_path, output_file):
    # Open the image in grayscale mode ('L' mode)
    image = Image.open(image_path).convert('L')

    # Convert the image to a NumPy array (grayscale values between 0 and 255)
    pixel_values = np.array(image)

    # Starting memory address
    memory_start_address = 0x00216000

    # Open the output file to write RISC-V assembly code
    with open(output_file, 'w') as outfile:
        offset = 0

        # Process each pixel, row by row
        for row in pixel_values:
            for pixel in row:
                # Divide the pixel value by 2
                pixel = pixel // 2

                # Convert pixel to a 64-bit hexadecimal value
                hex_str = format(pixel, '016x')

                # Parse 64-bit hex string into lower and upper 32-bit integers
                full_64_bit = int(hex_str, 16)
                lower_32 = full_64_bit & 0xFFFFFFFF
                upper_32 = (full_64_bit >> 32) & 0xFFFFFFFF

                # Calculate the current address
                addr_lower = memory_start_address + offset
                addr_upper = addr_lower + 4

                # Write the RISC-V instructions to the output file
                outfile.write(f"li t0, 0x{addr_lower:08X}     # Load address 0x{addr_lower:08X}\n")
                outfile.write(f"li t1, 0x{lower_32:08X}     # Load lower 32-bit data\n")
                outfile.write(f"sw t1, 0(t0)                # Store lower 32-bit data\n\n")

                outfile.write(f"li t0, 0x{addr_upper:08X}     # Load address 0x{addr_upper:08X}\n")
                outfile.write(f"li t1, 0x{upper_32:08X}     # Load upper 32-bit data\n")
                outfile.write(f"sw t1, 0(t0)                # Store upper 32-bit data\n\n")

                # Move to the next pair of addresses
                offset += 8

    print(f"RISC-V program successfully written to {output_file}")

# Input image and output RISC-V file paths
image_path = '125_5.jpg'
output_file = 'im2riscv.s'

generate_riscv_from_image(image_path, output_file)

