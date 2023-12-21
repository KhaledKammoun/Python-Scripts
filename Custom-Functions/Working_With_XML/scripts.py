import lxml.etree as etree
tree = etree.parse('books.xml')
root = tree.getroot()

var_books = root.findall('book')
class Book :
    def __init__(self,id, author, title, genre, price, publish_date, description) :
        self.id = id
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.publish_date = publish_date
        self.description = description
    
    @staticmethod
    def CreateNewBook(auth, tit, gen, pri, publish_da, descripti) :
        new_book = etree.Element("book")
        
        author = etree.Element("author")
        author.text = auth
        new_book.append(author)


        title = etree.Element("title")
        title.text = tit
        new_book.append(title)

        genre = etree.Element("genre")
        genre.text = gen
        new_book.append(genre)

        price = etree.Element("price")
        price.text = pri
        new_book.append(price)

        publish_date = etree.Element("publish_date")
        publish_date.text = publish_da
        new_book.append(publish_date)

        description = etree.Element("description")
        description.text = descripti
        new_book.append(description)

        return new_book
allBooks = []

for book in var_books:
    attributes = {'id': "NoID"}  # Default id value
    if 'id' in book.attrib:
        attributes['id'] = book.attrib['id']

    for child_node in book:
        if child_node.tag:
            attribute_name = child_node.tag #tag = tagName
            attribute_value = child_node.text
            attributes[attribute_name] = attribute_value

    book_var = Book(**attributes)
    allBooks.append(book_var)
for book in allBooks :
    print("------ Book ID : {} ------".format(book.id))
    for attribute, value in list(book.__dict__.items())[1:] :
        print("** {} : {} **".format(attribute, value))

new_book = Book.CreateNewBook("Khaled", "Anne With an E", "Drama", "12.2", "2001-01-01", "A good Book")

# root.remove(root[-1])  # Removes the last child of 'roote'
root.append(new_book)
tree.write("books.xml", pretty_print=True, encoding="utf-8")