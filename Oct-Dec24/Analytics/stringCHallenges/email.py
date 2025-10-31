def parse_email(email_address):
    if not type(email_address) == str:
        return([])
    if email_address.find("@") == -1:
        return([])
    if email_address.find(".") == -1:
        return([])
    x = email_address.split("@", 1)
    if x[1].find("@") != -1:
        return([])
    if x[0] == '':
        return ([])
    firstHalf = list([x[0]])
    secondHalf = x[1]
    secondHalf = "".join(reversed(secondHalf))
    z = secondHalf.split(".", 1)
    if len(z) != 2:
        return([])
    z[0] = "".join(reversed(z[0]))
    z[1] = "".join(reversed(z[1]))
    z.reverse()
    y = firstHalf + z

    if not y[1] or not y[2]:
        return([])
    for i in y:
        if i.find(".") == 0:
            return([])

        if i.find(".") == len(i)-1:
            return([])
    return(y)


# Test Driven Development

def test(input, expected):
    if parse_email(input) == expected:
        print("Pass")
    else:
        print("Fail", parse_email(input), " != ", expected)


# Stage 1 tests
print("--- Stage 1 Tests ---")
test("test@example.com", ["test", "example", "com"])
test("user@simple.org", ["user", "simple", "org"])
test("name@website.net", ["name", "website", "net"])

# Stage 2 tests
print("\n--- Stage 2 Tests ---")
test("another.user@my-domain.co.uk", ["another.user", "my-domain.co", "uk"])
test("first.last@sub.example.net", ["first.last", "sub.example", "net"])
test("email.with.many.dots@very.long.domain.info", ["email.with.many.dots", "very.long.domain", "info"])
test("user-name@domain.com", ["user-name", "domain", "com"])  # Added test case with hyphen

# Stage 3 tests
print("\n--- Stage 3 Tests ---")
test("invalid_email", [])
test("no@tld", [])
test("multiple@@symbols.com", [])
test("@missing_username.com", [])
test("username@missing_dot", [])
test("user@domain", [])  # Missing TLD
test("user@.com", [])  # Empty domain
test("user@com", [])  # Missing dot before TLD
test("user.name@", [])  # Missing domain
test(123, [])  # Invalid input type
test(None, [])  # Invalid input type
test("user@example.", [])  # TLD cannot be empty
test(".user@example.com", [])  # Username cannot start with a dot
test("user.@example.com", [])  # Username cannot end with a dot
test("user@.example.com", [])  # Domain cannot start with a dot
test("user@example.com.", [])  # Domain cannot end with a dot