document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os botões de abrir modal, botões de fechar modal, botões de excluir e formulários
    const openModalButtons = document.querySelectorAll(".openModal");
    const modals = document.querySelectorAll(".modalDelete");
    const closeModalButtons = document.querySelectorAll(".close");
    const deleteButtons = document.querySelectorAll(".btn-excluir");
    const forms = document.querySelectorAll(".formDelete");

    // Adiciona o evento de clique para abrir o modal correspondente
    openModalButtons.forEach((button, index) => {
        button.onclick = function() {
            modals[index].style.display = "block";
        };
    });

    // Adiciona o evento de clique para fechar o modal correspondente
    closeModalButtons.forEach((button, index) => {
        button.onclick = function() {
            modals[index].style.display = "none";
        };
    });

    // Adiciona o evento de clique para submeter o formulário de exclusão correspondente
    deleteButtons.forEach((button, index) => {
        button.onclick = function() {
            forms[index].submit();
        };
    });
});

