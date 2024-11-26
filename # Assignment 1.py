# Assignment 1

# Exercise 1 
word1 = "Coding"
word2 = "is"
word3 = "Cool"
print(word1 + " " + word2 + " " + word3)

# Exercise 2
num1 = 8
num2 = 10
sum_result = num1 + num2
print(sum_result)

# Exercise 3
bio = {
    "name": "Ayesha Ali",
    "hometown": "Pakistan",
    "age": 18
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")

# Exercise 4
answer = input("What is the capital of France? ")

if answer == "Paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The correct answer is Paris.")
    
# Exercise 5
months = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
month = int(input("Enter a month number (1-12): "))

# Exercise 6
if 1 <= month <= 12:
    print(f"The month {month} has {months[month]} days.")
else:
    print("Invalid month number.")

correct_password = "12345"
password = ""

while password != correct_password:
    password = input("Enter the password: ")
print("Access granted.")

# Exercise 7
print("Count up from 0 to 50:")
for i in range(0, 51):
    print(i, end=" ")
print("\nCount down from 50 to 0:")
for i in range(50, -1, -1):
    print(i, end=" ")
print("\nCount up from 30 to 50:")
for i in range(30, 51):
    print(i, end=" ")
print("\nCount down from 50 to 10 by 2:")
for i in range(50, 9, -2):
    print(i, end=" ")
print("\nCount up from 100 to 200 by 5:")
for i in range(100, 201, 5):
    print(i, end=" ")

# Exercise 8
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = "Sam"

if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")

# Exercise 9
def hello():
    print("Hello")  

def main():
    hello()  

if __name__ == "__main__":
    main()

# Exercise 10
def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    try:
        number = int(input("Enter a number: "))
        result = is_even_or_odd(number)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
