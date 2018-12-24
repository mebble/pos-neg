$('#input-form').submit(function(event) {
    const topic = $('#topic-input').val();
    const data = { topic };
    $.ajax({
        type: 'POST',
        url: '/pos-neg',
        data: JSON.stringify(data),
        success: function(response) {
            console.log(response);
        },
        contentType: 'application/json'
    });
    event.preventDefault();
    event.stopPropagation();
});
