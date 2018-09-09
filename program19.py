days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
curday=input("Enter Day")
curday=curday.capitalize()
day=int(input("Enter time to add"))
print(days[(days.index(curday)+day)%7])