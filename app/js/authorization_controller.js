let RPCNetworking = require('./js/rpc_networking');

let network = new RPCNetworking();

network.invoke('echo', 'server ready', (error, res, more) => {
    console.log(res);
});

let btn = document.querySelector('#login_button');

btn.addEventListener('click', () => {
    network.invoke('echo', 'do_something', (error, res, more) => {
        console.log(res);
    });
});
