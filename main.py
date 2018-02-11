
from spy_details import spy

print 'Hello Let\'s get started '

status_message = ['Gucci gang! Gucci gang! Gucci gang', 'Second', 'third', 'fourth']
friends = [{'name': 'aman', 'age': 21, 'rating': 9.5, 'is_online': True},
           {'name': 'udit', 'age': 22, 'rating': 9.4, 'is_online': True}]


def add_status(c_s_m):
    if c_s_m is not None:
        print "Your current status message is " + c_s_m + "\n"
    else:
        print "You don't have any current status"

    status_choice = raw_input("Do you want to add from old status (Y/N)?")

    if status_choice.upper() == 'Y':
        serial_no = 1
        for old_status in status_message:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_status_selection = input("Which one do you want to choose ")
        new_status = status_message[user_status_selection - 1]
    elif status_choice.upper() == 'N':
        new_status = raw_input("write your status")
        status_message.append(new_status)
    else:
        print "invalid entry"
    return new_status


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("what's your friend name?")
    new_friend['salutation'] = raw_input("Mr. or Ms.")
    new_friend['age'] = input("what's your friend age")
    new_friend['rating'] = input("what's your friend rating")
    if len(new_friend['name']) > 0 and 50 >= new_friend['age'] >= 12 and new_friend['rating'] >= 4.5:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)


def select_friend():
    item_number = 0
    for friend in friends:
        print str(item_number + 1) + " " + friend['name']
        item_number = item_number + 1
    user_selected_friend = input("which friend you wanna select?")
    user_index = friends[user_selected_friend - 1]
    return user_index['name']



def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do?"
                            "\n 1. Add a status  "
                            "\n 2. Add a friend "
                            "\n 3. Select a friend "
                            "\n 0. Close application")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "Your updated status message is " + updated_status_message
            current_status_message = updated_status_message
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print "Total friends " + str(number_of_friends)
        elif menu_choice == 3:
            selected_friend = select_friend()
            print "we are sending message to " + selected_friend
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice"


existing = raw_input("Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?")


if existing.upper() == "Y":
    # Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy['salutation'], spy['name'], spy['age'], spy['rating'])
    start_chat(spy['name'], spy['age'], spy['rating'])

elif existing.upper() == "N":
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) >= 3:
            print "welcome " + spy['name'] + " Glad to meet you"
            spy['salutation'] = raw_input("what should i call you? Mr. or Ms. ")
            spy['name'] = spy['salutation'] + " " + spy['name']
            print "Alright " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."

            spy['age'] = input("What is your age?")

            if 12 < spy['age'] < 50:
                print "Well, You are at right age for this"
                spy['rating'] = input("what is your rating?")

                if spy['rating'] >= 4.5:
                    print "Great Ace!"
                elif 3.5 < spy['rating'] < 4.5:
                    print "You are one of the good ones"
                elif 2.5 < spy['rating'] < 3.5:
                    print "You have to try to do better"
                else:
                    print "you can always ask someone for help"

                spy['is_online'] = True
                print "Authentication complete. Welcome %s age: %d and rating of: %.1f Proud to have you onboard" % (spy['name'], spy['age'], spy['rating'])
                start_chat(spy['name'], spy['age'], spy['rating'])
            else:
                print "Sorry, you are not a match"

    else:
            print "Name must be of atleast 3 characters"

else:
    print "Invalid response"
