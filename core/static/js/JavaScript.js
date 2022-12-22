let btn = document.querySelector('.fa-eye')

btn.addEventListener('click', ()=>{
    let inputSenha = document.querySelector('#senha')

    if(inputSenha.getAttribute('type') == 'password'){
        inputSenha.setAttribute('type', 'text')
    } else {
        inputSenha.setAttribute('type', 'password')
    }
});

let btnSenha = document.querySelector('#verSenha')

btn.addEventListener('click', ()=>{
    let inputVerSenha = document.querySelector('#verSenha')

    if(inputVerSenha.getAttribute('type') == 'password'){
        inputVerSenha.setAttribute('type', 'text')
    } else {
        inputVerSenha.setAttribute('type', 'password')
    }
});

let btnConfirm = document.querySelector('#verConfirmSenha')

btnConfirm.addEventListener('click', ()=>{
    let inputConfirSenha = document.querySelector('#ConfirmSenha')

    if(inputConfirSenha.getAttribute('type') == 'password'){
        inputConfirSenha.setAttribute('type', 'text')
    } else {
        inputConfirSenha.setAttribute('type', 'password')
    }
});


