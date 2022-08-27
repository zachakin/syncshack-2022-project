from codecs import ascii_decode
from random_periodic_table import random_periodic_table
import js
import math
from populate_options_chemle import periodic_table

tbody = Element("tb").element

def compare_complexity(guess,actual):
    # Returns 1 if guess is faster than actual
    # Returns 0 if guess is slower than actual
    # o_guess = guess[2:len(guess) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    # o_actual = actual[2:len(actual) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    # eval_guess = eval(o_guess)
    # eval_actual = eval(o_actual)
    # return eval_guess < eval_actual
    pass

def compare_guess(*args):

    # Count Guesses
    guesses_total = 8 - Element("tbl").element.rows.length

    # Prints correct algorithm
    if(guesses_total == 0):
        print(periodic_table[random_periodic_table].name)
        pyscript.write("answer", ("Correct answer: " + periodic_table[random_periodic_table].name))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = periodic_table[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")

    # Add columns for table
    name_td = js.document.createElement("td")
    name_td.textContent = guess.name
    name_td.value = guess.name
    an_td = js.document.createElement("td")
    an_td.textContent = guess.atomic_number
    an_td.value = guess.atomic_number
    p_td = js.document.createElement("td")
    p_td.textContent = guess.period
    p_td.value = guess.period
    g_td = js.document.createElement("td")
    g_td.textContent = guess.group
    g_td.value = guess.group
    cl_td = js.document.createElement("td")
    cl_td.textContent = guess.classification
    cl_td.value = guess.classification

    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(an_td)
    tr.appendChild(p_td)
    tr.appendChild(g_td)
    tr.appendChild(cl_td)
    
    if guess.id == periodic_table[random_periodic_table].id:
        # Correct guess
        name_td.className = "bg-success"
        an_td.className = "bg-success"
        p_td.className = "bg-success"
        g_td.className = "bg-success"
        cl_td.className = "bg-success"

    else:
        # Incorrect guess
        if guess.atomic_number == periodic_table[random_periodic_table].atomic_number:
            an_td.className = "bg-success"
        
        if guess.period == periodic_table[random_periodic_table].period:
            p_td.className = "bg-success"
        
        if guess.group == periodic_table[random_periodic_table].group:
            g_td.className = "bg-success"

        if guess.classification == periodic_table[random_periodic_table].classification:
            cl_td.className = "bg-success"
        
    tbody.appendChild(tr)
