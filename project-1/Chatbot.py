from datetime import datetime
import random

print("Welcome user!"
 "\n---AI ChatBot started---")
print("Type help to see commands")
print("Type bye to exit")


name=input("Enter your name:").strip().lower()
greetings=[
    "Hello!" , "Hii!" , "Nice to see you!" , "Hey!"
]
print(random.choice(greetings),name)
motivation=[
    "Keep learning, you're doing great!",
    "Every expert was once a beginner.",
    "Success comes from practice and consistency.",
    "Believe in yourself and keep coding!"
]
compliments=[
    "You're very smart!",
    "Your coding skills are improving!",
    "You have a great learning attitude!",
    "You're doing an amazing job!"
]
jokes=[
    "Why did the AI cross the road? To optimize the route!",
    "I would tell you a coding joke, but it has too many bugs.",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]
responses={
    "hello":random.choice(greetings),
    "hii":random.choice(greetings),
    "hey":random.choice(greetings),
    "who are you":"Iam AI ChatBot",
    "what can you do":"I can chat, tell jokes , motivates you , give compliments , give time and more!!",
    "who created you":"Iam created with python",
    "how are you":"Iam doing great!",
    "thank you":"you're Welcome!"
}
while True:
    user_input=input("").lower().strip()
    if user_input=="bye":
        print("Bot:Goodbye!")
        print("Session ended succesfully.")
        break
    elif user_input=="help":
        print("""
        ====== MENU ======

        hello / hi
        joke
        time
        date
        calculator
        motivate me
        compliment me
        bye
        """)
        # Time feature
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is ", current_time)

    # Date feature
    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is ", current_date)

    # Joke feature
    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))

    # Motivation feature
    elif user_input == "motivate me":
        print("Bot:", random.choice(motivation))

    # Compliment feature
    elif user_input == "compliment me":
        print("Bot:", random.choice(compliments))

    # Mood detection
    elif "sad" in user_input:
        print("Bot: Don't worry. Better days are coming !")

    elif "happy" in user_input:
        print("Bot: That's wonderful to hear !")

    elif "tired" in user_input:
        print("Bot: Take some rest and recharge yourself !")
    # Dictionary responses
    elif user_input in responses:
        print("Bot:", responses[user_input])

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that command.")
