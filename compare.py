from codecs import ascii_decode
from random_algo import random_algo
import js
import math
from populate_options import algos

tbody = Element("tb").element

def compare_complexity(guess,actual):
    # Returns 1 if guess is faster than actual
    # Returns 0 if guess is slower than actual
    o_guess = guess[2:len(guess) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    o_actual = actual[2:len(actual) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    eval_guess = eval(o_guess)
    eval_actual = eval(o_actual)
    return eval_guess < eval_actual

def compare_guess(*args):

    # Count Guesses
    guesses_total = 8 - Element("tbl").element.rows.length
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = algos[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")

    # Add columns for table
    name_td = js.document.createElement("td")
    name_td.textContent = guess.name
    name_td.value = guess.name
    ds_td = js.document.createElement("td")
    ds_td.textContent = guess.data_structure
    ds_td.value = guess.data_structure
    tc_td = js.document.createElement("td")
    tc_td.textContent = guess.time_complexity
    tc_td.value = guess.time_complexity
    sc_td = js.document.createElement("td")
    sc_td.textContent = guess.space_complexity
    sc_td.value = guess.space_complexity

    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(ds_td)
    tr.appendChild(tc_td)
    tr.appendChild(sc_td)
    
    if guess.id == algos[random_algo].id:
        # Correct guess
        name_td.className = "bg-success"
        ds_td.className = "bg-success"
        tc_td.className = "bg-success"
        sc_td.className = "bg-success"
    else:
        # Incorrect guess
        if guess.data_structure == algos[random_algo].data_structure:
            ds_td.className = "bg-success"
        
        if guess.time_complexity == algos[random_algo].time_complexity:
            tc_td.className = "bg-success"
        elif compare_complexity(guess.time_complexity,algos[random_algo].time_complexity):
            # time complexity of guess is better than of actual
            # Down arrow: U+021E9
            tc_td.textContent = '> ' + tc_td.textContent
        else:
            # time complexity of guess is worse than actual
            # Up arrow: U+021E7
            tc_td.textContent = '< ' + tc_td.textContent

        if guess.space_complexity == algos[random_algo].space_complexity:
            sc_td.className = "bg-success"
        elif compare_complexity(guess.space_complexity,algos[random_algo].space_complexity):
            # time complexity of guess is better than of actual
            sc_td.textContent = '> ' + sc_td.textContent
        else:
            # time complexity of guess is worse than actual
            sc_td.textContent = '< ' + sc_td.textContent
        
    tbody.appendChild(tr)
