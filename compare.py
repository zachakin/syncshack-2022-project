from random_algo import random_algo
import js
from populate_options import algos

table = Element("tb").element

def compare_guess(*args):

    # Count Guesses
    table_length = js.document.querySelector("table")
    guesses_total = table_length.rows.length
    if(guesses_total > 8):
        print("Game Over")
        return
    guesses_string = str(guesses_total) + "/8"
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
        name_td.className = "bg-success"
        ds_td.className = "bg-success"
        tc_td.className = "bg-success"
        # sc_td.className = "table-success"
    else:
        # Incorrect guess
        if guess.data_structure == algos[random_algo].data_structure:
            ds_td.className = "bg-success"
        if guess.time_complexity == algos[random_algo].time_complexity:
            tc_td.className = "bg-success"
        # if guess.space_complexity == algos[random_algo].space_complexity:
        #     sc_td.className = "table-success"
        
    table.appendChild(tr)