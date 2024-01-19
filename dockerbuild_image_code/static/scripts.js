function displayPokemon(data) {
    document.getElementById("error").style.display = "none";
    document.getElementById("pokemon-info").style.display = "block";
    document.getElementById("name").textContent = data.name;
    document.getElementById("weight").textContent = data.weight;
    document.getElementById("height").textContent = data.height;
    document.getElementById("types").textContent = data.types.join(", ");
    document.getElementById("abilities").textContent = data.abilities.join(", ");
    document.getElementById("sprite").src = data.sprite;
    
    const statsList = document.getElementById("stats-list");
    statsList.innerHTML = "";
    for (const [statName, statValue] of Object.entries(data.stats)) {
        const listItem = document.createElement("li");
        listItem.textContent = `${statName}: ${statValue}`;
        statsList.appendChild(listItem);
    }
}

function displayError() {
    document.getElementById("error").style.display = "block";
    document.getElementById("pokemon-info").style.display = "none";
}

document.getElementById("pokemon-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const pokemonName = document.getElementById("pokemon-name").value;
    fetch("/pokemon/" + pokemonName)
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                displayError();
            } else {
                displayPokemon(data);
            }
        });
});
