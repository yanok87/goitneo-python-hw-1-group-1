'''This module contains a function that returns birthday reminder'''
from datetime import datetime
from collections import defaultdict


'''test_users = [
    {"name": "Bill Gates-sun", "birthday": datetime(1955, 2, 18)},
    {"name": "Bill Gates-mon", "birthday": datetime(1955, 2, 19)},
    {"name": "Yana", "birthday": datetime(1955, 2, 20)},
    {"name": "Andy", "birthday": datetime(1955, 2, 20)},
    {"name": "Mary", "birthday": datetime(1955, 2, 22)},
    {"name": "Tom", "birthday": datetime(1955, 2, 23)},
    {"name": "Fabi", "birthday": datetime(1955, 2, 23)},
    {"name": "Elison", "birthday": datetime(1955, 2, 25)},
    {"name": "Dan-sat", "birthday": datetime(1955, 2, 26)},
    {"name": "Dan-sun", "birthday": datetime(1955, 2, 27)},
]'''

def get_birthdays_per_week(users):
    '''This function returns birthday reminder'''
    res = defaultdict(list)
    today =  datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days

        if birthday_this_year.year == today.year:
            if delta_days < 7: # Birthday for the upcoming 7 days
                week_day = birthday_this_year.weekday()
                if week_day == 5 or week_day == 6: # Birthday on weekend
                    res["Monday"].append(name)
                if week_day < 5: # Birthday on week day
                    day_name = birthday_this_year.strftime('%A')
                    res[day_name].append(name)
    for day, names in res.items():
        names_str = ", ".join(names)
        formated = f"{day}: {names_str}"
        print(formated)


