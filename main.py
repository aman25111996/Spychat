from spy_details import spy_name, spy_rating, spy_salutation, spy_age

print 'Hello Let\'s get started '


def start_chat(spy_name,spy_age, spy_rating):
    menu_choice = input("What do you want to do? \n 1. Add a status update \n 0. Close application")
    show_menu = True
    while show_menu:
        if menu_choice == 1:
            spy_status = raw_input("Write a status update")
            print "your status is %s" % spy_status
        elif menu_choice == 0:
            show_menu = False
        else:
            show_menu = False
            print "Invalid choice"


existing = raw_input("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?")


if existing.upper() == "Y":
      #Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy_salutation,spy_name,spy_age,spy_rating)
    start_chat(spy_name,spy_age,spy_rating)

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

            if spy_age > 12 and spy_age < 50:
                print "Well, You are at right age for this"
                spy_rating = input("what is your rating?")

                if spy_rating >= 4.5:
                    print "Great Ace!"
                elif spy_rating >= 3.5 and spy_rating < 4.5:
                    print "You are one of the good ones"
                elif spy_rating >= 2.5 and spy_rating < 3.5:
                    print "You have to try to do better"
                else:
                    print "you can always ask someone for help"

                spy_is_online = True
                print "Authentication complete. Welcome %s %s age: %d and rating of: %.1f Proud to have you onboard" % (spy_salutation,spy_name,spy_age,spy_rating)
                start_chat(spy_name, spy_age, spy_rating)
            else:
                print "Sorry, you are not a match"

    else:
            print "Name must be of atleast 3 characters"

else:
    print "Invalid response"