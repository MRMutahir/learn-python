import pyttsx3

user_bot = "Alex"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate',150)  # Male voice

get_msg = input("Enter your message (type 'q' to quit): ")

if get_msg.lower() == "q":
    engine.say("Bye bye")
    engine.runAndWait()


print(get_msg)


engine.say(f"Hi, I am {user_bot}. {get_msg}")
engine.runAndWait()
