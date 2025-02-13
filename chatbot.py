import random
import datetime

# TODO: Define a dictionary with predefined responses for common user inputs.
responses = {'love': {1: 'Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.',
                      2: 'Love is composed of a single soul inhabiting two bodies.',
                      3: 'We love life, not because we are used to living but because we are used to loving.',
                      4: 'To love and be loved is to feel the sun from both sides.',
                      5: 'Let us always meet each other with smile, for the smile is the beginning of love.'},
             'friendship': {1: 'The only way to have a friend is to be one.',
                            2: 'Love is the only force capable of transforming an enemy into a friend.',
                            3: 'A real friend is one who walks in when the rest of the world walks out.',
                            4: 'Walking with a friend in the dark is better than walking alone in the light.',
                            5: 'There is nothing on this earth more to be prized than true friendship.'},
             'motivational': {1: 'It does not matter how slowly you go as long as you do not stop.',
                              2: "It always seems impossible until it's done.",
                              3: 'Either you run the day or the day runs you.',
                              4: "Good, better, best. Never let it rest. 'Til your good is better and your better is best.",
                              5: 'If you fell down yesterday, stand up today.'}
             }


# TODO: Implement a function to get a random response based on user input.
def get_response(user_input):  # Replace with logic to match user input to predefined responses.
    random_number = random.randint(1, 5)
    if user_input.lower() == "love":
        return responses['love'][random_number]
    elif user_input.lower() == "friendship":
        return responses['friendship'][random_number]
    elif user_input.lower() == "motivational":
        return responses['motivational'][random_number]
    else:
        return "This theme in not part of my quotes library!"

# TODO: Implement a function to greet the user based on the current time.
def greet_user():  # Replace with logic to determine morning, afternoon, or evening greeting.
    x = datetime.datetime.now()
    if 6 <= int(x.strftime("%H")) <= 10:
        return "Good morning, "
    elif int(x.strftime("%H")) <= 14:
        return "Good day, "
    elif int(x.strftime("%H")) <= 17:
        return "Good afternoon, "
    elif int(x.strftime("%H")) <= 22:
        return "Good evening, "
    else:
        return "It's night. Please go to sleep, "


# TODO: Implement the main chatbot function that handles user interactions.
def chatbot():
    name = input("What is your name: ")
    print("🤖 Chatbot: " + greet_user() + name)
    print("🤖 Chatbot: I am quotes Chatbot")
    print("🤖 Chatbot: What type of quotes you want to receive?")
    print("🤖 Chatbot: love , friendship, motivational (type 'bye to exit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        print("🤖 Chatbot:", get_response(user_input))


# TODO: Ensure the chatbot function runs only when the script is executed directly.
if __name__ == "__main__":
    chatbot()