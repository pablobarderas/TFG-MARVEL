
// SPINNERS CONTROL
$(document).ready(function() {

    const blockContent = document.getElementById('block-content');
    
    // SEARCH CLICK
    $('#btn-search').click(function() {
        // Mostrar el spinner
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // SEARCH
        $.get("{% url 'search' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            blockContent.removeClass('visually-hidden');
            $('#spinners').addClass('visually-hidden');
        });
    });

    // CHARACTER CLICK
    $('#characters a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET CHARACTER
        $.get("{% url 'character' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });


    // COMIC CLICK
    $('#comics a').click( function() {

        console.log("trocolitos");

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET COMIC
        $.get("{% url 'comic' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });


    // EVENT CLICK
    $('#events a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET EVENT
        $.get("{% url 'event' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });


    // SERIE CLICK
    $('#series a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET SERIE
        $.get("{% url 'serie' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });

    // SERIE CLICK
    $('#series a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET SERIE
        $.get("{% url 'serie' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });


    // CREATOR CLICK
    $('#creators a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // SEARCH
        $.get("{% url 'creator' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });


    // STORIES CLICK
    $('#stories a').click( function() {

        // SHOW SPINNER
        blockContent.classList.add('visually-hidden');
        $('#spinners').removeClass('visually-hidden');

        // GET STORIES
        $.get("{% url 'story' %}", function() {
            // Ocultar el spinner cuando se obtienen los datos
            $('#spinners').addClass('visually-hidden');
            blockContent.removeClass('visually-hidden');
        });
    });

  });

