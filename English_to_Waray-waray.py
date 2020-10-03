"""An English to Waray-waray dictionary that does not use the data structure Dict. 

Code written Jul. 9, 2018 using Python 2; 
docstrings/comments added, two variable names changed, and lines 283-290 (in repeat) added/edited Oct. 3, 2020.
"""


print "Welcome to the English--> Waray-waray dictionary!"


word = str(raw_input("Please enter the word that you would like to translate: "))
word = word.lower()


def translate_word(word):
    """Translates the word."""
    if word[0] == "a":
        if word == "american":
            print "Amerikano/a"
        elif word == "":  # These empty spaces were intended for future entries.
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "b":
        if word == "beautiful":
            print "mahusay (female; see also pretty)"
        elif word == "baby":
            print "bata"
        elif word == "bad":
            print "maraut"
        elif word == "ball":
            print "bola"
        elif word == "big":
            print "daku"
        elif word == "book":
            print "libro"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "c":
        if word == "christian":
            print "Kristohanon"
        elif word == "chair":
            print "lingkuran"
        elif word == "child":
            print "bata"
        elif word == "class":
            print "klase"
        elif word == "cold":
            print "matugnaw (thing)"
        elif word == "cooked vegetable":
            print "utan"
        elif word == "church":
            print "simbahan"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "d":
        if word == "difficult":
            print "makuri"
        elif word == "day":
            print "adlaw (as in light; see also sun)"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "e":
        if word == "easy":
            print "masayon"
        elif word == "eye":
            print "mata"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "f":
        if word == "father":
            print "tatay"
        elif word == "friend":
            print "sangkay"
        elif word == "filipino":
            print "Pilipino (male)"
        elif word == "fat":
            print "matambok"
        elif word == "full":
            print "puno"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "g":
        if word == "glass":
            print "baso"
        elif word == "good":
            print "maupay"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "h":
        if word == "he":
            print "hiya (see also she)"
        elif word == "handsome":
            print "gwapo (male)"
        elif word == "hot":
            print "mapaso"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "i":
        if word == "i":
            print "ako"
        elif word == "industrious":
            print "maduroto"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "j":
        if word == "jeepney":
            print "dyip"
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "k":
        if word == "":
            print ""
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "l":
        if word == "long":
            print "hataas (see also tall)"
        elif word == "lesson":
            print "leksyon"
        elif word == "lumber":
            print "kahoy (see also tree)"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "m":
        if word == "mother":
            print "nanay"
        elif word == "man":
            print "lalake (male); tawo (person; see also person)"
        elif word == "missionary":
            print "misyonaryo"
        elif word == "many":
            print "damo"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "n":
        if word == "nice":
            print "buotan"
        elif word == "naughty":
            print "malabad"
        elif word == "new":
            print "bag-o"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "o":
        if word == "old":
            print "daan"
        elif word == "ocean":
            print "dagat (see also sea)"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "p":
        if word == "pretty":
            print "mahusay (female; see also beautiful)"
        elif word == "paper":
            print "papel"
        elif word == "pencil":
            print "lapis"
        elif word == "problem":
            print "problema"
        elif word == "person":
            print "tawo (see also man)"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "q":
        if word == "":
            print ""
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "r":
        if word == "rich":
            print "riko"
        elif word == "round":
            print "malidong"
        elif word == "road":
            print "karsada (see also way)"
        elif word == "room":
            print "kwarto"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "s":
        if word == "she":
            print "hiya (see also he)"
        elif word == "student":
            print "estudyante"
        elif word == "strong":
            print "makusog (person); madig-on (things)"
        elif word == "small":
            print "gutlay"
        elif word == "sun":
            print "adlaw"
        elif word == "sea":
            print "dagat (see also ocean)"
        elif word == "short":
            print "habubo"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "t":
        if word == "they":
            print "hira"
        elif word == "teacher":
            print "maestro/a"
        elif word == "tall":
            print "hataas"
        elif word == "table":
            print "lamesa"
        elif word == "this":
            print "ini"
        elif word == "that":
            print "iton/ ito (near the speaker); adto (far from the speaker)"
        elif word == "tree":
            print "kahoy (see also lumber)"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "u":
        if word == "":
            print ""
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "v":
        if word == "vegetable":
            print "utan (cooked)"
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "w":
        if word == "we":
            print "kita (inclusive); kami (exclusive)"
        elif word == "wife":
            print "asawa"
        elif word == "woman":
            print "babaye"
        elif word == "white":
            print "mabusag"
        elif word == "way":
            print "karsada (see also road)"
        elif word == "water":
            print "tubig"
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "x":
        if word == "":
            print ""
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "y":
        if word == "you":
            print "ikaw/ka (informal); kamo (formal)"
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    elif word[0] == "z":
        if word == "":
            print ""
        elif word == "":
            print ""
        else:
            print "The word you looked for is not currently in the dictionary. We apologize for the inconvenience."
    else:
        print "I'm sorry, but that is not a word. Please enter something new."


translate_word(word)


def repeat():
    """Allows the user to translate another word, if he/she chooses to do so."""
    more = str(raw_input("Do you want to translate another word? Please type Y/N. "))
    if more == "N" or more == "n":  # Future implementations will use the lower() method.
        print "Okay! Thank you for using this!"
    elif more == "Y" or more == "y":
        word = str(raw_input("Please enter the word that you would like to translate: "))
        word = word.lower()
        translate_word(word)
        repeat()
    else:
        print "I'm sorry, that is not a valid response."
        repeat()
repeat()
