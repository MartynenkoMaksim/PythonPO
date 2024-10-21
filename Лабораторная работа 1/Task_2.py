
information_capacity_Megabyte = 1.44
pages_of_book = 100
lines_of_book = 50
symbols_in_line = 25
capacity_one_symbol = 4

information_capacity_one_book = 4 * pages_of_book * lines_of_book * symbols_in_line
information_capacity_byte = information_capacity_Megabyte * 1024 ** 2
quantity_of_books = information_capacity_byte // information_capacity_one_book

print("Количество книг, помещающихся на дискету:", int(quantity_of_books))
