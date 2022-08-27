import random
import js
from populate_options import algos

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

reset()