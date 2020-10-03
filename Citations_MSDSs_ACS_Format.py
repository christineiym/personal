"""Creates citations for Manufacturer Safety Data Sheets (MSDSs) in the American Chemical Society format. 

Code written Jan. 10, 2020 using Python 2; docstrings added and one variable name changed Oct. 3, 2020.
"""


print "Hello!"


def cite():
    """Creates the actual citation."""
    print "Please enter the following information."

    chemical = raw_input("What is the name (not formula) of the chemical?\n")
    no = raw_input("What is the MSDS Number?\n")
    company = raw_input("What is the company name?\n")
    city = raw_input("What is the city name?\n")
    state_abbreviation = raw_input("What is the abbreviation of the state name?\n")
    month_abbreviation = raw_input("What is the month (abbreviated) it was last revised?\n")
    day = raw_input("What is the day it was last revised?\n")
    year = raw_input("What is the year it was last revised?\n")

    citation = "%s; MSDS No. %s; %s: %s, %s, %s %s, %s." % (chemical, no, company, city, state_abbreviation, month_abbreviation, day, year)

    print citation
cite()


def repeat():
    """Allows the user to create another citation before exiting the program, if he/she chooses."""
    more = raw_input("Do you want to cite another MSDS? Please type Y/N. ")
    if more =="N" or more =="n":
        print "Okay! Thank you for using this!"
    elif more =="Y" or more =="Y":
        cite()
        repeat()
    else:
        print "That is not a valid answer."
        repeat()
repeat()
