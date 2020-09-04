import pandas as pd
from openpyxl import load_workbook
from xlrd import sheet

data = pd.read_excel(r'C:\Users\User\Desktop\pyth1\week.xlsx')

df = pd.DataFrame(data, columns=['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata/Duminica'])

wb = load_workbook(filename='week.xlsx')
sheet_ranges = wb['Sheet2']

cell = (sheet_ranges.merged_cells.ranges)

cell = sheet.cell(row=1, column=4)
if type(cell).__name__ == 'MergedCell':
  print("Oh no, the cell is merged!")
else:
  print("This cell is not merged.")







df2=df



df2 = df2.style.set_properties(**{'font-weight': 'bold'})



# workbook = xlsxwriter.Workbook('week3.xlsx')


# bold = workbook.add_format({'bold': True})

df2.to_excel(r'C:\Users\User\Desktop\pyth1\week2.xlsx', index=False, header=True)

# workbook.close()
