from common_function import All_CHARACTER

def validate_phonenumber(phone):
    if phone == "":
        return True
    elif len(phone) != 10:
        raise("Please enter a valid phone number!")
    else:
        for i in range(0, len(phone)):
            if phone[i] in All_CHARACTER:
                raise ("Please enter a valid phone number!")
            i += 1
        return True