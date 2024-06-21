
const clock =document.getElementById('clock');

function updateTime (){

    const now= moment();
    const humanReadable = now.format('hh:mm:ssA');

    clock.textContent = humanReadable;

}


setInterval(updateTime,1000);
updateTime();
