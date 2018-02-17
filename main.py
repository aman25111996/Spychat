# Importing steganography library for encoding and decoding messages
from steganography.steganography import Steganography

# Importing the default spy objects
from spy_details import spy, friends

# Import the classes
from spy_details import Spy, ChatMessage

# Importing csv files
import csv

# Importing termcolor library for providing colors to different type of text
from termcolor import colored

# Welcome message to the user
print 'Hello Let\'s get started '

# list for old status messages
status_message = ['coding', 'eating', 'sleeping', 'repeating']
chats = []


# defining a function for loading existing friends when application starts
def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            if row:
                name = row[0]
                salutation = row[1]
                rating = row[2]
                age = row[3]
                new_spy = Spy(name, salutation, rating, age)
                friends.append(new_spy)


# defining a function for loading chats history between user and a friend when application starts
def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            if row:
                name_of_sender = row[0]
                message_sent_to = row[1]
                text = row[2]
                sent_by_me = row[4]
                new_chat = ChatMessage(name_of_sender, message_sent_to, text, sent_by_me)
                chats.append(new_chat)


load_friends()
load_chats()


# defining a function for adding status
def add_status(c_s_m):
    # checking if any old status exists or not
    if c_s_m is not None:
        print "Your current status message is " + c_s_m + "\n"
    else:
        print "You don't have any current status"

    status_choice = raw_input("Do you want to add from old status (Y/N)?")

    # If user selects to add from old status
    if status_choice.upper() == 'Y':
        serial_no = 1
        for old_status in status_message:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_status_selection = input("Which one do you want to choose ")
        new_status = status_message[user_status_selection - 1]

    # if user wants to add a new status
    elif status_choice.upper() == 'N':
        new_status = raw_input("write your status")
        status_message.append(new_status)
    else:
        print "invalid entry"
    return new_status


# defining a function to add a new friend
def add_friend():
    new_friend = Spy('', '', 0.0, 0)
    new_friend.name = raw_input("what's your friend name?")
    new_friend.salutation = raw_input("Mr. or Ms.")
    new_friend.age = input("what's your friend age")
    new_friend.rating = input("what's your friend rating")
    # checking eligibility of the new friend
    if len(new_friend.name) > 0 and 50 >= new_friend.age >= 12 and new_friend.rating >= 4.5:
        # saving new friend details
        friends.append(new_friend)
        # writing the details of new friend in csv file
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.rating, new_friend.age, new_friend.is_online])
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)


# defining a function to select a friend from existing frie/nd//s
def select_friend():
    item_number = 0
    for friend in friends:
        print str(item_number + 1) + " " + friend.name
        item_number = item_number + 1
    user_selected_friend = int(raw_input("which friend you wanna select?"))
    user_index = user_selected_friend - 1
    return user_index


# defining a function to send a secret message by encoding
def send_message():
    selected_friend = select_friend()
    message = raw_input("Write the secret message")

    original_image = raw_input("Write the name of image with which you want to encode secret message(with extension)")
    output_path = "output.png"
    Steganography.encode(original_image, output_path, message)
    message_sent_to = friends[selected_friend].name
    new_chat = ChatMessage(spy.name, message_sent_to, message, True)
    friends[selected_friend].chats.append(new_chat)
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([spy.name, message_sent_to, new_chat.message, new_chat.time, new_chat.sent_by_me])


# defining a function to read a secret message from a friend
def read_message():
    chosen_friend = select_friend()
    print "Reading message from " + friends[chosen_friend].name
    output_path = raw_input("Name of the image you want to decoded the message from(with extension)")
    secret_message = Steganography.decode(output_path)
    print "secret message is " + secret_message
    new_chat = ChatMessage(spy.name, friends[chosen_friend].name, secret_message, False)
    friends[chosen_friend].chats.append(new_chat)


def read_chat_history():
    friend_choice = select_friend()

    print '\n'

    for chat in chats:
        if chat.sent_by_me and chat.message_sent_to == friends[friend_choice].name:
            # Date and time is printed in blue
            print (colored(str(chat.time.strftime("%d %B %Y %A %H : %M")) + ",", "blue")),
            # The message is printed in red
            print (colored("You : ", "red")),
            # Default black colour for text
            print str(chat.message)

        # Message sent by another spy
        elif chat.sent_by_me is False:
            # Date and time is printed in blue
            print (colored(str(chat.time.strftime("%d %B %Y %A %H : %M")) + ",", "blue")),
            # The message is printed in red
            print (colored(str(friends[friend_choice].name) + " : ", "red")),
            # Default black colour for text
            print str(chat.message)


def start_chat():

    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do?"
                            "\n 1. Add a status  "
                            "\n 2. Add a friend "
                            "\n 3. Send a secret message " 
                            "\n 4. read a secret message "
                            "\n 5. View chat history"
                            "\n 0. Close application")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "Your updated status message is " + updated_status_message
            current_status_message = updated_status_message
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print "Total friends: " + str(number_of_friends)
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice"


existing = raw_input("Continue as " + spy.salutation + " " + spy.name + "(Y/N)?")


if existing.upper() == "Y":
    # Continue with the default user/details imported from the helper file.
    print "Welcome %s %s Glad to have you back." % (spy.salutation, spy.name)
    start_chat()

elif existing.upper() == "N":
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) >= 3:
            print "welcome " + spy.name + " Glad to meet you"
            spy.salutation = raw_input("what should i call you? Mr. or Ms. ")
            spy.name = spy.salutation + " " + spy.name
            print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."

            spy.age = input("What is your age?")

            if 12 < spy.age < 50:
                print "Well, You are at right age for this"
                spy.rating = input("what is your rating?")

                if spy.rating >= 4.5:
                    print "Great Ace!"
                elif 3.5 < spy.rating < 4.5:
                    print "You are one of the good ones"
                elif 2.5 < spy.rating < 3.5:
                    print "You have to try to do better"
                else:
                    print "you can always ask someone for help"

                spy.is_online = True
                print "Authentication complete. Welcome %s age: %d and rating of: %.1f Proud to have you onboard" \
                      % (spy.name, spy.age, spy.rating)
                start_chat()
            else:
                print "Sorry, you are not a match"

    else:
            print "Name must be of atleast 3 characters"

else:
    print "Invalid response"
