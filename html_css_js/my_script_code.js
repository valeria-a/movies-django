function showAlert() {
    window.alert("You clicked on button!")
}

async function getMessageFromKanye(id_to_change) {
    let response = await fetch("https://api.kanye.rest");
    let message = await response.json()
    console.log("You've got a message ", message)
    document.getElementById(id_to_change).innerHTML = message.quote
  }