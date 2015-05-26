def is_number_float(s):
    try:
        float(s)
        return True

    except ValueError:
        try:
            int(s)
            return True
        except:
            return False

        return False
