import random # Random number generator

# Declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.

name = "Mark"

#declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.

question = "Am I going to pass?"

#store the answer of the Magic 8-Ball in another variable
answer = ""

# Get the random number

random_number = random.randint(1,9)

# Control flow tree for guesses

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  print("Error")


print(name, "asks :", question)
print("Magic 8-ball's anser: ", answer)

