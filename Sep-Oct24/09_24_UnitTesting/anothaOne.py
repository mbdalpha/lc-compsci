from nextstupidmfingfile import validate

# Tests
def test_valid_input():
    # Input "a"
    # Expect result: True
    v = validate_input("a")

    return v is True


def test_empty_input():
    # Input ""
    # Expect result: False
    v = validate_input("")

    return v is False


def test_too_many_inputs():
    # Input "ab"
    # Expect result: False
    v = validate_input("ab")

    return v is False


def test_non_letter_inputs():
    # Input "3"
    # Expect result: False
    v = validate_input("3")

    return v is False


def test_uppercase_inputs():
    # Input "A"
    # Expect result: False
    v = validate_input("A")

    return v is False


def test_runner(tests):
    print("Running", len(tests), "tests")
    failed = 0
    for test in tests:
        result = eval(test)()
        if result is False:
            print(test, "failed")
            failed += 1

    if failed == 0:
        print("All tests passed")
    else:
        print(failed, "failure(s)")


test_runner(["test_valid_input",
             "test_empty_input",
             "test_too_many_inputs",
             "test_non_letter_inputs",
             "test_uppercase_inputs"])