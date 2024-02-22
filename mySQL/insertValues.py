import pymysql
import os
from openpyxl import load_workbook
from dotenv import load_dotenv
def getAllRowsFromExcel(sheet):
    elements = []
    allRowsList = list(sheet.iter_rows(min_row=0, max_row=sheet.max_row))
    
    # add rows value to the elements, distinct: id, name, description, niveau
    for row in allRowsList:
        element = [cell.value for cell in row][:6]
        if (element[0]) : 
            elements.append([cell.value for cell in row][:4])
    return elements

# get the excel file data
input_path = "excel_file.xlsx"
excelFile = load_workbook(input_path, read_only=True)
workSheet = excelFile.active
elements = getAllRowsFromExcel(workSheet)


load_dotenv()
# Connect to the MySQL database
connection = pymysql.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    database=os.environ.get('MYSQL_DATABASE')
)
# Create a cursor object
cursor = connection.cursor()


for element in elements :
    id, name, descriptif, level = element
    # chapter
    if len(id) == 2 :
        # add chapter to the database without a parent id
        print(element)
    else :
        id1, id2, id3 = id.split('|')
        # if the second id is 0, add descriptif to the chapter not the article
        if (not int(id2)) :
            print(element)
        elif not int(id3) :
            # if the third id is 0, add article to the data base with descriptif if there .
            print("    ",element)
        else :
            # if the third id is not 0, add article to the data base with descriptif if there .
            print("         ", element)


# SQL query to insert data into a table
sql = "INSERT INTO lots (userID, lotName) VALUES (%s, %s)"

# Values to be inserted
values = ["GENIE CIVIL", "VRD", "ÉLECTRICITÉ", "SÉCURITÉ INCENDIE", "FLUIDE", "CONDITIONNEMENT"]

try:
    # Execute the SQL query
    for value in values :
        cursor.execute(sql, (1, value))

    # Commit changes
    connection.commit()
    print("Data inserted successfully!")



except mysql.connector.Error as error:
    # Rollback in case of an error
    print("Error inserting data:", error)
    connection.rollback()

# Close the cursor and connection
cursor.close()
connection.close()