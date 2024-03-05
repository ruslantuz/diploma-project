var loginModal = document.querySelector('#loginModal'),
    registerModal = document.querySelector('#registerModal'),
    loginBtn = document.querySelector('#loginBtn');
    signupBtn = document.querySelector('#signupBtn');
    
function x () {
    this.parentElement.parentElement.style.display = "none";
    scrollUnlock();
}
function scrollLock(){
  $('body').css('overflow', 'hidden');
}
function scrollUnlock(){
  $('body').css('overflow', '');
}

loginBtn.onclick = function () {
  loginModal.style.display = "block";
  closeBtn = loginModal.querySelector('.close-btn');
  scrollLock();
  closeBtn.onclick = x;
}

signupBtn.onclick = function () {
  registerModal.style.display = "block";
  closeBtn = registerModal.querySelector('.close-btn');
  scrollLock();
  closeBtn.onclick = x;
}

window.onclick = function (e) {
    if (e.target.className === 'modal-cont'){
        e.target.style.display = 'none';
        scrollUnlock();
    }
}
window.onkeydown = function (e) {
  if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27){
    $('.modal-cont').css('display','none');
    scrollUnlock();
  }
}