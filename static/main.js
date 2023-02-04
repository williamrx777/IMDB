const sinopse = document.querySelector(".info p");
const tituloSinopse = document.querySelector(".info h2");

tituloSinopse.addEventListener("click", function() {
  sinopse.style.display = sinopse.style.display === "none" ? "block" : "none";
});
