from openpyxl import Workbook
import lxml.etree as etree


def return_row(item, niveau) :
    if (len(item.find("ID").text) == 8) or niveau == 3 :
        id_value = item.find("ID").text
    elif niveau == 1:
        if len(item.find("ID").text) == 2 :
            id_value = "{}|00|00".format(item.find("ID").text)
        elif len(item.find("ID").text) == 1 :
            id_value = "0{}|00|00".format(item.find("ID").text)
    elif niveau == 2 or len(item.find("ID").text) == 5:
        id_value = "{}|00".format(item.find("ID").text)

    name_value = item.find("Name").text if item.find("Name") is not None else ""

    description = item.find("Description").text

    try :
        return [id_value, name_value, description, niveau]
    except :
        return []
def convert_xml_to_excel(input_file, output = "", output_file_name = "new_file") :
    # XML File
    tree = etree.parse(input_file)
    
    xpath_expression = "/BuildingInformation/Classification/System/Items/Item"
    items = tree.xpath(xpath_expression)

    # Create new Excel File
    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Name", "Description", "Niveau"])

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
    if (len(output_file_name) >= 5 and output_file_name[-5:] != ".xlsx") :
        wb.save("{}.xlsx".format(output_file_name))
    else :
        wb.save(output_file_name)

convert_xml_to_excel("your xml file ...")