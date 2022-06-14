  $(function () {
    $("#dt_colaboradores").DataTable({
      "responsive": true, "lengthChange": false, "autoWidth": false,
      "buttons": ["csv", "excel", "pdf", "print", "colvis"],
      lengthMenu: [5, 10],
        "language": {

                   "sEmptyTable": "Nenhum registro encontrado",
                   "sInfo": "Mostrando de _START_ à _END_ de um total de _TOTAL_ registros",
                   "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
                   "sInfoFiltered": "(Filtrados de _MAX_ registros)",
                   "sInfoPostFix": "",
                   "sInfoThousands": ".",
                   "sLengthMenu": "Mostrando _MENU_ resultados por página",
                   "sLoadingRecords": "Carregando...",
                   "sProcessing": "Processando...",
                   "sZeroRecords": "Nenhum registro encontrado",
                   "sSearch": "Pesquisar na Lista:",
                   "oPaginate": {
                       "sNext": "Próximo",
                       "sPrevious": "Anterior",
                       "sFirst": "Primeiro",
                       "sLast": "Último"
                   },
                   "oAria": {
                       "sSortAscending": ": Ordenar colunas de forma ascendente",
                       "sSortDescending": ": Ordenar colunas de forma descendente"
                   }

        }
    }).buttons().container().appendTo('#dt_colaboradores_wrapper .col-md-6:eq(0)');
  });





