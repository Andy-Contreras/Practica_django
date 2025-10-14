const buscador = document.getElementById("buscar");
const listado = document.querySelectorAll(".table tbody tr");

buscador.addEventListener("input", () => {
  const valorBuscador = buscador.value.toLowerCase().trim();
  listado.forEach((list) => {
    const nombre = list.querySelector("td:nth-child(1)").textContent.toLowerCase();

    if (nombre.includes(valorBuscador)) {
      list.style.display = "";
    } else {
      list.style.display = "none";
    }
  });
});
