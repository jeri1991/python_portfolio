from datetime import datetime

names = ['Jonathan', 'Geovanni', 'Yessica', 'Kevin', 'Mario']
birthdays = ["1991-09-24", "1993-07-22", "1990-09-16","1997-08-17", "1993-04-24"]

print("Escribe la fecha de hoy en formato YYYY-MM-DD")
x = input()

for name in names:
    for birthday in birthdays:
        if datetime.strptime()