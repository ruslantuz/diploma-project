const iconMenu = document.getElementById('iconMenu')
const navigation = document.getElementById('navigation')
const login = document.querySelector('.login-wrap')
const heroWrap = document.getElementById('heroWrap')
const header = document.getElementById('headerId')

iconMenu.addEventListener('click', ()=> {
	navigation.classList.toggle('hide');
    login.classList.toggle('hide');
    header.classList.toggle('burger-clicked');
    iconMenu.classList.toggle("active");
})

