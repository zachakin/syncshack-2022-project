import random

def add_task(*args):

    print(args)

    list = ['dfs', 'bfs', 'dijkstras', 'bubble sort', 'heap sort']

    randVal = random.randint(0, 4)

    randList = list[randVal]

    guess_context = Element('guess').element.value

    if(guess_context == randList):
        out = "Correct!"
    else:
        out = "Wrong :("

    pyscript.write('secret', randList)
    pyscript.write('output', out)

    Element('guess').clear()