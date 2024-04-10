
function typed(button) {
    var n1 = document.getElementById("out").innerHTML;
    var ans = n1 + button

    document.getElementById("out").innerHTML = ans;
}

function addit() {
    num1 = Number(document.getElementById("out").innerHTML);
    operation = 'add'
    document.getElementById("out").innerHTML = '';
}

function subtraction() {
    num1 = Number(document.getElementById("out").innerHTML);
    opp = 'sub'
    document.getElementById("out").innerHTML = '';
}

function equals() {
    var n2 = Number(document.getElementById("out").innerHTML);
    if (opp == 'add'){
        var ans = num1 + n2;}
    else if (opp == 'sub'){
        var ans = num1 - n2;}
    else if (opp == 'mult'){
        var ans = num1 - n2;}
    else if (opp == 'div'){
        var ans = num1 - n2;}


    document.getElementById("out").innerHTML = ans;
}
