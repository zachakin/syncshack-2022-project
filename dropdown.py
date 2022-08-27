import js
from populate_options import algos

select = Element("selectNumber").element

for k,v in algos.items():
    el = js.document.createElement("option")
    el.textContent = v.name
    el.value = k
    select.appendChild(el)