let screen = window.screen.width
console.log(screen)
let text = document.querySelectorAll('.content__text')
for( let i of text){
    let lenText = i.innerText.length
    if (screen < 500 && screen>375){
        i.innerText = i.innerText.slice(0,100)+"..."
    }else if(screen < 380){
        i.innerText = i.innerText.slice(0,190)+"..."
    }else{
        i.innerText = i.innerText.slice(0,500)+"..."
    }
}
