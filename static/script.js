$(document).ready(function(){
    $('#birthdayButton').click(function(){
        $.ajax({
            url: '/birthday',
            method: 'GET',
            success: function(response) {
                $('#message').html(response.message); // Usando .html() para preservar a formatação
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});