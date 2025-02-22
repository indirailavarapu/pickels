// document.addEventListener("DOMContentLoaded", function () {
//     const addToCartButtons = document.querySelectorAll(".add-to-cart");

//     addToCartButtons.forEach(button => {
//         button.addEventListener("click", function () {
//             const productCard = this.closest(".card"); // Get the nearest product card
//             const productName = productCard.querySelector("h2").innerText; // Get product name
//             const selectedPriceButton = productCard.querySelector(".price-button.selected"); // Get selected price
//             const quantityInput = productCard.querySelector("#quantity-input"); // Get quantity
//             const messageBox = productCard.querySelector(".message-box") || document.createElement("p");

//             messageBox.classList.add("message-box");
//             if (!productCard.contains(messageBox)) {
//                 productCard.appendChild(messageBox);
//             }

//             if (!selectedPriceButton) {
//                 messageBox.innerText = "Please select a price option before adding to cart.";
//                 messageBox.style.color = "red";
//                 return;
//             }

//             const selectedPrice = selectedPriceButton.innerText; // Get selected price
//             const quantity = parseInt(quantityInput.value, 10); // Get quantity value

//             let cart = JSON.parse(localStorage.getItem("cart")) || [];

//             cart.push({
//                 name: productName,
//                 price: selectedPrice,
//                 quantity: quantity
//             });

//             localStorage.setItem("cart", JSON.stringify(cart));

//             window.location.href = "cart.html";
//         });
//     });

//     const priceButtons = document.querySelectorAll(".price-button");
//     priceButtons.forEach(button => {
//         button.addEventListener("click", function () {
//             const parentCard = this.closest(".card"); // Get the parent product card
//             const buttonsInCard = parentCard.querySelectorAll(".price-button");

//             buttonsInCard.forEach(btn => btn.classList.remove("selected"));

//             this.classList.add("selected");

//             const messageBox = parentCard.querySelector(".message-box");
//             if (messageBox) {
//                 messageBox.innerText = "";
//             }
//         });
//     });

//     document.querySelectorAll(".card").forEach(card => {
//         const decreaseButton = card.querySelector("#decrease");
//         const increaseButton = card.querySelector("#increase");
//         const quantityInput = card.querySelector("#quantity-input");

//         decreaseButton.addEventListener("click", function () {
//             let value = parseInt(quantityInput.value, 10);
//             if (value > 1) {
//                 quantityInput.value = value - 1;
//             }
//         });

//         increaseButton.addEventListener("click", function () {
//             let value = parseInt(quantityInput.value, 10);
//             quantityInput.value = value + 1;
//         });
//     });
// });




document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".options .option-btn").forEach(button => {
        button.addEventListener("click", function () {
            this.parentElement.querySelectorAll(".option-btn").forEach(btn => btn.classList.remove("selected"));
            this.classList.add("selected");
        });
    });

    document.querySelectorAll(".quantity-container").forEach(container => {
        let minusBtn = container.querySelector(".quantity-btn:first-child");
        let plusBtn = container.querySelector(".quantity-btn:last-child");
        let inputField = container.querySelector(".quantity-input");

        minusBtn.addEventListener("click", function () {
            let currentValue = parseInt(inputField.value, 10);
            if (currentValue > 1) {
                inputField.value = currentValue - 1;
            }
        });

        plusBtn.addEventListener("click", function () {
            let currentValue = parseInt(inputField.value, 10);
            inputField.value = currentValue + 1;
        });
    });

    document.querySelectorAll(".add-to-cart-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault(); 
            
            let productCard = this.closest(".papads-card");
            let productName = productCard.querySelector("h2").textContent;
            let selectedOption = productCard.querySelector(".option-btn.selected").textContent;
            let quantity = parseInt(productCard.querySelector(".quantity-input").value, 10);
            
            updateCartCounter(quantity);

        });
    });

    function updateCartCounter(quantity) {
        let cartCounter = document.querySelector("#cart-count");
        let currentCount = parseInt(cartCounter.textContent, 10) || 0;
        cartCounter.textContent = currentCount + quantity;
    }
});
