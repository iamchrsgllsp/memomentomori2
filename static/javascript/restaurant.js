function hamburger() {
    var header = document.getElementById("header");
    var menu = document.getElementById("menu");

    if (header.style.visibility == "hidden") {
        header.style.visibility = "visible"
    }
    else {
        header.style.visibility = "hidden";


    }
}

function getRestaurant(restaurant) {
    var res = document.getElementById("selected");
    var leng = restaurant.length;
    var index = Math.floor(Math.random() * leng); // Removed -1 and +1 to include the last element
    var selectedRestaurant = restaurant[index];
    var accept1 = selectedRestaurant['Name'];
    
    res.innerHTML = `
        <div class="restaurant" id="restaurant">
            <p id="sr">${selectedRestaurant['Name']}</p>
            <p id="rid">${selectedRestaurant['Id']}</p>
            <img src="${selectedRestaurant['LogoUrl']}"><br><br>
            <div>
            <button><a href="">Decline</a></button>
            <button id="accept" onclick='acceptedRestaurant();'>Accept</button>
            </div>
        </div>`;
}
function acceptedRestaurant() {
    console.log("hey")
    console.log(sr.innerHTML)
    console.log(rid.innerHTML)
    alert("You have chosen " + sr.innerHTML)
    fetch("http://127.0.0.1:5000/match", {
  method: "POST",
  body: JSON.stringify({
    userId: 1,
    title: rid.innerHTML,
  }),
  headers: {
    "Content-type": "application/json"
  }
}).then((response) => response.json())
.then((json) => console.log(json));
}
