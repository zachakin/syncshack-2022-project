function toggle_light() {
    if (document.getElementById("stylesheet").getAttribute("href") === "./style.css") {
        document.getElementById("stylesheet").setAttribute("href", "./light.css");
    } else {
        document.getElementById("stylesheet").setAttribute("href", "./style.css");
    }
}