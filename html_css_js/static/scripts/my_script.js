// function switchColor(elem_id) {
//     elem = document.getElementById(elem_id)
//     currClass = elem.className
//     console.log('current class:', currClass)
//     if (currClass == 'text-primary') {
//         nextClass = 'text-info'
//     } else {
//         nextClass = 'text-primary'
//     }
//     // Note: The class is an HTML Attribute, while the className is a DOM Property.
//     elem.setAttribute('class', nextClass)

// }

function switchBtnColor(e) {
    elem = e.currentTarget
    currClassList = elem.classList
    console.log('current class:', currClassList)
    if (currClassList.contains('btn-primary')) {
        nextClass = 'btn-info'
        curClass = 'btn-primary'
    } else {
        nextClass = 'btn-primary'
        curClass = 'btn-info'
    }
    // https://developer.mozilla.org/en-US/docs/Web/API/Element/classList
    currClassList.replace(curClass, nextClass)

}