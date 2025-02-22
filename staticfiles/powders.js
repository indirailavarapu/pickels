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
