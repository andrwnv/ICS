const rpc = require('zerorpc');

let client = new rpc.Client();
client.connect('tcp://127.0.0.1:4242');

export {client};