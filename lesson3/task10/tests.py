from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == '","':  # TODO: your condition here
        passed()
    elif placeholders[1] == "join":
        passed()
    elif placeholders[2] == "treasure_chest":
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call


