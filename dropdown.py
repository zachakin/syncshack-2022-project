import js
from populate_options import algos

select = Element("selectNumber").element

for i in algos:
    el = js.document.createElement("option")
    el.textContent = i[0]
    el.value = i[0]
    select.appendChild(el)