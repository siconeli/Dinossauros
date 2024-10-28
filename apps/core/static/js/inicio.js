document.addEventListener('DOMContentLoaded', function() {
    const rowsPerPage =7; // Define quantas linhas por página
    const table = document.getElementById("alunos").getElementsByTagName('tbody')[0];
    const rows = table.getElementsByTagName("tr");
    const totalRows = rows.length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);
    const paginationControls = document.getElementById("paginationControls");

    let currentPage = 1;

    function displayRows(startIndex, endIndex) {
        for (let i = 0; i < totalRows; i++) {
            rows[i].style.display = (i >= startIndex && i < endIndex) ? '' : 'none';
        }
    }

    function createPaginationButtons() {
        paginationControls.innerHTML = ""; // Limpa os botões anteriores
        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("button");
            button.innerText = i;
            button.addEventListener('click', function() {
                currentPage = i;
                displayRows((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage);
                updatePaginationControls();
            });
            paginationControls.appendChild(button);
        }
    }

    function updatePaginationControls() {
        const buttons = paginationControls.getElementsByTagName("button");
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].classList.remove('active');
            if (i === currentPage - 1) {
                buttons[i].classList.add('active');
            }
        }
    }

    // Exibe a primeira página ao carregar
    displayRows(0, rowsPerPage);
    createPaginationButtons();
    updatePaginationControls();
    
    
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
});
    