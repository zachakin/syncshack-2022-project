from random_algo import random_algo
import js
import math
from populate_options import algos
from random_algo import gc

tbody = Element("tb").element


def complex_eval(o):
    o = o[2:len(o) - 1]
    o.replace("^", "**").replace("n", "10000").replace("log", "math.log")
    return eval(o)


def compare_guess(*args):
    if Element("tbl").element.rows.length > 8:
        return

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
    # sc_td = js.document.createElement("td")
    # sc_td.textContent = guess.time_complexity
    # sc_td.value = guess.time_complexity

    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(ds_td)
    tr.appendChild(tc_td)
    # tr.appendChild(sc_td)
    
    if guess.id == algos[random_algo].id:
        # Correct guess
        name_td.className = "table-success"
        ds_td.className = "table-success"
        tc_td.className = "table-success"
        # sc_td.className = "table-success"
    else:
        # Incorrect guess
        if guess.data_structure == algos[random_algo].data_structure:
            ds_td.className = "table-success"
        
        if guess.time_complexity == algos[random_algo].time_complexity:
            tc_td.className = "table-success"
        elif complex_eval(guess.time_complexity) > complex_eval(algos[random_algo].time_complexity):
            pass  # time complexity is worse
        elif complex_eval(guess.time_complextiy) > complex_eval(algos[random_algo].time_complexity):
            pass  # time complexity is better
        else:
            pass    # how tf did you get here?

        if guess.space_complexity == algos[random_algo].space_complexity:
            tc_td.className = "table-success"
        elif complex_eval(guess.space_complexity) > complex_eval(algos[random_algo].space_complexity):
            pass  # space complexity is worse
        elif complex_eval(guess.space_complextiy) > complex_eval(algos[random_algo].space_complexity):
            pass  # space complexity is better
        else:
            pass    # how tf did you get here?
        
    tbody.appendChild(tr)
