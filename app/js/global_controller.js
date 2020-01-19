// const zeroRPC = require('zerorpc');

class RPCNetworking
{
    constructor(name = "")
    {
        if (!!RPCNetworking.instance)
        {
            return RPCNetworking.instance;
        }
        
        RPCNetworking.instance = this;
        
        // this.client  = new zeroRPC.Client();
        this.address = 'tcp://127.0.0.1:4242';

        this.name = name;

        return this;
    }

    connect()
    {
        // this.client.connect(this.address);
    }

    disconnect()
    {
        // this.client.disconnect();
    }

    invoke(functionName, params, handler)
    {
        this.client.invoke(functionName, params, handler);
    }
}

let rpc = new RPCNetworking("asdsd")

module.exports.RPCNetworking = {
    RPCNetworking
}
// module.exports.RPCNetworking = new RPCNetworking();