# Open the original log file and the new file for output
with open('sc.log', 'r') as infile:
    # Open the output file in write mode
    with open('csb_lines.log', 'w') as outfile:
        # Iterate through each line in the input file
        for line in infile:
            # Check if the line contains 'nvdla.dbb_adaptor'
            if 'nvdla.csb_adaptor' in line:
                # Write the matching line to the output file
                outfile.write(line)

