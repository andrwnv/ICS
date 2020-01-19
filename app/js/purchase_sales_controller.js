let RPCNetworking = require('./js/rpc_networking');

let network = new RPCNetworking();

function GoodsTableController(){
    this.table = document.getElementById('goods_table');
    this._appendRows();
}

GoodsTableController.prototype._createCell = function(cell, text, style){
    let tr = document.createElement('tr');                  
    cell.innerHTML = text;       
    cell.setAttribute('id', style);        
}

GoodsTableController.prototype._appendRows = function(){
    let row = this.table.insertRow(this.table.rows.length);

    for (var i = 0; i < this.table.rows[0].cells.length; i++) 
    {
        this._createCell(row.insertCell(i), i, 'goods_table_table_item');
    }
}

GoodsTableController.prototype.updateData = function(){
    network.invoke('update_goods', '', () => {

    });
}

let table_controller = new GoodsTableController();