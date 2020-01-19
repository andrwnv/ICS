const globalController = require('/home/andrew/Desktop/ICS/app/js/global_controller');

globalController.client.invoke('echo', 'server ready', (error, res, more) => {
    console.log(res);
});

let btn = document.querySelector('#login_button');

btn.addEventListener('click', () => {
    globalController.client.invoke('echo', 'do_something', (error, res, more) => {
        console.log(res);
    });
});