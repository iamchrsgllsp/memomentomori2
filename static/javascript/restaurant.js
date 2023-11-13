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
    console.log(leng);
    var index = Math.floor(Math.random() * leng); // Removed -1 and +1 to include the last element
    var selectedRestaurant = restaurant[index];
    
    res.innerHTML = `
        <div class="restaurant" id="restaurant">
            <p>${selectedRestaurant['Name']}</p>
            <img src="${selectedRestaurant['LogoUrl']}"><br><br>
            <button><a href="">Decline</a></button>
            <button><a href="${selectedRestaurant['Url']}">Accept</a></button>
        </div>`;
}
