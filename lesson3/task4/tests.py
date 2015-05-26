from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    # placeholder = placeholders[0]
    if placeholders[0] == "":  # TODO: your condition here
        passed()
    elif placeholders[1] == "It eats you. Well, that was tasty!":
        passed()
    elif placeholders[2] == "def you_died(why):":
        passed()
    elif placeholders[3] == "why":
        passed()

    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call


