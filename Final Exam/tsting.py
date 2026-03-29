def get_size(gender, height):
    if gender == "F":
        if height < 150:
            return "S"
        elif 150 <= height <= 160:
            return "M"
        elif 161 <= height <= 170:
            return "L"
        elif height > 170:
            return "XL"
    elif gender == "M":
        if height < 160:
            return "S"
        elif 160 <= height <= 170:
            return "M"
        elif height > 170:
            return "L"
    else:
        return "Bad input, please make sure gender is entered as 'M' or 'F' and height is entered as an integer"