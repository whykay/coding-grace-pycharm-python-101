from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    # placeholder = placeholders[0]
    if placeholders[0] == "name":  # TODO: your condition here
        passed()
    elif placeholders[1] == "lower":
        passed()
    elif placeholders[2] == "name = alt_name":
        passed()
    elif placeholders[3] == "name = alt_name":
        passed()
    elif placeholders[4] == "name":
        passed()
    elif placeholders[5] == "player_name":
        passed()
    elif placeholders[6] == "get_player_name()":
        passed()
    elif placeholders[7] == "player_name":
        passed()
    else:
        failed()


if __name__ == '__main__':
    # run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


