#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlrd

file = "data.xls"

class ExcelReader:
    def __init__(self, filename):
        self.filename = filename
        self.wb = xlrd.open_workbook(self.filename)
        self.sh0 = self.wb.sheet_by_index(0)    
    def read_first_row(self):
        first_row = []
        for i in range(self.sh0.ncols):
            first_row.append(self.sh0.cell_value(0, i))
        return first_row
    def read_last_column(self):
        last_column = []
        for i in range(self.sh0.nrows):
            last_column.append(self.sh0.cell_value(i, self.sh0.ncols-1))
        return last_column 
    def read_excel(self):
        data = {}
        keys = self.read_first_row()
        for i in range(self.sh0.ncols):
            for j in range(1, self.sh0.nrows):
                data.setdefault(keys[i], [])
                data[keys[i]].append(self.sh0.cell_value(j, i))
        return data  
    def read_row(self, row_number):
        row = []
        for i in range(self.sh0.ncols):
            row.append(self.sh0.cell_value(row_number, i))
        return row 
    def read_column(self, col_number):
        col = []
        for i in range(self.sh0.nrows):
            col.append(self.sh0.cell_value(i, col_number))
        return col
    def read_excel2(self):
        data = {}
        keys = self.read_first_row()
        for i in range(self.sh0.ncols):
            data[keys[i]] = self.read_column(i)[1:]
        return data  


# In[ ]:




