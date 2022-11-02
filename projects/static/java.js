const htmlEl = document.getElementsByTagName('html')[0];
const darkswitch = document.getElementById("darkswitch");
console.log(darkswitch)
const toggleTheme = (theme) => {
    htmlEl.dataset.theme = theme;
}

function tgl() {
    if (darkswitch.checked == true) {
        localStorage.setItem('darkswitch', true);
        if (localStorage.getItem('darkswitch') == 'true')
            htmlEl.dataset.theme = 'dark';
    } else {
        htmlEl.dataset.theme = 'light';
        localStorage.setItem('darkswitch', false);
    }
}

if (localStorage.getItem('darkswitch') == 'true') {
    htmlEl.dataset.theme = 'dark';
    darkswitch.checked = true;


}
else {
    htmlEl.dataset.theme = 'light';
    darkswitch.checked = false;
}

