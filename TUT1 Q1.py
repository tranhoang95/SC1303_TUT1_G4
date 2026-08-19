def convert_time(total_seconds):
    hours = total_seconds // 3600
    seconds = total_seconds % 60
    minutes = int((total_seconds - (hours * 3600) - seconds) / 60)
    return hours, minutes, seconds


def decimal_to_any_base(number, base):
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        digits.append(number % base)
        number = number // base
    return digits[::-1]


# READ INPUT
total_seconds = int(input("Enter the number of seconds: "))

while not (1 <= total_seconds <= 86400):
    total_seconds = int(input("The number of seconds must be between 1 and 86400\nPlease re-enter the number of seconds: "))

# Approach 1
hours1, minutes1, seconds1 = convert_time(total_seconds)

print(total_seconds, "is", hours1, "hours,", minutes1, "minutes, and", seconds1, "seconds.")


# Approach 2
base60_digits = decimal_to_any_base(total_seconds, 60)
hours2, minutes2, seconds2 = ([0, 0] + base60_digits)[-3:]

print(total_seconds, "is", hours2, "hours,", minutes2, "minutes, and", seconds2, "seconds.")