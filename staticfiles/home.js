document.addEventListener("DOMContentLoaded", function () {
    const addToCartButtons = document.querySelectorAll(".add-to-cart");

    addToCartButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const productCard = this.closest(".product-card");
            const productName = productCard.querySelector(".product-details h2").innerText;
            const priceButtons = productCard.querySelectorAll(".price-button");
            const messageBox = productCard.querySelector(".message-box") || document.createElement("p");

            messageBox.classList.add("message-box");
            if (!productCard.contains(messageBox)) {
                productCard.appendChild(messageBox);
            }

            let selectedPrice = null;
            priceButtons.forEach(button => {
                if (button.classList.contains("selected")) {
                    selectedPrice = button.innerText;
                }
            });

            if (!selectedPrice) {
                messageBox.innerText = "Please select a price option before adding to cart.";
                messageBox.style.color = "red";
                return;
            }

            let cart = JSON.parse(localStorage.getItem("cart")) || [];
            cart.push({ name: productName, price: selectedPrice });
            localStorage.setItem("cart", JSON.stringify(cart));

            window.location.href = "{% url 'myapp:cart' %}";
        });
    });

    const priceButtons = document.querySelectorAll(".price-button");
    priceButtons.forEach(button => {
        button.addEventListener("click", function () {
            const parentCard = this.closest(".product-card");
            const buttonsInCard = parentCard.querySelectorAll(".price-button");

            buttonsInCard.forEach(btn => btn.classList.remove("selected"));
            this.classList.add("selected");

            const messageBox = parentCard.querySelector(".message-box");
            if (messageBox) {
                messageBox.innerText = "";
            }
        });
    });
});





