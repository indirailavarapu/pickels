document.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".proceed-btn").addEventListener("click", function () {
      let searchQuery = document.querySelector(".search-input").value.trim().toLowerCase();
      
      let products = document.querySelectorAll(".product-card");

      products.forEach(product => product.style.display = "none");

      let found = false;
      products.forEach(product => {
          let productName = product.getAttribute("data-name").toLowerCase();
          if (productName.includes(searchQuery)) {
              product.style.display = "block";
              found = true;
          }
      });

      if (!found) {
          document.querySelector(".search-input").style.border = "2px solid red";
      } else {
          document.querySelector(".search-input").style.border = "1px solid #ccc";
      }
  });

  document.querySelector(".search-input").addEventListener("input", function () {
      this.style.border = "1px solid #ccc";
  });
});
