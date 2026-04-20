def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Input cannot be empty. Try again.")
        else:
            return value


def get_number(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Input cannot be empty.")
        elif not value.isdigit():
            print("Please enter a valid number.")
        else:
            return value
            

print("Select a story template:")
print("1 - Hospital story")
print("2 - Camping story")
print("3 - Castle story")

while True:
    choice = input("Select the number (1-3): ").strip()

    if choice in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

def hospital_story():
    number = get_number("Enter a number: ")
    time = get_text("Enter a measure of time (e.g., days, weeks): ")
    transport = get_text("Enter a mode of transportation: ")
    adjective = get_text("Enter an adjective: ")
    noun = get_text("Enter a noun: ")

    story = f"""
It was about {number} {time} ago when I arrived at the hospital in a {transport}.
The hospital is a {adjective} place. There are a lot of {noun} here.
"""
    print(story)

def camping_story():
    person = get_text("Enter a person's name: ")
    noun = get_text("Enter a noun: ")
    feeling = get_text("Enter a feeling: ")
    animal = get_text("Enter an animal: ")

    story = f"""
This weekend I am going camping with {person}.
I packed my lantern and {noun}.
I am so {feeling} to go camping.
I hope we don't meet a {animal}.
"""
    print(story)

def castle_story():
    person = get_text("Enter a person's name: ")
    adjective1 = get_text("Enter an adjective: ")
    color = get_text("Enter a color: ")
    number = get_number("Enter a number: ")
    verb_ing = get_text("Enter a verb ending in -ing: ")

    story = f"""
Dear {person}, I am writing to you from a {adjective1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color} animal in a faraway place.
There are {magical_creature1} and {magical_creature2} here!
In the {room} there is a pool full of {noun1}.
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective2} adventures.
It feels as though I have lived here for {number} days.
I hope one day you can visit, although the only way to get here now is {verb_ing} on a magical creature!!
"""
    print(story)


if choice == "1":
    hospital_story()
elif choice == "2":
    camping_story()
elif choice == "3":
    castle_story()
while True:
    if choice in ["1","2","3"]:
        break
