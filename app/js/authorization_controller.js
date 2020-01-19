import {client} from 'global_variables';

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