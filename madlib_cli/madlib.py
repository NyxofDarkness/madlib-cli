# import re 

def read_template(path):
    with open(path) as file:
        string = file.read()
        return string

def parse_template(string):
    """this goes through the template looking for strings of {...} replaceing this first string with a temp on made up of user coices.

    Args:
        file strg, s_strg
    """
    count = 0
    list1 = []
    for character in string:
        count = count + 1
        if character == "{":
            end = string.find("}", count)
            s_strg = string[count:end]
            list1.append(s_strg)
            string = string.replace(s_strg, "", 1)
            count = count - len(s_strg)

    subs = tuple(list1)

    return(string, subs)
    print(subs)

def merge(string, user_tuple):
    madlib = string.format(*user_tuple)
    return madlib

def write_madlib(string):
    with open("madlib.txt", "wt") as file:
        file.write(string)

def main():
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

    raw_template = read_template('assets/madlib.txt')
    no_words, input_things = parse_template(raw_template)

    list1 = []
    for things in input_things:
        user_input = input(f"Enter a... {things.lower()}: ")
        list1.append(user_input)

    inputs = tuple(list1)

    user_madlib = merge(no_words, inputs)
    print(f"Here is your adventure...\n{user_madlib}")

    write_madlib(user_madlib)

if __name__ == "__main__":
    main()

