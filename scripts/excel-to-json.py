import pandas as pd
import xlrd
import openpyxl
from time import time

start_time = time()

df_territoriales2011_ingresos = pd.read_excel('procesos-electorales/2011/Territoriales_2011.xlsx',sheet_name=['Ingresos'])
print(df_territoriales2011_ingresos.shape)

elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)

# ['Ingresos', 'Gastos', 'Gastos208']


#wb = openpyxl.load_workbook("procesos-electorales/2011/Territoriales_2011.xlsx")
#print(wb.sheetnames)