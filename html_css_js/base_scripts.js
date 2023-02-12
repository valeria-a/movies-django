
intervalID = -1

function displayDate(elementId) {
    document.getElementById(elementId).innerHTML = Date()
}


function displayDateNew(pId, btnId) {
    // change html content
    document.getElementById(pId).innerHTML = Date()

    // change attribute
    document.getElementById(btnId).style.visibility = "visible"
    
    // change CSS
    h2_elements = document.getElementsByTagName('h2')

    // for i in range()
    //len(l)
    //l.length
    //python: num = 65
    //js: num = 65 | let num = 65 | const num = 65 | var num = 65
    for (i = 0; i < h2_elements.length; i++) {
        element = h2_elements[i];
        element.style.color = "purple"
    }

    intervalID = setInterval(displayDate, 1000, 'demo');

}



function stopRefresh() {
    if (intervalID != null) {
        clearInterval(intervalID)
    }
}

function duplicateText(event) {
    document.getElementById('user_text').innerHTML = value
}
