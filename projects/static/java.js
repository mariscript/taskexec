const htmlEl = document.getElementsByTagName('html')[0];

const toggleTheme = (theme) => {
    htmlEl.dataset.theme = theme;
}

function tgl() {
    var darkswitch = document.getElementById("darkswitch");
    if (darkswitch.checked == true) {
        htmlEl.dataset.theme = 'dark';
    } else {
        htmlEl.dataset.theme = 'light';
    }
}



