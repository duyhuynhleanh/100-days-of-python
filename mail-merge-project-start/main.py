PLACE_HOLDER = "[name]"


with open('./Input/Names/invited_names.txt') as input_names:
    names = input_names.readlines()

with open('./Input/Letters/starting_letter.txt') as input_letter:
    letter = input_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)




