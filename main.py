from csv import reader as read
from random import choice as pick
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def initialize_topics(dict_file):
    """Generates and returns the dictionary from a csv-file (style 'topic';full number"""

    with open(dict_file, newline='') as trendlist:
        dict_reader = read(trendlist, delimiter=';')
        topics = {}

        for row in dict_reader:
            topics[row[0]] = int(row[1])
        return topics


def select_answer():
    """Gives the player the choice to choose 'A' or 'B' and returns the result"""

    choice = ""

    while choice != "a" and choice != "b":
        choice = input(
            "\nThe search number is...\n\n(A) higher ➕👍 \n(B) lower ➖👎\n > ").lower()
        if choice != "a" and choice != "b":
            print("Please only pick 'A' or 'B' !")
    return choice


def pick_topic(topic_dict):
    """Picks a random topic from the dictionary displays the name and returns a single key"""

    choice = pick(list(topic_dict))

    return choice


def compare_numbers(topic1, topic2, topic_dict):
    """Takes 2 topics and compares the number in the dictionary provided"""
    first_number = topic_dict[topic1]
    second_number = topic_dict[topic2]

    print("'{}': {}k searches".format(topic1, first_number))
    print("vs.\n '{}': ??k searches".format(topic2))
    answer = select_answer()

    if answer == "a" and second_number >= topic_dict[topic1]:
        print("Correct, the search number of '{}' was higher\n     ca. {}k searches !".format(topic2, second_number))
        

        go_on = input("Hit Enter for next round or 'N' for retire: ").lower()

        if go_on != "n":
            clear()
            return True
        else:
            return False

    elif answer == "b" and topic_dict[topic2] <= topic_dict[topic1]:
        print("Correct, the search number of '{}' was lower\n     ca. {}k searches !".format(topic2, topic_dict[topic2]))

        go_on = input("Hit Enter for next round or 'N' for retire: ").lower()

        if go_on != "n":
            clear()
            return True
        else:
            return False
    else:
        print("Wrong, the search number of\n '{}' was ca. {}k searches !".format(topic2, topic_dict[topic2]))
        return False

game = True
gamedict = initialize_topics('google_trends.csv')
score = -1

first_topic = pick_topic(gamedict)

while game:
    score += 1
    new_topic = pick_topic(gamedict)

    game = compare_numbers(first_topic, new_topic, gamedict)
    first_topic = new_topic
print("Game Over, your end score is {}".format(score))