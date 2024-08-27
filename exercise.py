def banner(num):
    print('')
    print('--------------------------------')
    print(f'---------- Excercise {num} ---------')
    print('--------------------------------')
    print('')

# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

banner(0)
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

banner(1)
def check_letter():
   vowels = ['a', 'e', 'i', 'o', 'u']
   alphabets = ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   userInput = input('Enter a letter :').lower()
   print(userInput)
   if (userInput in alphabets):
       if (userInput in vowels):
           print(f'The letter {userInput} is a vowel')
       else:
           print(f'The letter {userInput} is a constant')
   else:
       print(f'The {userInput} is a non-alphabetical or invalid entry')


# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

banner(2)
def check_voting_eligibility():
    age = input("Please enter your age: ")
    if(int(age) < 0):
        print('no negative numbers')
    elif(int(age) >= 21):
        print('eligible to vote')
    elif(int(age) < 21):
        print('not eligible to vote')
    else:
        print('Invalid input')

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

banner(3)
def calculate_dog_years():
    dogAge = int(input("Input a dog's age: "))
    if(dogAge < 0):
        print(f'{dogAge} is not valid input')
    elif(dogAge == 0):
        print(f"The dog's age in dog years is {dogAge}.")
    elif(dogAge <= 2 and dogAge > 0):
        dogAge *= 10
        print(f"The dog's age in dog years is {dogAge}.")
    else:
        dogAge = 20 + (dogAge - 2)*7
        print(f"The dog's age in dog years is {dogAge}.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

banner(4)
def weather_advice():
    cold = input("Is it cold ? (yes/no) ").strip().lower()
    raining = input("Is it raining ? (yes/no) ").strip().lower()
    if(cold == 'yes' and raining == 'yes'):
        print('Wear a waterproof coat.')
    elif(cold == 'yes' and raining == 'no'):
        print('Wear a warm coat.')
    elif(cold == 'no' and raining == 'yes'):
        print('Carry an umbrella.')
    elif(cold == 'no' and raining == 'no'):
        print('Wear light clothing.')
    else:
        print('Invalid Input')

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

banner(5)
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").strip()
    day = input("Enter the day of the month: ").strip()
    date = month + ' ' + day
    winterCollection = ['Jan', 'Feb', 'Dec 21', 'Mar 19']
    springCollection = ['Apr', 'May', 'Mar 20', 'Jun 20']
    summerCollection = ['Jul', 'Aug', 'Jun 21', 'Sep 21']
    fallCollection = ['Oct', 'Nov', 'Sep 22', 'Dec 20']
    mixedCollection = ['Dec', 'Mar', 'Jun', 'Sep']
    months_30_days = ["Apr", "Jun", "Sep", "Nov"]
    months_31_days = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
    if(day.isdigit()):
        if((month in months_30_days and int(day) != 0 and int(day) <=30) or (month in months_31_days and int(day) != 0 and int(day) <=31) or (month == 'Feb' and int(day) != 0 and int(day) > 0 and int(day) <= 29)):
            if(month in winterCollection or date in winterCollection):
                season = "winter"
                print(f'{month} {day} is in {season}')
            elif(month in springCollection or date in springCollection):
                season = "spring"
                print(f'{month} {day} is in {season}')
            elif(month in summerCollection or date in summerCollection):
                season = "summer"
                print(f'{month} {day} is in {season}')
            elif(month in fallCollection or date in fallCollection):
                season = "fall"
                print(f'{month} {day} is in {season}')
            elif(month in mixedCollection):
                if(month == 'Dec'):
                    if(int(day) >= 21):
                        season = "winter"
                        print(f'{month} {day} is in {season}')
                    elif(int(day) <= 20):
                        season = "fall"
                        print(f'{month} {day} is in {season}')
                    else:
                        print('Invalid Input')
                elif(month == 'Mar'):
                    if(int(day) <= 19):
                        season = "winter"
                        print(f'{month} {day} is in {season}')
                    elif(int(day) >= 20):
                        season = "spring"
                        print(f'{month} {day} is in {season}')
                    else:
                        print('Invalid Input')
                elif(month == 'Jun'):
                    if(int(day) >= 21):
                        season = "summer"
                        print(f'{month} {day} is in {season}')
                    elif(int(day) <= 20):
                        season = "spring"
                        print(f'{month} {day} is in {season}')
                    else:
                        print('Invalid Input')
                elif(month == 'Sep'):
                    if(int(day) <= 21):
                        season = "summer"
                        print(f'{month} {day} is in {season}')
                    elif(int(day) >= 22):
                        season = "fall"
                        print(f'{month} {day} is in {season}')
                    else:
                        print('Invalid Input')
                else:
                    print('Invalid Input')
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')

# Call the function
determine_season()