class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_time(self, other): # Method definition takes self and other as arguments, must be defined inside class.
        """Adds two Time objects."""
        sum_time = Time() # Creating a new Time object to represent sum
        sum_time.hour = self.hour + other.hour
        sum_time.minute = self.minute + other.minute
        sum_time.second = self.second + other.second

        if sum_time.second >= 60:
            sum_time.second -= 60
            sum_time.minute += 1

        if sum_time.minute >= 60:
            sum_time.minute -= 60
            sum_time.hour += 1

        return sum_time
# Example Usage
time1 = Time(93, 55, 47)
time2 = Time(0, 34, 45)
sum_time = time1.add_time(time2)  # Call the method on a Time object
print(f"{sum_time.hour:02d}:{sum_time.minute:02d}:{sum_time.second:02d}")  # Output the result using f-string formatting