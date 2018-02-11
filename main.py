
from spy_details import spy_name, spy_rating, spy_salutation, spy_age

print 'Hello Let\'s get started '

status_message = ['Gucci gang! Gucci gang! Gucci gang', 'Second', 'third', 'fourth']


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
    print "dfgdg"



def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do? \n 1. Add a status  \n 2. Add a friend \n 0. Close application")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "Your updated status message is " + updated_status_message
            current_status_message = updated_status_message
        elif menu_choice == 2:
            print "sgfs"
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice"

existing = raw_input("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?")


if existing.upper() == "Y":
    #Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy_salutation, spy_name, spy_age, spy_rating)
    start_chat(spy_name, spy_age, spy_rating)

elif existing.upper() == "N":
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) >= 3:
            print "welcome " + spy_name + " Glad to meet you"
            spy_salutation = raw_input("what should i call you? Mr. or Ms. ")
            spy_name = spy_salutation + " " + spy_name
            print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

            spy_age = 0
            spy_rating = 0.0
            spy_is_online = False
            spy_age = input("What is your age?")

            if 12 < spy_age < 50:
                print "Well, You are at right age for this"
                spy_rating = input("what is your rating?")

                if spy_rating >= 4.5:
                    print "Great Ace!"
                elif 3.5 < spy_rating < 4.5:
                    print "You are one of the good ones"
                elif 2.5 < spy_rating < 3.5:
                    print "You have to try to do better"
                else:
                    print "you can always ask someone for help"

                spy_is_online = True
                print "Authentication complete. Welcome %s age: %d and rating of: %.1f Proud to have you onboard" % (spy_name, spy_age, spy_rating)
                start_chat(spy_name, spy_age, spy_rating)
            else:
                print "Sorry, you are not a match"

    else:
            print "Name must be of atleast 3 characters"

else:
    print "Invalid response"
