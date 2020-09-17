import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def Reading(file_name):
    f = open(os.path.join(BASE_DIR, 'politics_' + file_name + '.json'), 'r')
    line = f.readline()
    print(line)
    return line


def function(file_name):
    body = Reading(file_name)
    body = body[2:-8].lower()
    body = body.replace('u00a0', ' ').replace('u2019s', ' ').replace('u2014', ' ').replace('null', ' ').replace('u201d',
                                                                                                                ' ').replace(
        'U.S.', 'US').replace('D.C.', 'DC')

    for remove_mark in body:
        remove_mark = str.maketrans('\n\"\'\\.,:{}()-1234567890', '                      ')
        body = body.translate(remove_mark)

    body = body.split(' ')

    body = [word for word in body if word != '']
    print(body)
