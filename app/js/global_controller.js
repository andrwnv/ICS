const rpc = require('zerorpc');

var client = new rpc.Client();
client.connect('tcp://127.0.0.1:4242');

module.exports.client = client;