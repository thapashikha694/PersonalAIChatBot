# Rule Based Python AI ChatBot

import datetime
import time

name = input("Welcome, Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    print("Good Morning,", name)

elif 12 <= presentHour < 17:
    print("Good Afternoon,", name)

elif 17 <= presentHour <= 20:
    print("Good Evening,", name)

else:
    print("Good Night,", name)

print("Hello!! Welcome To Your ChatBot..")
print("You can ask me Basic Questions, Type 'Bye' to exit from the bot")

# ChatBot Memory Creation (Dictionary of responses)

responses = {
    "hello": "Hi!! Welcome, How Can I Help You?",
    "how are you?": "I am Good!, Thank you!",
    "who are you?": "I am Smart Personal Chat Assistant! I am here to talk with you.",
    "can you motivate me": "Every small step brings you closer to success.",
    "thank you for your time": "It's fine, I am glad to help you anytime.",
    "okay, bye!": "Bye!, Have a wonderful day."
}


def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I am still learning."


while True:
    userInput = input("Ask Your Question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
       break