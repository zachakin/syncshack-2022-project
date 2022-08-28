import random
import js
import math
import csv

# Class for each psycho
class psycho:
    def __init__(self, id_: int, name: str, start: int, lives: int, years: int, country: str, victims: int):
        self.id = id_
        self.name = name
        self.start = start
        self.lives = lives
        self.years = years
        self.country = country
        self.victims = victims

    
    def __str__(self):
        return f'Name: {self.name}\nSentence Start: {self.start}\nx Life Sentences: {self.lives}\n+ x years: {self.years}\nCountry: {self.country}\nVictims: {self.victims}'

# Populates the dictionary of psycho objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = psycho(j,i[0],i[1],i[2],i[3],i[4],i[5])
            output[j] = a
            j += 1
    return output

psychos = populate_options('./psychos.csv')

# Resets the game
def reset(*args):
    # Get new random number that represents key of element in dictionary
    r = list(range(len(psychos)+1))
    random_psycho = random.choice(r)
    # Store that random number in localStorage
    js.localStorage.setItem("random_psycho", random_psycho)

    # Store guesses remaining in localStorage
    js.localStorage.setItem("guesses_remaining_parole",8)
    
    # !!!!!!
    pyscript.write("count", str(psychos[random_psycho].name))

    # Reset count on frontend
    pyscript.write("count","8")

    # Store has_won_chem in localStorage
    js.localStorage.setItem("has_won_parole","False")
   
    # Reset table
    tb = js.document.getElementById("tb")
    tb.innerHTML = ""

    # Reset answer
    answer = js.document.getElementById("answer")
    answer.innerHTML = ""

tbody = Element("tb").element

# Compares guess to the random element
def compare_guess(*args):
    random_psycho = int(js.localStorage.getItem("random_psycho"))
    
    if js.localStorage.getItem("has_won_parole") == "True":
        return

    # Count Guesses
    guesses_total = int(js.localStorage.getItem("guesses_remaining_parole"))-1
    js.localStorage.setItem("guesses_remaining_parole",guesses_total)
    # Prints correct element
    if(guesses_total == 0):
        pyscript.write("answer", ("Correct answer: " + psychos[random_psycho].name))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = psychos[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")

    # self, id_: int, name: str, start: int, lives: int, years: int, country: str, victims: int):
    name_td = js.document.createElement("td")
    name_td.textContent = guess.name
    name_td.value = guess.name
    start_td = js.document.createElement("td")
    start_td.textContent = guess.start
    start_td.value = guess.start
    lives_td = js.document.createElement("td")
    lives_td.textContent = guess.lives
    lives_td.value = guess.lives
    years_td = js.document.createElement("td")
    years_td.textContent = guess.years
    years_td.value = guess.years
    country_td = js.document.createElement("td")
    country_td.textContent = guess.country
    country_td.value = guess.country
    victims_td = js.document.createElement("td")
    victims_td.textContent = guess.victims
    victims_td.value = guess.victims

    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(start_td)
    tr.appendChild(lives_td)
    tr.appendChild(years_td)
    tr.appendChild(country_td)
    tr.appendChild(victims_td)
    
    if guess.id == psychos[random_psycho].id:
        # Correct guess
        name_td.className = "bg-success"
        start_td.className = "bg-success"
        lives_td.className = "bg-success"
        years_td.className = "bg-success"
        country_td.className = "bg-success"
        victims_td.className = "bg-success"

    else:
        
        if int(guess.start) == int(psychos[random_psycho].start):
            start_td.className = "bg-success"
        elif int(guess.start) < int(psychos[random_psycho].start):
            start_td.textContent = '> ' + start_td.textContent
        else:
            start_td.textContent = '< ' + start_td.textContent
        
        if int(guess.lives) == int(psychos[random_psycho].lives):
            lives_td.className = "bg-success"
        elif int(guess.lives) < int(psychos[random_psycho].lives):
            lives_td.textContent = '> ' + lives_td.textContent
        else:
            lives_td.textContent = '< ' + lives_td.textContent

        if int(guess.years) == int(psychos[random_psycho].years):
            years_td.className = "bg-success"
        elif int(guess.years) < int(psychos[random_psycho].years):
            years_td.textContent = '> ' + years_td.textContent
        else:
            years_td.textContent = '< ' + years_td.textContent
        
        if guess.country == psychos[random_psycho].start:
            start_td.className = "bg-success"
        
        if int(guess.victims) == int(psychos[random_psycho].victims):
            victims_td.className = "bg-success"
        elif int(guess.victims) < int(psychos[random_psycho].victims):
            victims_td.textContent = '> ' + victims_td.textContent
        else:
            victims_td.textContent = '< ' + victims_td.textContent

    
        
    
    
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in psychos.items():
        el = js.document.createElement("option")
        el.textContent = v.name
        el.value = k
        select.appendChild(el)

reset()
dropdown()
