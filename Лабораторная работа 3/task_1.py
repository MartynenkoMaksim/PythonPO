# TODO Напишите функцию для поиска индекса товара
def search_index(list_all_items, item):
    if item in list_all_items:
        index_ = list_all_items.index(item)
        return index_


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
