
// SPINNERS CONTROL
$(document).ready(function() {

    const blockContent = document.getElementById('block-content');

    // SEARCH
    $('#btn-search').click(function() {
        // Mostrar el spinner
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // SEARCH
        $.get("currentUrl", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
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
