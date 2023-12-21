from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

import os
import xlwings as xw
import subprocess
def open_file(filePath) :
    try:
        subprocess.Popen(['start', 'excel', filePath], shell=True)
    except Exception as e:
        print(f"An error occurred: {e}")

def close_file(filePath) :
    try:
        book = xw.Book(filePath)
        book.close()
    except Exception as e:
        print(e)


def excelSheet_modulation(sheet) :

     # Convert the generator to a list for reversing
    rows_to_delete = list(sheet.iter_rows(min_row=1, max_row=sheet.max_row))
    
    
    # Delete empty rows
    for row in reversed(rows_to_delete):
        if all(cell.value is None for cell in row):
            sheet.delete_rows(row[0].row, amount=1)

    # Convert the generator to a list for reversing
    cols_to_delete = list(sheet.iter_cols(min_col=1, max_col=sheet.max_column))
    
    # Delete empty columns
    for col in reversed(cols_to_delete):
        if all(cell.value is None for cell in col):
            sheet.delete_cols(col[0].col_idx, amount=1)
    
    return sheet
# close_file('FamilyExcel.xlsx')
excelFile = load_workbook('FamilyExcel.xlsx')
workSheet = excelFile.active
# workSheet = excelSheet_modulation(workSheet)

class ExcelElementsClass :
    def __init__(self, id, name, description, niveau) :
        self.id = id
        self.name = name
        self.description = description
        self.niveau = niveau
    @staticmethod
    def getAllRowsFromExcel(file) :
        elements = []
        allRowsList = list(workSheet.iter_rows(min_row = 2, max_row = workSheet.max_row))
        if all(len(row) == 4 for row in allRowsList) :
            # add rows value to the elements, distinct : id, name, description, niveau
            for row in allRowsList:
                elements.append(ExcelElementsClass(*[cell.value for cell in row]))
 
        else :
            print("You have an Error, check Nb Columns and Rows")
        return elements

class TreeNode:
    def __init__(self, data):
        self.data = data # data = the excel row
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# contain all the excel rows with distinct value according to ('id', 'name', 'description', 'Niveau')
elements = ExcelElementsClass.getAllRowsFromExcel('FamilyExcel.xlsx')  

# Create a Tree
root = TreeNode(ExcelElementsClass('0', "Root",None, 0))


excelFile.save('FamilyExcel.xlsx')
# open_file('FamilyExcel.xlsx')