import random
import js
import math
import csv

# Class for each element
class element:
    def __init__(self, id_: int, name: str, atomic_number: int, period: int, group: int, classification: str):
        self.id = id_
        self.name = name
        self.atomic_number = atomic_number
        self.period = period
        self.group = group
        self.classification = classification
    
    def __str__(self):
        return f'Name: {self.name}\nAtomic Number: {self.atomic_number}\nPeriod: {self.period}\nGroup: {self.group}\nClassification: {self.classification}'

# Populates the dictionary of element objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = element(j,i[0],i[1],i[2],i[3],i[4])
            output[j] = a
            j += 1
    return output

elements = populate_options('./elements.csv')

# Resets the game
def reset(*args):
    # Get new random number that represents key of element in dictionary
    r = list(range(len(elements)+1))
    random_element = random.choice(r)
    # Store that random number in localStorage
    js.localStorage.setItem("random_element", random_element)

    # Store guesses remaining in localStorage
    js.localStorage.setItem("guesses_remaining_chem",8)
    
    # !!!!!!
    pyscript.write("count", str(elements[random_element].name))

    # Reset count on frontend
    pyscript.write("count","8")

    # Store has_won_chem in localStorage
    js.localStorage.setItem("has_won_chem","False")
   
    # Reset table
    tb = js.document.getElementById("tb")
    tb.innerHTML = ""

    # Reset answer
    answer = js.document.getElementById("answer")
    answer.innerHTML = ""

tbody = Element("tb").element

# Compares guess to the random element
def compare_guess(*args):
    random_element = int(js.localStorage.getItem("random_element"))
    
    if js.localStorage.getItem("has_won_chem") == "True":
        return

    # Count Guesses
    guesses_total = int(js.localStorage.getItem("guesses_remaining_chem"))-1
    js.localStorage.setItem("guesses_remaining_chem",guesses_total)
    # Prints correct element
    if(guesses_total == 0):
        pyscript.write("answer", ("Correct answer: " + elements[random_element].name))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = elements[int(Element("selectNumber").element.value)]

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
    
    if guess.id == elements[random_element].id:
        # Correct guess
        name_td.className = "bg-success"
        an_td.className = "bg-success"
        p_td.className = "bg-success"
        g_td.className = "bg-success"
        cl_td.className = "bg-success"
        js.localStorage.setItem("has_won_chem","True")
    else:
        # Incorrect guess
        if guess.atomic_number == elements[random_element].atomic_number:
            an_td.className = "bg-success"
        elif int(guess.atomic_number) < int(elements[random_element].atomic_number):
            an_td.textContent = '> ' + an_td.textContent
        else:
            an_td.textContent = '< ' + an_td.textContent
        
        if guess.period == elements[random_element].period:
            p_td.className = "bg-success"
        elif int(guess.period) < int(elements[random_element].period):
            p_td.textContent = '> ' + p_td.textContent
        else:
            p_td.textContent = '< ' + p_td.textContent
        
        if guess.group == elements[random_element].group:
            g_td.className = "bg-success"
        elif int(guess.group) < int(elements[random_element].group):
            g_td.textContent = '> ' + g_td.textContent
        else:
            g_td.textContent = '< ' + g_td.textContent

        if guess.classification == elements[random_element].classification:
            cl_td.className = "bg-success"
    
    
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in elements.items():
        el = js.document.createElement("option")
        el.textContent = v.name
        el.value = k
        select.appendChild(el)

reset()
dropdown()
