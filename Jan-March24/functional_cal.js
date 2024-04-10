var num1 = ""
var opp = ""

function typed(button) {
    var n1 = document.getElementById("out").innerHTML;
    var ans = n1 + button

    document.getElementById("out").innerHTML = ans;
}

function opperation(opp_function) {
    num1 = Number(document.getElementById("out").innerHTML);

    document.getElementById("out").innerHTML = '';

    opp = opp_function;
}

function add(n1, n2) {
    return n1 + n2;
}

function sub(n1, n2) {
    return n1 - n2;

}

function mul(n1, n2) {
    return n1 * n2;
}

function div(n1, n2) {
    return n1 / n2;

}

function equals() {
    var n2 = Number(document.getElementById("out").innerHTML);

    var ans = opp(num1, n2)

    document.getElementById("out").innerHTML = ans;
}




