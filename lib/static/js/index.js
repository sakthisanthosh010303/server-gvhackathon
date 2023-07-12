/*
 * Author: Sakthi Santhosh
 * Created on: 23/04/2023
 */
let counter = 1;
let placeholderElement = document.getElementById("placeholder");

function getEvent() {
    fetch("/get_event")
    .then(response => response.json())
    .then(data => {
        let imageElement = document.getElementById("image-data");
        let imageDescriptionElement = document.getElementById("image-description");
        let tableBodyElement = document.getElementById("table-body");
        let actionLinkElement = document.createElement("a");
        let newRow = document.createElement("tr");
        let rowContent = [];

        actionLinkElement.className = "btn btn-primary";
        actionLinkElement.href = "http://www.google.com/maps/place/" + data.location;
        actionLinkElement.textContent = "View in Map";

        for (let i = 0; i < 5; i++)
            rowContent[i] = document.createElement("td");

        rowContent[0].textContent = counter++;
        rowContent[1].textContent = data.datetime;
        rowContent[2].textContent = data.device_id;
        rowContent[3].textContent = data.animal_class.charAt(0).toUpperCase() + data.animal_class.slice(1);
        rowContent[4].appendChild(actionLinkElement);

        for (let i = 0; i < 5; i++)
            newRow.appendChild(rowContent[i]);

        if (data.animal_class != "NA")
            rowContent[3].className = "text-danger";

        tableBodyElement.appendChild(newRow);
        imageElement.src = "data:image/png;base64," + data.image;
        imageDescriptionElement.textContent = data.datetime;
    })
    .catch(error => console.error(error))
}

setTimeout(function() {
    placeholderElement.remove();
}, 5000);
setInterval(getEvent, 5000);
