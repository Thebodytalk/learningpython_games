import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number higher than 0.')
        quit()
    else:
        print('Pick a number next time ya dummy!')
        quit()

random_number = random.randint(0, top_of_range)
print(random_number)
