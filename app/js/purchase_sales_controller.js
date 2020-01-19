// const globalController = require('/home/andrew/Desktop/ICS/app/js/global_controller');

class GoodsTableController
{
    constructor()
    {
        // this.globalController = require('/home/andrew/Desktop/ICS/app/js/global_controller');
        this.table = document.getElementById('goods_table');
        this._appendRows();
    }

    _createCell(cell, text, style) 
    {
        let tr = document.createElement('tr');                  
        cell.innerHTML = text;       
        cell.setAttribute('id', style);        
    }

    _appendRows()
    {        
        let row = this.table.insertRow(this.table.rows.length);

        for (var i = 0; i < this.table.rows[0].cells.length; i++) 
        {
            this._createCell(row.insertCell(i), i, 'goods_table_table_item');
        }
    }

}

let table_controller = new GoodsTableController();