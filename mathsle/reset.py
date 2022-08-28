import random
import js
import math
import csv

# Class for each algorithm
class maths:
    def __init__(self, id_: int, funcstr: str, eval: str):
        self.id = id_
        self.funcstr = funcstr
        self.eval = eval
    
# Populates the dictionary of algo objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        # next(reader,None)
        for i in reader:
            a = maths(j,i[0],i[1])
            output[j] = a
            j += 1
    return output

functions = populate_options('./maths.csv')

import matplotlib.pyplot as plt
def mpl():
    random_algo = int(js.localStorage.getItem("random_algo"))
    func = functions[random_algo].eval

    x = list(range(1,101))
    y = []
    for i in range(1,101):
        val = eval(func.replace('x',str(i)))
        y.append(val)
    
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.grid(alpha=0.3)
    pyscript.write('mpl',fig)

# Resets the game
def reset(*args):
    # Get new random number that represents key of algorithm in dictionary
    r = list(range(len(functions)+1))
    random_algo = random.choice(r)
    # Store that random number in localStorage
    js.localStorage.setItem("random_algo", random_algo)

    # Store guesses remaining in localStorage
    js.localStorage.setItem("guesses_remaining",8)
    # Reset count on frontend
    pyscript.write("count","8")

    # Store has_won in localStorage
    js.localStorage.setItem("has_won","False")
   
    # Reset table
    tb = js.document.getElementById("tb")
    tb.innerHTML = ""

    # Reset answer
    answer = js.document.getElementById("answer")
    answer.innerHTML = ""

    # Draw plot
    mpl()

tbody = Element("tb").element

# Compares guess to the random algorithm
def compare_guess(*args):
    random_algo = int(js.localStorage.getItem("random_algo"))
    
    if js.localStorage.getItem("has_won") == "True":
        return

    # Count Guesses
    guesses_total = int(js.localStorage.getItem("guesses_remaining"))-1
    js.localStorage.setItem("guesses_remaining",guesses_total)
    # Prints correct algorithm
    if(guesses_total == 0):
        pyscript.write("answer", ("Correct answer: " + functions[random_algo].funcstr))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = functions[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")

    # Add columns for table
    func_td = js.document.createElement("td")
    func_td.textContent = guess.funcstr
    func_td.value = guess.funcstr

    # Add columns to row
    tr.appendChild(func_td)
    
    if guess.id == functions[random_algo].id:
        # Correct guess
        func_td.className = "bg-success"
        js.localStorage.setItem("random_algo","True")
        
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in functions.items():
        el = js.document.createElement("option")
        el.textContent = v.funcstr
        el.value = k
        select.appendChild(el)

reset()
dropdown()