import random
import js
import math
import csv

# Class for each movie
class movie:
    def __init__(self, id_: int, name: str, runtime: int, release_year: int, oscars: int, bafta: int, golden_globe: int):
        self.id = id_
        self.name = name
        self.runtime = runtime
        self.release_year = release_year
        self.oscars = oscars
        self.bafta = bafta
        self.golden_globe = golden_globe

    
    def __str__(self):
        return f'Name: {self.name}\nRuntime: {self.runtime}\nRelease Year: {self.release_year}\nOscars: {self.oscars}\nBAFTAs: {self.bafta}\nGolden Globes: {self.golden_globe}'

# Populates the dictionary of element objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = movie(j,i[0],i[1],i[2],i[3],i[4],i[5])
            output[j] = a
            j += 1
    return output

movies = populate_options('./movies.csv')

# Resets the game
def reset(*args):
    # Get new random number that represents key of element in dictionary
    r = list(range(len(movies)+1))
    random_movie = random.choice(r)
    # Store that random number in localStorage
    js.localStorage.setItem("random_movie", random_movie)

    # Store guesses remaining in localStorage
    js.localStorage.setItem("guesses_remaining_movie",8)
    # Reset count on frontend
    pyscript.write("count","8")

    # Store has_won_chem in localStorage
    js.localStorage.setItem("has_won_movie","False")
   
    # Reset table
    tb = js.document.getElementById("tb")
    tb.innerHTML = ""

    # Reset answer
    answer = js.document.getElementById("answer")
    answer.innerHTML = ""

tbody = Element("tb").element

# Compares guess to the random element
def compare_guess(*args):
    random_movie = int(js.localStorage.getItem("random_movie"))
    
    if js.localStorage.getItem("has_won_movie") == "True":
        return

    # Count Guesses
    guesses_total = int(js.localStorage.getItem("guesses_remaining_movie"))-1
    js.localStorage.setItem("guesses_remaining_movie",guesses_total)
    # Prints correct element
    if(guesses_total == 0):
        pyscript.write("answer", ("Correct answer: " + movies[random_movie].name))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = movies[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")

    # Add columns for table
    name_td = js.document.createElement("td")
    name_td.textContent = guess.name
    name_td.value = guess.name
    run_td = js.document.createElement("td")
    run_td.textContent = guess.runtime
    run_td.value = guess.runtime
    ry_td = js.document.createElement("td")
    ry_td.textContent = guess.release_year
    ry_td.value = guess.release_year
    o_td = js.document.createElement("td")
    o_td.textContent = guess.oscars
    o_td.value = guess.oscars
    b_td = js.document.createElement("td")
    b_td.textContent = guess.bafta
    b_td.value = guess.bafta
    g_td = js.document.createElement("td")
    g_td.textContent = guess.golden_globe
    g_td.value = guess.golden_globe

    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(run_td)
    tr.appendChild(ry_td)
    tr.appendChild(o_td)
    tr.appendChild(b_td)
    tr.appendChild(g_td)

    
    if guess.id == movies[random_movie].id:
        # Correct guess
        name_td.className = "bg-success"
        run_td.className = "bg-success"
        ry_td.className = "bg-success"
        o_td.className = "bg-success"
        b_td.className = "bg-success"
        g_td.className = "bg-success"
    else:
        # Incorrect guess
        if int(guess.runtime) == int(movies[random_movie].runtime):
            run_td.className = "bg-success"
        elif int(guess.runtime) < int(movies[random_movie].runtime):
            run_td.textContent = '> ' + run_td.textContent
        else:
            run_td.textContent = '< ' + run_td.textContent
        
        if int(guess.release_year) == int(movies[random_movie].release_year):
            ry_td.className = "bg-success"
        elif int(guess.release_year) < int(movies[random_movie].release_year):
            ry_td.textContent = '> ' + ry_td.textContent
        else:
            ry_td.textContent = '< ' + ry_td.textContent
        
        if int(guess.oscars) == int(movies[random_movie].oscars):
            o_td.className = "bg-success"
        elif int(guess.oscars) < int(movies[random_movie].oscars):
            o_td.textContent = '> ' + o_td.textContent
        else:
            o_td.textContent = '< ' + o_td.textContent

        if int(guess.bafta) == int(movies[random_movie].bafta):
            b_td.className = "bg-success"
        elif int(guess.bafta) < int(movies[random_movie].bafta):
            b_td.textContent = '> ' + b_td.textContent
        else:
            b_td.textContent = '< ' + b_td.textContent

        if int(guess.golden_globe) == int(movies[random_movie].golden_globe):
            g_td.className = "bg-success"
        elif int(guess.golden_globe) < int(movies[random_movie].golden_globe):
            g_td.textContent = '> ' + g_td.textContent
        else:
            g_td.textContent = '< ' + g_td.textContent
    
    
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in movies.items():
        el = js.document.createElement("option")
        el.textContent = v.name
        el.value = k
        select.appendChild(el)

reset()
dropdown()
