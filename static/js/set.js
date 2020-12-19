
function signup() {
    $('#sign-up').removeClass("sign-up").addClass("sign-up-2");
    $('#sign-in').removeClass("sign-in").addClass("sign-in-2");
    let btn = document.getElementById('sign-up-btn');
    let btn_2 = document.getElementById('sign-in-btn')
    btn.style.display = "none";
    btn_2.style.display = "";
}
function signin() {
    $('#sign-up').removeClass("sign-up-2").addClass("sign-up");
    $('#sign-in').removeClass("sign-in-2").addClass("sign-in");
    let btn = document.getElementById('sign-up-btn');
    let btn_2 = document.getElementById('sign-in-btn')
    btn.style.display = "";
    btn_2.style.display = "none";
}
// e.style.display = "";