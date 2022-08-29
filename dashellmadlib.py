name = input("Name of someone in the room:")
Noun1 = input("Noun:")
noun2 = input("Noun:")
adj1 = input("Adjective:")
adj2 = input("Adjective:")
adj3 = input("Adjective:")
sentence = input("type in a short sentence:")
verb1 = input("Verb:")
verb2 = input("Verb:")
verb3 = input("Verb:")
bodypart = input("bodypart:")

MadLib = f"{name} was walking through the {noun1} and {name} saw a/an {adj1}, {adj2} {noun2}. \
The {noun2} looked at {name} and said: '{sentence}' {name} jumped back and {verb1}. He/she hit the \
{noun2} on the {bodypart}. The {noun2} {verb2} and {verb3} away. {name} continued walking on his/her \
path and lived {adj3} ever after."


print(MadLib)