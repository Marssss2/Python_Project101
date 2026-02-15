files = ['report.csv', 'DATA.csv', 'summary.txt', 'image.png', 'notes.docx']
for file in files:
    if file.strip().lower().endswith(('.csv', '.txt')):
        print(f"Processing {file}...")
        # Add code to process the CSV file here
    else:
        print(f"Skipping {file} as it is not a CSV or TXT file.")