# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, n_=','):
    first = set(first_group.split(n_))
    second = set(second_group.split(n_))
    common_members = first.intersection(second)

    list_common_memebers = list(common_members)
    list_common_memebers.sort()

    return list_common_memebers

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", participants)