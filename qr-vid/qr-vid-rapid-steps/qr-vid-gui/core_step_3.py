import json
import segno
import os

def main():
    # Maximum amount of data to put in a single QR code
    MAX_DATA_PER_QR = 256

    # Load the function.json file
    with open('function.json', 'r') as file:
        functions = json.load(file)

    # Create the qrs directory if it doesn't exist
    os.makedirs('qrs', exist_ok=True)

    # Loop through each entry in the functions
    for entry, function_code in functions.items():
        # Split the function code into chunks that fit into a QR code
        qr_data_chunks = [function_code[i:i+MAX_DATA_PER_QR] for i in range(0, len(function_code), MAX_DATA_PER_QR)]

        # Generate a QR code for each chunk
        for i, data_chunk in enumerate(qr_data_chunks):
            qr = segno.make(data_chunk)

            # Extract the entry number and zero pad it
            entry_num = int(entry.split('_')[1])  # Extract the number part from the entry (e.g., '1' from 'entry_1')
            padded_entry_num = str(entry_num).zfill(3)  # Zero pad the entry number (e.g., '1' becomes '001')

            # Save the QR code as a PNG file, adding a sequence number if there are multiple QR codes for this entry
            filename = f"qrs/entry_{padded_entry_num}_qr{i}.png"
            qr.save(filename, scale=10)

if __name__ == '__main__':
    main()