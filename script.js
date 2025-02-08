document.getElementById("predict-btn").addEventListener("click", async function () {
    let inputData = {
        house_age: document.getElementById("house-age").value,
        distance_to_mrt: document.getElementById("distance-mrt").value,
        num_convenience_stores: document.getElementById("convenience-stores").value,
        latitude: document.getElementById("latitude").value,
        longitude: document.getElementById("longitude").value
    };

    let response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(inputData)
    });

    let result = await response.json();

    if (result.error) {
        document.getElementById("prediction").innerHTML = `❌ Error: ${result.error}`;
    } else {
        document.getElementById("prediction").innerHTML = `🔮 Predicted Price: ${result.predicted_price} per unit area`;
    }
});
