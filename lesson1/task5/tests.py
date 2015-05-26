from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from cg_utils import is_number_float

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]

    if is_number_float(placeholder):
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


