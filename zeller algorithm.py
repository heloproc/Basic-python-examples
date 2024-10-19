def zeller():
    a = int(input("Enter month (March=1, April=2, ..., Jan=11, Feb=12): "))
    b = int(input("Enter date: "))
    c = int(input("Enter year of century (e.g., 89 for 1989): "))
    d = int(input("Enter century (e.g., 19 for 1989): "))

    if a == 11 or a == 12:  # Correctly adjust for January and February
        c -= 1
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7  # Day of the week (0=Sunday, 1=Monday, ..., 6=Saturday)

    return r

if __name__ == "__main__":
    day_of_week = zeller()
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(days[day_of_week]) # Prints the day's name