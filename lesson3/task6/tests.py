from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    # placeholder = placeholders[0]

    if placeholders[0] == "for treasure in treasure_chest:":  # TODO: your condition here
        passed()
    elif placeholders[1] == "treasure":
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


