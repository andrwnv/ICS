const electron      = require('electron');
const browserWinow  = electron.BrowserWinowdow;
const app           = electron.app;

const path          = require('path');

let mainWindow = null;

const createWindow = () => {
    mainWindow = new browserWinow( { width: 1280, height: 720 } );
    mainWindow.loadURL( require('url').format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));

    // mainWindow.webContents.openDevTools();

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    app.quit();
});

app.on('activate', () => {
    if (mainWindow === null) 
        createWindow();
});