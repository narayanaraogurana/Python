#program for day check
day=int(input("enter day number"))
match(day):
    case 1|2|3|4|5:
        print("weekday")
    case 6|7:
        print("weekend")
    case _:
        print("enter proper day number")