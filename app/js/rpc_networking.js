const zeroRPC = require('zerorpc');

function RPCNetworking() {
    if ( typeof RPCNetworking.instance === 'object') {
        return RPCNetworking.instance;
    }

    RPCNetworking.instance = this;

    this.client = new zeroRPC.Client();
    this.address = 'tcp://127.0.0.1:4242';

    this.connect();
}

RPCNetworking.prototype.connect = function() {
    this.client.connect(this.address);
}

RPCNetworking.prototype.disconnect = function() {
    this.client.disconnect();
}

RPCNetworking.prototype.invoke = function(functionName, params, handler) {
    this.client.invoke(functionName, params, handler);
}

module.exports = RPCNetworking;