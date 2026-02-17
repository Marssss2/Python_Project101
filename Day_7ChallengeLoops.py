files =['report.csv','data.xlsx','summary.docx','report.docx','data.cvs']

for file in files:
    if file.startswith('report'):
        print('Duplicate Found!')
        break
else:
    print('All Files are Unique!')