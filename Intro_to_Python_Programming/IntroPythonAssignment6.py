star_trek = [
'Star Trek Discovery', 'Star Trek Voyager',
'Star Trek Deep Space Nine', 'Star Trek Next Generation',
]
chicago_series = [
'Chicago Pd', 'Chicago Fire',
'Chicago Med', 'Chicago Justice'
]

law_and_order = [
'Law & Order', 'Law & Order: Special Victims Unit',
'Law & Order: Criminal Intent', 'Law & Order: Trial By Jury',
]

arrow_verse = [
'Arrow', 'The Flash',
'Supergirl', 'Batwoman'
]

marvel_verse = [
'Daredevil', 'Jessica Jones',
'Iron Fist', 'Luke Cage'
]

message = {
    'intro': "Welcome to the Television Franchise Rating Challenge.",
    'select': "Please select a number between 1 and 5 to get started.",
    'selects': "Please type the series you would like to review:",
    'quit': "If you want to quit just type Q.",
    'continue': "Would you like to rate another series? (Y/N)",
    'not_available': "That series is not on the list.",
    'incorrect': "Wrong input. To exit please read the prompt carefully.",
    'complete': "Thank you for rating every series. You are a rockstar!",
    'end': "Thank you for rating. Try a different franchise next time!",
    'kill': "I'm sorry, I did not understand that prompt. Goodbye!"
}

def series_input(choice):
    if choice == 1:
        return star_trek
    elif choice == 2:
        return chicago_series
    elif choice == 3:
        return law_and_order
    elif choice == 4:
        return arrow_verse
    elif choice == 5:
        return marvel_verse
    else:
        return print(message['incorrect'])

def str_format(user_input):
    return str(user_input).title()

def break_point(series_dict):
    print(message['end'])
    series_dict = {k: v for k, v in series_dict.items() if v is not None}
    return series_dict

def notrated_input():
    not_rated = [
        tv_show.title() for tv_show, rating in series_dict.items() if rating is None
    ]
    return not_rated

def avail_input():
    available_shows = ', '.join(not_rated)
    return available_shows

def retrieve_input():
    entry = str_format(
        input(
            f"\n{message['selects']}\n{available_shows}.\n{message['quit']}\n\n"))
    return entry

print(message['intro'])

try:
    choice = int(input(message['select']))
except choice > 5:
    print(message['kill'])
    quit()
except choice < 1:
    print(message['kill'])
    quit()
except ValueError:
    print(message['kill'])
    quit()
series_list = series_input(choice)
series_dict = {k: None for k in series_list}

cnt = 0
while None in series_dict.values():
    for tv_show, rating in series_dict.items():
        if rating is None:
            not_rated = notrated_input()
            available_shows = avail_input()
            selection = retrieve_input()
            if selection in not_rated:
                tv_show = selection
                rating = str_format(input(f"How good do you think {tv_show} is going to be?\n"))
                series_dict[tv_show] = rating
                cnt += 1
                print(f"You think that {tv_show} is going to be {rating}!")
                if cnt < len(series_list):
                    rate_again = str_format(input(message['continue']))
                    if rate_again == 'Y':
                        continue
                    elif rate_again == 'N':
                        series_dict = break_point(series_dict)
                        break
                    else:
                        print(message['incorrect'])
            elif selection == 'Q':
                series_dict = break_point(series_dict)
                break
            else:
                print(message['not_available'])
print("\nTo recap, you said that...")
for tv_show, rating in series_dict.items():
    print(f"{tv_show} is going to be {rating}!")
if cnt == len(series_list):
    print(message['complete'])
