const rpc = require('zerorpc');

let client = new rpc.Client();
client.connect('tcp://127.0.0.1:4242');


client.invoke('echo', 'server ready', (error, res) => {
    if ( error || res !== 'server ready' )
        console.error(error);
    else
        console.log(res);
});

let btn = document.querySelector('#do_smth');

btn.addEventListener('click', () => {
    client.invoke('do_something', (error, res) => {
        console.log(res);
    });
});