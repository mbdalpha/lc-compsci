function go(){

    var fname = "Bob"
    var sname = "Byrne"
    var phone = 0872648987

    print(fname + " " + sname + ", " + phone)

    var john_fname = "John"
    var john_sname = "Murphy"
    var john_phone = 324234

    var staff = [fname, sname, phone, john_fname, john_sname, john_phone]

    print(staff[3] + " " + staff[4] + ", " + staff [5])

    print("classtype lesson")

    //Array Method
    var bob = [fname, sname, phone]
    var john = [john_fname, john_sname, john_phone]

    var customers = [
        bob,
        john,
        ["Eoin", "OC", 2454]

    ]

    print(customers[2][0] + " " + customers[2][1] + ", " + customers [2][1])


    //DIctionary Method

    var tod ={
    fname: "Tod",
    sname: "Doyle",
    phone: 4721032809
    }

    print(tod.fname + " " + tod.sname + ", " + tod.phone)

    var people = [
        tod,
        {
            name: {
                first: "Anne",
                second: "Doyle",
            },
            phone: 47591409
        }
    ]

    print(people[1].fname)

}