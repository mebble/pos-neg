$('#input-form').submit(function(event) {
    const topic = $('#topic-input').val();
    const data = { topic };
    $.ajax({
        type: 'POST',
        url: '/pos-neg',
        data: JSON.stringify(data),
        success: function(response) {
            console.log(response);
            createChart(response.tweets);
        },
        contentType: 'application/json'
    });
    event.preventDefault();
    event.stopPropagation();
});

function createChart(tweets) {
    const ctx = $('#tweet-graph');
    const tweetChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Array(tweets.length),
            datasets: [{
                label: 'Tweets',
                data: tweets.map(t => t.favorite_count)
            }]
        }
    });
}
