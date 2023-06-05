
// SPINNERS CONTROL
$(document).ready(function() {

    // SEARCH
    $('#btn-search').click(function() {
        // Mostrar el spinner
        $('#spinners').removeClass('visually-hidden');
    
        // SEARCH
        $.get("{% url 'search' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
        });
    });

    // CHARACTER
    

  });
