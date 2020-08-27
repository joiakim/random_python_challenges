# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.The results should be printed to the screen and saved to a new text file.
# reference AUTOMATE THE BORING STUFF CHAPTER 8, Page 195


madlibs = open('madlibsfile.txt', 'r')
contents = madlibs.read()
print(contents)

for word in contents.split():
    if word == 'NOUN':
        madlibs_edit = open('madlibs_edit.txt', 'w')
        new = contents.replace(word, str(input(print('ENTER A NOUN: '))), 1)
        madlibs_edit.write(new)
        contents = new
    if word == 'VERB':
        madlibs_edit = open('madlibs_edit.txt', 'w')
        new = contents.replace(word, str(input(print('ENTER A VERB: '))), 1)
        madlibs_edit.write(new)
        contents = new
    if word == 'ADJECTIVE':
        madlibs_edit = open('madlibs_edit.txt', 'w')
        new = contents.replace(word, str(input(print('ENTER AN ADJECTIVE: '))), 1)
        madlibs_edit.write(new)
        contents = new
else:
    print(contents)

























