#!/usr/bin/env python

l = []
done = False

def get_word():
    return input("Type a word to add to the list: ")

print("Type 'EXIT' to exit")
while not done:
    print("There are currently {0} words in the list.".format(len(l)))

    word = get_word()
    if word == "EXIT":
        done = True
    else:
        l.append(word)

print("The words you entered in reverse order are:")
print(", ".join(reversed(l)))

