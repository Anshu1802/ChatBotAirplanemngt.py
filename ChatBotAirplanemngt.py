#created by ansh kevadiya 
import random
from string import punctuation, ascii_letters, digits
import datetime
from win32com.client import Dispatch

speak = Dispatch("SAPI.spvoice")
speak.Speak(
    "good afternoon everyone present here . we group Ansh are going to present our project on air plane management system . and our company name is Bhaarat AIRWAYS . we selected this topic because . it was quite challenging and Has been some kind of fun with it . first after my voice gets over. it will ask for personal details . there after there will be four options . booking a ticket.  alarm for reminder  . service . and much more. so with out wasting time lets get started. now i would like to hand over to my colleagues  ansh keva diya  thank you over to you guys....")


def hardsec():
    xer = input("Please enter your name for security of database: \n")
    if xer == "ansh" or xer == "grishma" or xer == "himanshu" or xer == "shraddha" or xer == "keven":
        database()
    else:
        print("You aren't authorized to view data. ")
        press()


def date():
    import datetime
    return datetime.datetime.now()


def security():
    pass


def password():
    size = 9
    mix = ascii_letters + punctuation + digits
    endpass = random.SystemRandom()  # it is a function which will select anything from mix
    passwordgenerator = "".join(endpass.choice(mix) for i in range(size))
    print(passwordgenerator)


def press():
    hii = int(input("Press 0 for Home "))
    if hii == 0:

        home()
    else:
        speak = Dispatch("SAPI.spvoice")
        speak.Speak("Thank you for keenly listening to us and paying attention to our project on behalf of team 3.")


def sure():
    confirm = int(input("Are you sure you want to book ?\n 1.Yes \n 2.No \n"))
    if confirm == 1:
        print("Your booking has been confirmed. \n Thank you for choosing Bharat Airways.")
    else:
        print("Request Timeout!!!")


def ticket():
    words = ['A', 'B', 'C', 'D', 'E']
    wing = random.choice(words)
    cusid = random.randint(1000000000, 5000000000)
    x = datetime.datetime.now()
    print("-----------------------------------------------------------------------")
    print("   NAME           BANK A/C             WING        CUSTOMER ID(unique)    DATE OF BOOKING   ")
    print("  ", name, "          ", bank_balance, "               ", wing, "            ", cusid, "         ", x)

    print("Thank-you for choosing Bharat Airways, Have a safe and peaceful journey. ")
    print("-----------------------------------------------------------------------")


def booking_tic():
    print(" \n 1. International Flight \n 2. Domestic Flight \n 3. Private Jet \n 4. VIP Flight")
    flight = int(input("Select the Airways: \n"))
    if flight == 1:
        print("-------------------------------------------------------------------------------------------")
        print("1. Air India\n2. Jet Airways\n3. Emirates Qatar Airways\n4. Vistara")
        international = int(input("Select the International Brand: "))
        if international == 1 or international == 2 or international == 3 or international == 4:
            print("International Flight Price is $305")
            print("1. First Class \n2. Economy Class \n3. Business Class")
            premimum = int(input("select the class ?"))
            if premimum == 1:
                print("You have selected 1st Class which charges extra $80")
                eigthy = bank_balance - 385
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()

            elif premimum == 2:
                print("You have selected Economy Class which charges extra $40")
                eigthy = bank_balance - 345
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()

            else:
                print("You have selected Business Class charges extra $290")
                eigthy = bank_balance - 595
                print(sure())
                print("bank balance after the booking is ", eigthy)
                print("name is ", name, " mobile number is ", number)
                print(ticket())
                press()







    # ------------------------------------------------------------------------------------------------------------------------

    elif flight == 2:
        print("-------------------------------------------------------------------------------------------")
        print("1. Air India\n2. Jet Airways\n3. IndiGo ")
        domestic = int(input("Select the Domestic Brand ? "))
        if domestic == 1 or domestic == 2 or domestic == 3:
            print("Domestic Flight price is $175")
            print("1. First class \n2. Economy class \n3. Business class")
            premimum = int(input("Select the class ?"))
            if premimum == 1:
                print("You have selected First Class which charges extra $80")
                eigthy = bank_balance - 255
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()



            elif premimum == 2:
                print("You have selected Economy Class which charges extra $40")
                eigthy = bank_balance - 215
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()
            else:
                print("You have selected Business Class which charges extra $290")
                eigthy = bank_balance - 465
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()



    # -------------------------------------------------------------------------------------------------------------------
    elif flight == 3:
        print("-------------------------------------------------------------------------------------------")
        print("1. Air India\n2. Jet Airways\n3. SpirceJet ")
        domestic = int(input("Select the Jet Brand ?"))
        if domestic == 1 or domestic == 2 or domestic == 3:
            food = int(input("Food & BAR included ? \n1. Yes \n2. No \n"))
            if food == 1:
                print("Private jet with food included charge after all charges is")
                eigthy = bank_balance - 1775
                print(sure())
                print("Bank Balance after the booking is ", eigthy)
                print("Name is ", name, " mobile number is ", number)
                print(ticket())
                press()
            else:
                eigthy = bank_balance - 1775
                print("Name is ", name, " mobile number is ", number)
                print("Without food pvt jet total price $", eigthy)
                press()
    # - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - --  - - - -- - - - - - - -
    else:
        print("---------------------------------------------------------------------------------------------")
        print("Special Guests are welcomed,  we have best security and safety precaution during Covid-19. ")
        print("Charges for special guest is $5000 per hour. ")
        eigthy = bank_balance - 5000
        print(sure())
        # =-=-=-=-==ansh kevadiya =-=-=-=-=purpose for doing this
        print("Bank Balance after the booking is ", eigthy)
        print("Name is ", name, " mobile number is ", number)
        print(ticket())
        press()

        # -------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------


print("Welcome to Bharat Airways--> A internation ride")
print("Where do you find our app ? \n 1. Social media \n 2. Friends \n 3. Agent ")
find = int(input("Select Input "))
if find == 1:
    print("Thanks your response is saved, please proceed, Bharat Airways")
elif find == 2:
    print("Thanks your review is submitted please proceed, Bharat Airways")
else:
    print("Thanks for your time please proceed, Bharat Airways")
print("------------------------------------------------------------------------------------------------")
name = input("Enter the name \n")
print("Your Random Generated Password is : ")
password()
number = int(input("Enter mobile number to link to your bank account: "))
bank_balance = random.randint(1000, 20000)
print("Your Bank Balance is $", bank_balance)


# ------------------------------------------------------------service ---------------------------------------------------------------->
def tokyo():
    oslo = int(input(" Services we provide---> \n 1. Food \n 2. Give Feedbacks \n 3. See Feedback \n"))
    if oslo == 1:
        obj = open("food.txt", "r")
        le = obj.read()
        print(le)
        obj.close()
        press()
    elif oslo == 2:
        with open("feedback.txt", "a") as feed:
            print("Please enter Feedback :")
            feed.write(input())
            feed.write("\n")
            feed.close()
            print("Thanks for Review :)")
            press()
    else:
        denver = open("feedback.txt", "r")
        smile = denver.read()
        print(smile)
        denver.close()
        press()


# ---------------------------------------------------------------------main menu-------------------------------------------------------->

def home():
    batra = int(
        input(
            " \n-------HOME--------\n\n 1. Book a Ticket \n\n 2. Set Alarm for Flight Time \n\n 3. Flight Service \n\n 4. Database \n\n 5. EXIT \n\n"))
    if batra == 1:
        print(" ")
        booking_tic()
    elif batra == 2:
        print(" ")
        alarmsys()
    elif batra == 3:
        print(" ")
        tokyo()
    elif batra == 4:
        print(" ")
        hardsec()
    else:
        exit()


# ---------------------------------------------------------database----------------->

def database():
    moscow = open("database.txt", "a")
    moscow.write("---------------------------------------------------------------------------")
    moscow.write("\n")
    moscow.write(str(name))
    moscow.write("\n")
    moscow.write(str(number))
    moscow.write("\n")
    moscow.write(str(bank_balance))
    moscow.write("\n")
    moscow.write(str(date()))
    moscow.write("\n")
    moscow.write("---------------------------------------------------------------------------")
    moscow.close()

    happy = open("database.txt", "r")
    khush = happy.read()
    print(khush)
    happy.close()
    press()


def exitss():
    exit()


# ------------------------------------------------------------------------------------------------------------------------------------>


# alarm system for flight 007 ap
def alarmsys():
    # alarm set

    print("Bharat Airways (A international ride)")
    alarm = int(input("Set alarm ? \n 1. Yes \n 2. No \n"))
    try:
        print("Bharat Airways ( A international ride ) ! Welcomes you")
        al = int(input("1. Set alarm \n 2. Alarm status \n"))
        if al == 1:

            f = open("alarm system.txt", "a")
            l = str(date())
            f.write(l)
            f.write(" : ")
            print("Enter the time: in format hr : min : sec pm/am")
            f.write(input())
            f.write(" \n ")
            f.close()
        else:

            f = open("alarm system.txt", "r")
            l = f.read()

            print(l)
            f.close()

    except Exception as e:
        print(e)
    else:
        print("Have a Good Day.)")
    finally:
        print("Thank You being with us ...! Bharat Airways")
        press()


home()

# speak = Dispatch("SAPI.spvoice")
# speak.Speak(
#     "Thank you for keenly listening to us and paying attention to our project on behalf of team Ansh")
