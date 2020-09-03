import pandas as pd
from pandas.tests.io.excel.test_xlsxwriter import xlsxwriter

data = pd.read_excel(r'C:\Users\User\Desktop\pyth1\week.xlsx')

df = pd.DataFrame(data, columns=['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata/Duminica'])

df.to_excel(r'C:\Users\User\Desktop\pyth1\week2.xlsx', index = False, header=True)


workbook = xlsxwriter.Workbook('week2.xlsx')

bold = workbook.add_format({'bold': True})

workbook.close()

'''
worksheet.write(0, 0, 'Hello Excel')

workbook.close()

'''

