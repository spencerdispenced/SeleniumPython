

from xlrd import open_workbook
import xlwt

# Open Excel file
wb = open_workbook("..\Data\params2.xls")

# Get sheet by sheet name
sheet = wb.sheet_by_name("Sheet1")

# Print number of sheets
print(wb.nsheets)

# Print number of rows and cols
print(sheet.nrows)
print(sheet.ncols)

# Printt value from sheet (Row, Col), zero indexed
print(sheet.cell_value(2, 0))

# Create a new workbook
wb1 = xlwt.Workbook()

# Add a new sheet
sh1 = wb1.add_sheet("Names", cell_overwrite_ok=True)

# Write values to sheet
sh1.write(1, 1, "First Name")
sh1.write(1, 2, "Last Name")

# Save the file, using path
wb1.save("..\Data\demo1.xls")
