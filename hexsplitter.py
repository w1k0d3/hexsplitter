import sys


def divide_hex_range(start_hex, end_hex, num_parts, output_file):
    # Convert hex to decimal
    start = int(start_hex, 16)
    end = int(end_hex, 16)

    # Calculate the total range and each part size
    total_range = end - start
    part_size = total_range // num_parts

    # Generate the parts
    hex_parts = [hex(start + i * part_size) for i in range(num_parts)]

    # Save to output file
    with open(output_file, 'w') as f:
        for i, part in enumerate(hex_parts):
            f.write(f"Part {i + 1}: {part}\n")

    print(f"Divided the range from {start_hex} to {end_hex} into {num_parts} parts and saved to {output_file}.")

# Example usage
if __name__ == "__main__":
    start_hex = "0x4000000000000000"
    end_hex = "0x7FFFFFFFFFFFFFFF"
    num_parts = 100000
    output_file = "hex_parts100000.txt"

    divide_hex_range(start_hex, end_hex, num_parts, output_file)
