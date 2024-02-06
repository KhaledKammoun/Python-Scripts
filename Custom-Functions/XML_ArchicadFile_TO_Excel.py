from openpyxl import Workbook
import lxml.etree as etree

# XML File
tree = etree.parse("classification.xml")
xpath_expression = "/BuildingInformation/Classification/System/Items/Item"
items = tree.xpath(xpath_expression)


# Create new Excel File
wb = Workbook()
ws = wb.active
ws.append(["ID", "Name", "Description", "Niveau"])

def return_row(item, niveau) :
    id_value = item.find("ID").text

    name_value = item.find("Name").text if not item.find("Name") else ""

    description = item.find("Description").text

    return [id_value, name_value, description, niveau]

for item in items :
    ws.append(return_row(item, 1))
    children = item.find("Children")
    if children is not None:
        for item_child_1 in children.findall("Item") :
            ws.append(return_row(item_child_1, 2))
            children_1 = item_child_1.find("Children")
            if children_1 is not None:
                for item_child_2 in children_1.findall("Item") :
                    ws.append(return_row(item_child_2, 3))
                    children_2 = item_child_2.find("Children")
                    if children_2 is not None:
                        for item_child_3 in children_2.findall("Item") :
                            ws.append(return_row(item_child_3, 4))
                            children_3 = item_child_3.find("Children")
                            if children_3 is not None:
                                for item_child_4 in children_3.findall("Item") :
                                    ws.append(return_row(item_child_4, 5))

wb.save("Classification.xlsx")