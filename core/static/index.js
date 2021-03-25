var formItem = document.querySelectorAll('.form-item')
formItem.forEach(element => {
    element.addEventListener('focus', () => {
        element.style.border = '1px solid black';
    })
    element.addEventListener('focusout', () => {
        if (element.value == ''){
            element.style.border = '1px solid red';
        } else {
            element.style.border = '1px solid rgb(175, 239, 177)';
        }
    })
})

var show = document.querySelector('#show');
var file = document.querySelector('input[type=file]')
file.addEventListener('input', () => {
    show.textContent = file.files[0].name
})
