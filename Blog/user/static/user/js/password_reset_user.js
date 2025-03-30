
document.querySelector('input[name="password1"]').addEventListener('input',CheckPassword)
//document.querySelector('input[name="password2"]').addEventListener('input',CheckPassword)

function CheckPassword(){
    const password = this.value
    const error_pass = []
    const special_char = /[!#&@%${}^(),.?:|"<>*]/

    if (!/\d/.test(password)){
        error_pass.push("Au moins un chiffre")
    }
    if(!special_char.test(password)){
        error_pass.push("Au moins un caractère spécial")
    }
    if(password.length < 8){
        error_pass.push("Au moins 8 caractère")
    }
    const info_error = document.getElementById("info_error")
    if (error_pass.length > 0 ){
        info_error.innerHTML =error_pass.map(erro => `. ${erro}`).join("<br>")
        //info_error.textContent = error_pass.join(", ")
    }else{
        info_error.textContent = ""
    }
}