import random
import js
import math
import csv

# Class for each veggie
class veggie:
    def __init__(self, id_: int, name: str, calories: float, carbs: float, fiber: float, sugar: float, fat: float, protein: float):
        self.id = id_
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.fiber = fiber
        self.sugar = sugar
        self.fat = fat
        self.protein = protein
    
    def __str__(self):
        return f'Name: {self.name}\nCalories: {self.calories}\nCarbs: {self.carbs}\nFiber: {self.fiber}\nSugar: {self.sugar}\nFat: {self.fat}\nProtein: {self.protein}'

# Populates the dictionary of veggie objects
def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = veggie(j,i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            output[j] = a
            j += 1
    return output

veggies = populate_options('./veggies.csv')

# Resets the game
def reset(*args):
    # Get new random number that represents key of element in dictionary
    r = list(range(len(veggies)+1))
    random_veggie = random.choice(r)
    # Store that random number in localStorage
    js.localStorage.setItem("random_veggie", random_veggie)

    # Store guesses remaining in localStorage
    js.localStorage.setItem("guesses_remaining_chem",8)
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

# Compares guess to the random veggie
def compare_guess(*args):
    random_veggie = int(js.localStorage.getItem("random_veggie"))
    
    if js.localStorage.getItem("has_won_chem") == "True":
        return

    # Count Guesses
    guesses_total = int(js.localStorage.getItem("guesses_remaining_chem"))-1
    js.localStorage.setItem("guesses_remaining_chem",guesses_total)
    # Prints correct veggie
    if(guesses_total == 0):
        pyscript.write("answer", ("Correct answer: " + veggies[random_veggie].name))
    if(guesses_total < 0):
        return
    guesses_string = str(guesses_total)
    pyscript.write("count", guesses_string)
    
    # Get guess selection
    guess = veggies[int(Element("selectNumber").element.value)]

    # Create row for table
    tr = js.document.createElement("tr")
    # name, calories, carbs, fiber, sugar, fat, protein

    # Add columns for table
    name_td = js.document.createElement("td")
    name_td.textContent = guess.name
    name_td.value = guess.name
    cal_td = js.document.createElement("td")
    cal_td.textContent = guess.calories
    cal_td.value = guess.calories
    carb_td = js.document.createElement("td")
    carb_td.textContent = guess.carbs
    carb_td.value = guess.carbs
    fib_td = js.document.createElement("td")
    fib_td.textContent = guess.fiber
    fib_td.value = guess.fiber
    sug_td = js.document.createElement("td")
    sug_td.textContent = guess.sugar
    sug_td.value = guess.sugar
    fat_td = js.document.createElement("td")
    fat_td.textContent = guess.fat
    fat_td.value = guess.fat
    pro_td = js.document.createElement("td")
    pro_td.textContent = guess.protein
    pro_td.value = guess.protein



    # Add columns to row
    tr.appendChild(name_td)
    tr.appendChild(cal_td)
    tr.appendChild(carb_td)
    tr.appendChild(fib_td)
    tr.appendChild(sug_td)
    tr.appendChild(fat_td)
    tr.appendChild(pro_td)
    
    if guess.id == veggies[random_veggie].id:
        # Correct guess
        name_td.className = "bg-success"
        cal_td.className = "bg-success"
        carb_td.className = "bg-success"
        fib_td.className = "bg-success"
        sug_td.className = "bg-success"
        fat_td.className = "bg-success"
        pro_td.className = "bg-success"

    else:
        if float(guess.calories) == float(veggies[random_veggie].calories):
            cal_td.className = "bg-success"
        elif float(guess.calories) < float(veggies[random_veggie].calories):
            cal_td.textContent = '> ' + cal_td.textContent
        else:
            cal_td.textContent = '< ' + cal_td.textContent

        if float(guess.carbs) == float(veggies[random_veggie].carbs):
            carb_td.className = "bg-success"
        elif float(guess.carbs) < float(veggies[random_veggie].carbs):
            carb_td.textContent = '> ' + carb_td.textContent
        else:
            carb_td.textContent = '< ' + carb_td.textContent
        
        if float(guess.fiber) == float(veggies[random_veggie].fiber):
            fib_td.className = "bg-success"
        elif float(guess.fiber) < float(veggies[random_veggie].fiber):
            fib_td.textContent = '> ' + fib_td.textContent
        else:
            fib_td.textContent = '< ' + fib_td.textContent
        
        if float(guess.sugar) == float(veggies[random_veggie].sugar):
            sug_td.className = "bg-success"
        elif float(guess.sugar) < float(veggies[random_veggie].sugar):
            sug_td.textContent = '> ' + sug_td.textContent
        else:
            sug_td.textContent = '< ' + sug_td.textContent
        
        if float(guess.fat) == float(veggies[random_veggie].fat):
            fat_td.className = "bg-success"
        elif float(guess.fat) < float(veggies[random_veggie].fat):
            fat_td.textContent = '> ' + fat_td.textContent
        else:
            fat_td.textContent = '< ' + fat_td.textContent
        
        if float(guess.protein) == float(veggies[random_veggie].protein):
            pro_td.className = "bg-success"
        elif float(guess.protein) < float(veggies[random_veggie].protein):
            pro_td.textContent = '> ' + pro_td.textContent
        else:
            pro_td.textContent = '< ' + pro_td.textContent
        
    tbody.appendChild(tr)

# Populates the menu of available guesses
def dropdown():
    select = Element("selectNumber").element

    for k,v in veggies.items():
        el = js.document.createElement("option")
        el.textContent = v.name
        el.value = k
        select.appendChild(el)

reset()
dropdown()
