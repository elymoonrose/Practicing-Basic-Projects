# You will be given 12 general knowledge questions. For each one you will earn 1 point if the answer is correct.
# Once you finish, you'll see how many answers you got correct, as well as the accuracy percentage.

print("Welcome to the quiz!")

playing = input("Do you want to start the quiz? (y/n) ")

if playing.lower() != "y":
    quit()
print("Alright, let's begin!")
score = 0

answer = input("What is the national animal of Australia? ")
if answer.lower() == "kangaroo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("How many days does it take for the Earth to orbit the Sun? ")
if answer.lower() == "365":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Name the longest river in the world ")
if answer.lower() == "the nile":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is the largest mammal in the world? ")
if answer.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Who painted the Mona Lisa? ")
if answer.lower() == "leonardo da vinci":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input(
    "What popular ice cream flavor is typically made with crushed cookies? ")
if answer.lower() == "cookies and cream":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is the name of the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("In what galaxy is our solar system located? ")
if answer.lower() == "milky way":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Which planet is known as the “Blue Planet”? ")
if answer.lower() == "earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Who is known as the “Father of Modern Physics”? ")
if answer.lower() == "albert einstein":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("In which year did World War II end? ")
if answer.lower() == "1945":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("How many zodiac signs are there? ")
if answer.lower() == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct! Congrats!")
print("The percentage of accuracy is " + str(round((score / 12) * 100)) + "%.")
