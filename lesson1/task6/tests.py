from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    # placeholder = placeholders[0]
    print(placeholders)
    print(placeholders[0].isalpha())
    print(type(placeholders[1]))
    if placeholders[0].isalpha() and placeholders[1].isalpha():  # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


