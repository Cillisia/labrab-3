def find_common_participants(s1,s2,sep=','):
    common_participants = []
    for lastname1 in s1.split(sep):
        for lastname2 in s2.split(sep):
            if lastname1==lastname2:
                common_participants.append(lastname1)
                break
    return sorted(common_participants)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,'|'))
