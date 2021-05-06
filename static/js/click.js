

let elements = document.querySelectorAll('.cell');
elements.forEach(function (elem) {
    elem.onclick = function () {
        if (document.getElementById('first').innerHTML == '') {
            document.getElementById('first').innerHTML = this.childNodes[1].innerHTML            
        } else {
            document.getElementById('second').innerHTML = this.childNodes[1].innerHTML
        }
    }
    elem.onmouseover = function () {
        elem.style.borderColor = 'red'
    }
    elem.onmouseout = function () {
        elem.style.borderColor = 'black'
    }
});

let button = document.querySelector('button');
button.onclick = function () {
    document.getElementById('first').innerHTML = ''
    document.getElementById('second').innerHTML = ''
    document.getElementById('answer').innerHTML = ''
}

