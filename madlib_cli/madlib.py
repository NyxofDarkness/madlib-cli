print("""
****************************************************
**                                                **
***                   Welcome!                   ***
****           Today is a Day for fun!          ****
*****        Choose a word that meets the      *****
****           prompt and press enter!          ****
***                     ***                      ***
**                At the end you get              **
**              a fantastical adventure!          **
**                                                **
****************************************************
** adjective: describes something                 **
**                                                **
** adverb: describes an action                    **
**                                                **
** noun: person place or thing                    **
**                                                **
** verb: An action                                **
**                                                **
** exclaimation: (Wow!, Oh!, Yuck!)               **
** number: a number!                              **
** color: any color!                              **
****************************************************
****************************************************
""")

name = input('Please enter a name! =>')
adverb_a = input('Enter an adverb =>')
noun_a = input('Enter a noun =>')
verb_a = input('Enter a verb =>')
adjective_a = input('Enter an adjective =>')
noun_b = input('Enter a noun =>')
noun_c = input('Enter another noun please! =>')
adjective_b = input('Enter an adjective =>')
color = input('Enter a color =>')
noun_d = input('Enter a noun =>')
verb_b = input('Enter a verb =>')
exclaim = input('Enter an exclaimation! (i.e. Wow! Oh! Yuck!) =>')
number = input('Enter a number =>')

with open('assets/madlib.txt', 'r') as file:
    madlib = file.read()

    madlib = madlib.replace('{name}', name, 1)
    madlib = madlib.replace('{adverb}', adverb_a, 1)
    madlib = madlib.replace('{noun}', noun_a, 1)
    madlib = madlib.replace('{verb}', verb_a, 1)
    madlib = madlib.replace('{adjective}', adjective_a, 1)
    madlib = madlib.replace('{noun}', noun_b, 1)
    madlib = madlib.replace('{noun}', noun_c, 1)
    madlib = madlib.replace('{adjective}', adjective_b, 1)
    madlib = madlib.replace('{color}', color, 1)
    madlib = madlib.replace('{noun}', noun_d, 1)
    madlib = madlib.replace('{verb}', verb_b, 1)
    madlib = madlib.replace('{exclaimation}', exclaim, 1)
    madlib = madlib.replace('{exclaimation}', exclaim, 1)
    madlib = madlib.replace('{number}', number, 1)

    print(madlib)

with open('assets/result.txt', 'wt') as result:
    result.write(madlib)

import re

def read_template(i):
    with open(i) as text:
        madlib_read = text.read()
        return madlib_read

def parse_template(file):
    new_file = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", txt))
    new_madlib = file.replace(personal_mad[0], "")
    new_madlib = new_file.replace(personal_mad[2], "")
    return(new_file, personal_mad)

def merge(file_1, file_2):
    these_are_mad = file_1.format(file_2[0], file_2[1], file_3[2])
    print(these_are_mad)
    return these_are_mad
# print('is the file closed?', file.closed)

# madlib = open('assets/madlib.txt')
# list(madlib)
# for i in madlib:

# print(madlib)

# with open('assets/madlib.txt') as reader:
#     line = reader.readline()
#     while line != '':

#         print(line, end = '')
#         line = reader.readline()
