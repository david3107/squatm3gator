socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    socket.emit('client_connected', {data: 'New client!'});
});

socket.on('results', function (data) {
    console.log(data);
});

socket.on('alert', function (data) {
    alert('Alert Message!! ' + data);
});

function json_button() {
    socket.send('{"message": "test"}');
    alert(1)
}

function alert_button() {
    socket.emit('alert_button', 'Message from client!')
}