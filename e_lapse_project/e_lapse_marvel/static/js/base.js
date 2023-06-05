
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

  });

/*
  $(window).on('load', function() {
       // Mostrar el spinner
       $('#spinners').removeClass('visually-hidden');

        const currentUrl = window.location;
        console.log(currentUrl.pathname);

       // Realizar la solicitud GET
       $.get(currentUrl, function() {
           // Ocultar el spinner cuando se obtienen los datos
           $('#spinners').addClass('visually-hidden');
       });
  });

  */
