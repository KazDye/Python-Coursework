pet_list = [
    'cat', 'dog', 'hamster', 'rat', 'camel', 'ostrich', 'anaconda',
    'tarantula', 'parrot', 'alpaca', 'horse'
]
pet_dict = {k: None for k in pet_list}
message = {
    'intro': "Molly needs help coloring the animals in her coloring book.",
    'select': "Please type in one of the following animals to help her color:",
    'quit': "If you want to quit just type Q.",
    'continue': "Would you like to continue to help Molly color? (Y/N)",
    'not_available': "That animal is not in the list.",
    'incorrect': "Wrong input. To exit please read the prompt carefully.",
    'complete': "You helped Molly color all the animals. You are a superstar!",
    'end': "Come back soon!"
}

def str_format(user_input):
    return str(user_input).lower()

def uncolored_input():
    uncolored_pets = [
        pet.title() for pet, color in pet_dict.items() if color is None
    ]
    return uncolored_pets

def avail_input():
    available_pets = ', '.join(uncolored_pets)
    return available_pets

def retrieve_input():
    entry = str_format(
        input(
            f"\n{message['select']}\n{available_pets}.\n{message['quit']}\n\n"))
    return entry

def break_point(pet_dict):
    print(message['end'])
    pet_dict = {k: v for k, v in pet_dict.items() if v is not None}
    return pet_dict

def function(user_input):
    if color_next == 'y':
        return continue
    elif color_next == 'n':
        return pet_dict = break_point(pet_dict)
        return break
    else:
        return print(message['incorrect'])

cnt = 0
print(message['intro'])
while None in pet_dict.values():
    for pet, color in pet_dict.items():
        if color is None:
            uncolored_pets = uncolored_input()
            available_pets = avail_input()
            choice = retrieve_input()
            if choice.title() in uncolored_pets:
                pet = choice
                color = str_format(input(f"What color should the {pet} be?\n"))
                pet_dict[pet] = color
                cnt += 1
                print(f"You helped Molly color the {pet} {color}!")
                if cnt < len(pet_list):
                    color_next = str_format(input(message['continue']))
                    color_next = function(color_next)
            elif choice == 'q':
                pet_dict = break_point(pet_dict)
                break
            else:
                print(message['not_available'])
print("\nTo recap, you helped Molly color...")
for pet, color in pet_dict.items():
    print(f"The {pet} {color}!")
if cnt == len(pet_list):
    print(message['complete'])
