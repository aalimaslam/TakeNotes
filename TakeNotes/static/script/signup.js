const $ = s => document.querySelector(s);
const password = $("#password")
const confirmPassword = $("#confirmPassword")
const form = $("form");
form.addEventListener("submit", (e)=>{
    if(password.value != confirmPassword.value){
        alert("Password Did Not Match");
        e.preventDefault()
        return false
    }
})