const profilImage = document.querySelector(".profil_image")
const dropDown = document.querySelector(".drop_down")
profilImage.addEventListener('click',()=>{dropDown.classList.toggle('disp')})
        

const body = document.querySelector("body")
const message_info = document.querySelector(".message")

body.addEventListener("click",
    ()=>{
        message_info.style.display="none"
    }
)