// Función para obtener CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie("csrftoken");

// Función para eliminar producto vía AJAX
document.querySelectorAll(".eliminar-btn").forEach((boton) => {
  boton.addEventListener("click", function () {
    const id = this.dataset.id;
    const fila = this.closest("tr");

    if (confirm("¿Seguro que deseas eliminar este producto?")) {
      fetch(`/eliminar_producto/${id}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then((res) => {
          if (!res.ok) throw new Error("Error al eliminar producto");
          return res.json();
        })
        .then((data) => {
          alert(data.mensaje);
          fila.remove(); // eliminar la fila del DOM
        })
        .catch((err) => {
          console.error(err);
          alert("Error al eliminar producto");
        });
    }
  });
});