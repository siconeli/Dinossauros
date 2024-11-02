document.addEventListener('DOMContentLoaded', function() {
    function attachModalEvents() {
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
    }

   // Função para iniciar o DataTables na tabela
   function initializeDataTable() {
    $('#listar-documentos').DataTable({
        destroy: true, // Permite reinicializar o DataTable
        responsive: true,
        ordering: true,
        searching: false,
        info: false,
        pageLength: 4,
        language: {
            decimal: "",
            emptyTable: "Nenhum documento",
            infoEmpty: "Ativos: 0",
            zeroRecords: "Nenhum documento",
            paginate: {
                first: "Primeiro",
                last: "Último",
                next: "Próximo",
                previous: "Anterior"
            },
            aria: {
                sortAscending: ": ordem crescente",
                sortDescending: ": ordem decrescente"
            }
        }
    });

    $('.dataTables_length').hide(); // Esconde a opção de selecionar número de registros por página
}

    // Inicializa os eventos do modal e o DataTables ao carregar a página
    attachModalEvents();
    initializeDataTable();

    // Reanexa os eventos e reinicializa o DataTables após o HTMX atualizar o DOM
    document.body.addEventListener('htmx:afterSwap', function () {
        // Destroi o DataTables se já estiver inicializado
        if ($.fn.DataTable.isDataTable('#listar-documentos')) {
            $('#listar-documentos').DataTable().destroy();
            $('#listar-documentos').empty(); // Limpa o conteúdo da tabela para evitar duplicação de linhas
        }
        
        // Adiciona um timeout para garantir que o DOM esteja completamente carregado antes de reinicializar
        setTimeout(() => {
            attachModalEvents();
            initializeDataTable();
        }, 100); // Ajuste o tempo se necessário
    });
});

