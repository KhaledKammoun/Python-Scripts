import xml.dom.minidom

def collapse_xml(input_file, output_file):
    # Read the content of the XML file
    with open("books.xml", "r", encoding="utf-8") as file:

        lines = file.readlines()

    # Join the list of lines into a single string
    xml_content = ''.join(lines)
    print(lines)
    # Parse the input XML string
    dom = xml.dom.minidom.parseString(xml_content)

    # Get the XML content as a string with no indentation
    collapsed_xml = dom.toxml()
    
    # Write the collapsed XML to the output file
    with open(output_file, 'w') as file:
        file.write(collapsed_xml)
output_file = "books.xml"
collapse_xml("books.xml", output_file)