def checks_for_digit(arg: list):
    arg_str = "".join(arg)
    print(arg_str)
    mistake = 0
    for element in arg_str:
        if not element.isdigit():
            mistake = 1
    if mistake == 1: return False
    else: return True


def checks_for_produkt(text):
    mistake = 0
    for element in text:
        if not element.isdigit() and not element in ["+", "-", "*", "/"]:
            mistake = 1
    if mistake == 1: return False
    else: return True

def check_for_logic(user_input:str):
    numbers = 0
    chars = 0
    minus = 0
    exponent = 0
    temp_exponent="" # требуется для определения возведения в степень
    temp_number = "" # набирает символы знака
    double_char = 0 #ловит дубли знаков кроме *
    for char in user_input:
        if char.isdigit():
            temp_number += char
            if double_char>0: double_char-=1
            if len(temp_exponent) == 2:
                exponent +=1
                temp_exponent=""
                double_char -=1
        elif char in ["+", "*", "/"]:
            chars+=1
            if temp_number:
                numbers+=1
                temp_number=""
            if char =="*":
                temp_exponent+=char
        elif char == "-":
            minus+=1
            if temp_number:
                numbers+=1
                temp_number=""
        if char in ["+", "*", "/", "-"]:
                double_char+=1
                try:
                    if user_input[user_input.index(char)+1] == "(":
                        double_char-=1
                except:
                    double_char*=1
    if temp_number: numbers+=1
    if chars > numbers and numbers <= (chars - minus - exponent) or double_char !=0:
        return False
    return True

print(check_for_logic("2+4+p"))