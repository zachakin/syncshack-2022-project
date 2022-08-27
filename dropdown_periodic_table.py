import js
from populate_options_chemle import periodic_table

select = Element("selectNumber").element

for k,v in periodic_table.items():
    el = js.document.createElement("option")
    el.textContent = v.name
    el.value = k
    select.appendChild(el)