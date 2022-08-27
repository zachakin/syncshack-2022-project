from random_algo import random_algo

def compare_guess(*args):
    guess = Element("selectNumber").element.value
    if guess == random_algo[0]:
        pyscript.write("guess-table","right")
    else:
        pyscript.write("guess-table","wrong")