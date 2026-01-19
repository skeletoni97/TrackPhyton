# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, n = ','):
    group1 = participants_first_group.split(n)
    group2 = participants_second_group.split(n)
    common_participants = sorted(set(group1) & set(group2))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
