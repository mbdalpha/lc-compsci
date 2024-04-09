
function do_n_times(n, fun) {
    for (var i = 0; i < n; i = i + 1) {
        fun(i);
    }
}

function hello(val) {
    print("Hello World!" + val);
}

function go() {
    do_n_times(10, hello);


    do_n_times(5, (val) => {
        print("Hi" + val);
    });
}