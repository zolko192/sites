function calcAmount() {
    let price = 1000;
    let amountInput = document.querySelector("input[name='amount-input']");
    let amountNumber = parseInt(amountInput.value);

    showSumPrice(price, amountNumber);
}

function showSumPrice(price, amountNumber) {
    let showAmount = document.querySelector("span.show-amount");
    if (amountNumber > 10) {
        alert("Maximum 10 terméket vásárolhat!");
        return;
    }
    else if (amountNumber < 1) {
        alert("Minimum 1 terméket kell vásárolnia!");
    }
    else {
        let amount = amountNumber * price;
        showAmount.innerHTML = amount;
    }
}