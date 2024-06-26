import pdfplumber
import pandas as pd 

pdf = pdfplumber.open(r"./meds.pdf")
f = open('meds.csv', 'w')


def read_pdf(pdf):
    text = []
    for page in pdf.pages:
        table = page.extract_table()
        # print(table)
        print(f'table length: {len(table)}')
        if table:
            f.write("med_name\n")
            for row in table:
                if row[0].isnumeric():
                    f.write(row[1].replace('\n', ' ') + "\n")
        
    
read_pdf(pdf)
f.close()