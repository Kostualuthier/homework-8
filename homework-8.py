from datetime import datetime, timedelta


users = [{"name": "Kolya", "birthday": datetime(year=1976, month=9, day=23)},
        {"name": "Tanya", "birthday": datetime(year=1993, month=9, day=24)},
        {"name": "Katya", "birthday": datetime(year=1992, month=9, day=25)},
        {"name": "Serhiy", "birthday": datetime(year=1991, month=9, day=26)},
        {"name": "Sasha", "birthday": datetime(year=1994, month=9, day=27)},
        {"name": "Nastya", "birthday": datetime(year=1983, month=9, day=28)},
        {"name": "Vasya", "birthday": datetime(year=1986, month=9, day=29)},
        {"name": "Pasha", "birthday": datetime(year=1986, month=9, day=30)},
        {"name": "Olia", "birthday": datetime(year=1990, month=10, day=1)},
        {"name": "Ivan", "birthday": datetime(year=1995, month=10, day=2)},
        {"name": "Oleksiy", "birthday": datetime(year=1995, month=10, day=3)}]


def get_birthdays_per_week(some_list):
    current_date = datetime.now()
    monday = current_date + timedelta(7 - current_date.weekday())
    workdays = [monday]
    for i in range(1, 5):
        workdays.append(monday + timedelta(days=i))

    weekends = [monday - timedelta(days=1), monday - timedelta(days=2)]

    mon = ['Monday']
    tue = ['Tuesday']
    wed = ['Wednesday']
    thu = ['Thursday']
    fri = ['Friday']

    for user in users:
        if user["birthday"].month == workdays[0].month and user["birthday"].day == workdays[0].day:
            mon.append(user["name"])
        elif user["birthday"].month == workdays[1].month and user["birthday"].day == workdays[1].day:
            tue.append(user["name"])
        elif user["birthday"].month == workdays[2].month and user["birthday"].day == workdays[2].day:
            wed.append(user["name"])
        elif user["birthday"].month == workdays[3].month and user["birthday"].day == workdays[3].day:
            thu.append(user["name"])
        elif user["birthday"].month == workdays[4].month and user["birthday"].day == workdays[4].day:
            fri.append(user["name"])
        elif user["birthday"].month == weekends[0].month and user["birthday"].day == weekends[0].day:
            mon.append(user["name"])
        elif user["birthday"].month == weekends[1].month and user["birthday"].day == weekends[1].day:
            mon.append(user["name"])

    birthdays_list = [mon, tue, wed, thu, fri]

    for day in birthdays_list:
        if len(day) > 1:
            print(day[0], end=': ')
            print(', '.join(day[1:]))

if __name__ == "__main__":
    get_birthdays_per_week(users)
