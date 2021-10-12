import math
import random

name = input("Howdy. What is your name? ")
question = input("Ask me any question: ")
answer = ""

# my_list = ["apple", "banana", "cherry", "orange", "kiwi"]
# print(random.choice(my_list))

random_number = random.randint(1,9)
 # print (random_number)

if random_number == 1:
    answer = "yes - definitely"
elif random_number == 2:
    answer = "It decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:   
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

print("Hi "+ name + " , you asked: " + question)
print(f"The Magic Eight Ball Answer: {answer}.")
# print(Magic  8-Ball) answer [My Sources say no]