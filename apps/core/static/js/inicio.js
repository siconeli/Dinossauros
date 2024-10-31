   
// Modal de Delete
const modal = document.getElementById("modalDelete");
const openModalButton = document.getElementById("openModal");
const closeModalButton = document.querySelector(".close");
const deleteButton = document.getElementById("btn-excluir");
const formDelete = document.getElementById("formDelete");

openModalButton.onclick = function() {
    modal.style.display = "block";
};

closeModalButton.onclick = function() {
    modal.style.display = "none";
};

deleteButton.onclick = function () {
    formDelete.submit();
};

    