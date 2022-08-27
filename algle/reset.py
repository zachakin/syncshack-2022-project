import random
import js
import math
import csv

# Class for each algorithm
class algo:
    def __init__(self, id_: int, name: str, ds: str, atc: str, wtc: str, sc: str):
        self.id = id_
        self.name = name
        self.data_structure = ds
        self.avg_time_complexity = atc
        self.worst_time_complexity = wtc
        self.space_complexity = sc
    
    def __str__(self):
        return f'Name: {self.name}\nData Structure: {self.data_structure}\nAverage Time Complexity: {self.avg_time_complexity}\nWorst Case Time Complexity: {self.worst_time_complexity}\nSpace Complexity: {self.space_complexity}'

# Populates the dictionary of algo objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = algo(j,i[0],i[1],i[2],i[3], i[4])
            output[j] = a
            j += 1
    return output

algos = populate_options('./algos.csv')


# Resets the game
def reset(*args):
    # Get new random number that represents key of algorithm in dictionary
    r = list(range(len(algos)+1))
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

tbody = Element("tb").element

# Function to compare big O complexities
def compare_complexity(guess,actual):
    # Returns 1 if guess is faster than actual
    # Returns 0 if guess is slower than actual
    o_guess = guess[2:len(guess) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    o_actual = actual[2:len(actual) - 1].replace("^", "**").replace("n", "10000").replace("log", "math.log")
    eval_guess = eval(o_guess)
    eval_actual = eval(o_actual)
    return eval_guess < eval_actual

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
        pyscript.write("answer", ("Correct answer: " + algos[random_algo].name))
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
    atc_td = js.document.createElement("td")
    atc_td.textContent = guess.avg_time_complexity
    atc_td.value = guess.avg_time_complexity
    wtc_td = js.document.createElement("td")
    wtc_td.textContent = guess.worst_time_complexity
    wtc_td.value = guess.worst_time_complexity
    sc_td = js.document.createElement("td")
    sc_td.textContent = guess.space_complexity
    sc_td.value = guess.space_complexity


    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(ds_td)
    tr.appendChild(atc_td)
    tr.appendChild(wtc_td)
    tr.appendChild(sc_td)
    
    if guess.id == algos[random_algo].id:
        # Correct guess
        name_td.className = "bg-success"
        ds_td.className = "bg-success"
        atc_td.className = "bg-success"
        wtc_td.className = "bg-success"
        sc_td.className = "bg-success"
        js.localStorage.setItem("random_algo","True")
    else:
        # Incorrect guess
        if guess.data_structure == algos[random_algo].data_structure:
            ds_td.className = "bg-success"

        if guess.avg_time_complexity == algos[random_algo].avg_time_complexity:
            atc_td.className = "bg-success"
        elif compare_complexity(guess.avg_time_complexity,algos[random_algo].avg_time_complexity):
            # time complexity of guess is better than of actual
            # Down arrow: U+021E9
            atc_td.textContent = '> ' + atc_td.textContent
        else:
            # time complexity of guess is worse than actual
            # Up arrow: U+021E7
            atc_td.textContent = '< ' + atc_td.textContent
        
        if guess.worst_time_complexity == algos[random_algo].worst_time_complexity:
            wtc_td.className = "bg-success"
        elif compare_complexity(guess.worst_time_complexity,algos[random_algo].worst_time_complexity):
            # time complexity of guess is better than of actual
            # Down arrow: U+021E9
            wtc_td.textContent = '> ' + wtc_td.textContent
        else:
            # time complexity of guess is worse than actual
            # Up arrow: U+021E7
            wtc_td.textContent = '< ' + wtc_td.textContent

        if guess.space_complexity == algos[random_algo].space_complexity:
            sc_td.className = "bg-success"
        elif compare_complexity(guess.space_complexity,algos[random_algo].space_complexity):
            # time complexity of guess is better than of actual
            sc_td.textContent = '> ' + sc_td.textContent
        else:
            # time complexity of guess is worse than actual
            sc_td.textContent = '< ' + sc_td.textContent
        
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in algos.items():
        el = js.document.createElement("option")
        el.textContent = v.name
        el.value = k
        select.appendChild(el)

reset()
dropdown()