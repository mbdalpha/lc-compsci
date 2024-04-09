function add() {
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;
    var ans = Number(n1) + Number(n2)

    document.getElementById("out").innerHTML = ans;
}

function red(){
    document.getElementById("out").style.color = "red";
}