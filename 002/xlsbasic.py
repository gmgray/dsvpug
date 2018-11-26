from datetime import datetime
import xlwt
import random

# define some styles

styleBold = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',num_format_str='#,##0.00')
styleDateTime = xlwt.easyxf(num_format_str='DD-MM-YYYY H:m:S')

# create workbook
wb=xlwt.Workbook()
# add worksheet to workbook
ws=wb.add_sheet('Python data')

# fill out some cells
ws.write(0,0,1234.56,styleBold)
ws.write(1,0, datetime.now(),styleDateTime)
# add more cells
for i in range(2,12):
    for j in range(1,5):
        ws.write(i,j,random.randint(1,10000))
# add formula
ws.write(13,5,xlwt.Formula("SUM(C2:C12)"))
wb.save('output.xls')