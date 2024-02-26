#Q1)
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3

print(a)  # Print the final value of a

#Q2)
result = (3 + 10 ** 2 / 2) or 70.0
print(result)

#Q3)
import datetime

a = 3
b = 4
today = datetime.datetime(2024, 2, 26)  # February 26, 2024
day_of_week = today.weekday()  # Tuesday (0-indexed, so Tuesday is 1)
month_of_year = today.month  # February

a = a + day_of_week  # a = 3 + 1 = 4
b += month_of_year   # b = 4 + 2 = 6

print(a)  # 4
print(b)  # 6

c = a + b  # c = 4 + 6 = 10
print(c)  # 10

d = "abc" * (c//3)  # d = "abc" * (10//3) = "abc" * 3 = "abcabcabc"
print(d)  # "abcabcabc"


#Q4)
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Test each string
strings = [
    "7798338247658278460338648728567428338977",
    "0974101607733149676776769413377061014790",
    "2704702208931031198668911301398022074072",
    "4257304920394478392772938744930294037524"
]

for string in strings:
    print(f"{string}: {palindrome(string)}")

#Q5)
def count_bob_occurrences(text):
    count = 0
    i = 0
    while i < len(text):
        # Check if the current character is 'b' and there are at least 3 characters left
        if text[i] == 'b' and i + 3 <= len(text):
            # Check if the next three characters form the pattern 'Bob'
            if text[i+1:i+4] == 'Bob':
                count += 1
                i += 3  # Skip 'Bob' to avoid counting overlapping occurrences
            else:
                i += 1  # Move to the next character
        else:
            i += 1  # Move to the next character
    return count

# Test the function
text = "Bob is a good boy and Bobby is his friend. They both love Bob!"
print("Number of occurrences:", count_bob_occurrences(text))


#Q6)
#mutable
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Modify the second element of the list
my_list[1] = 10
print("Modified List:", my_list)
#inmutable
my_string = "Hello"
print("Original String:", my_string)

# Attempt to modify the second character of the string
try:
    my_string[1] = 'a'
except TypeError as e:
    print("Error:", e)

#Q7)
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# Replace numbers greater than 80 with their corresponding negative value
for i in range(len(random_numbers)):
  if random_numbers[i] > 80:
    random_numbers[i] = -random_numbers[i]

# Print the updated list
print(random_numbers)

#Q8)

#Q9)
def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Calculate today's date
    current_day = 26  # Assume today is the 26th
    current_month = 2  # Assume today is February
    current_year = 2024  # Assume today is 2024

    # Calculate the number of whole years between birth year and current year
    years_passed = current_year - year - 1

    # Calculate the number of days passed excluding birth year and current year
    days_passed = years_passed * 365

    # Add leap years occurred between the birth year and current year
    leap_years = 0
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            leap_years += 1

    # Add leap years' days to the total days passed
    days_passed += leap_years

    # Subtract the days passed in the birth year
    if month < 2 or (month == 2 and day < 26):
        # If birthday has passed in the birth year, exclude the days from the birth year
        days_passed -= 365 - ((31 * (month - 1) + day) + 1)

    return days_passed

birthday = "24-02-2004"
print("Days since your birthday:", days_since_birthday(birthday))


