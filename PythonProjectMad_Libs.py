print("Select a story template:")

print("1 - Hospital story")
print("2 - Camping story")
print("3 - Castle story")

choice = input("Select the number:")

def hospital_story():
    number = input("Enter a number: ")
    time = input("Enter a measure of time (e.g., days, weeks): ")
    transport = input("Enter a mode of transportation: ")
    adjective = input("Enter an adjective (e.g., scary, big): ")
    noun = input("Enter a noun (e.g., robot, chair): ")

    story = f"""
It was about {number} {time} ago when I arrived at the hospital in a {transport}.
The hospital is a {adjective} place. There are a lot of {noun} here.
"""
    print(story)

def camping_story():
    person = input("Enter a person's name: ")
    noun = input("Enter a noun (e.g., lantern, backpack): ")
    feeling = input("Enter a feeling (e.g., excited, nervous): ")
    animal = input("Enter an animal: ")

    story2 = f"""
This weekend I am going camping with {person}.
I packed my lantern and {noun}.
I am so {feeling} to go camping.
I hope we don't meet a {animal}.
"""
    print(story2)

def castl_story():
    person = input("Enter a person's name: ")
    adjective1 = input("Enter an adjective (e.g., magical, spooky): ")
    color = input("Enter a color: ")
    magical_creature1 = input("Enter a magical creature (plural): ")
    magical_creature2 = input("Enter another magical creature (plural): ")
    room = input("Enter a room in a house (e.g., kitchen, bedroom): ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter an adjective: ")
    noun3 = input("Enter another noun: ")
    number = input("Enter a number: ")
    verb_ing = input("Enter a verb ending in -ing: ")

    castlstory = f"""
Dear {person}, I am writing to you from a {adjective1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color} animal in a faraway place.
There are {magical_creature1} and {magical_creature2} here!
In the {room} there is a pool full of {noun1}.
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective2} adventures.
It feels as though I have lived here for {number} days.
I hope one day you can visit, although the only way to get here now is {verb_ing} on a magical creature!!
"""
    print(castlstory)


if choice == "1":
    hospital_story()
elif choice == "2":
    camping_story()
elif choice == "3":
    castl_story()
else:
    print("Invalid choice!")
