'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    count = word.count('th')
    if word == "":
        return count
    elif word.count('th') >= 1:
        return count
    else:
        return count
