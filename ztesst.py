from datetime import datetime as date


participant_list = [
    ('Lê An', "15/10/2021", 18),
    ('Trần Bình', "20/10/2021", 12),
    ('Trần Tâm', "06/08/2021", 20),
    ('Thanh Lam', "30/10/2020", 22),
    ('Vũ Lan', "05/11/2019", 12)
]
format = '%d/%m/%Y'
# datetime.strptime(date_string, format)
sorted_list = sorted(participant_list, key=lambda item: (date.strptime(item[1], format), item[2]), reverse=True)
print(sorted_list)