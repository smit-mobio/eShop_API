from utils import common_function

def validate_phonenumber(phone):
    if phone == "":
        return True
    elif len(phone) != 10:
        return False
    else:
        for i in range(0, len(phone)):
            if phone[i] in common_function.All_CHARACTER:
                return False
            i += 1
        return True