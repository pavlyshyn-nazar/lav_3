def decoder(text):
    """This function is created to decode encrypted   
    messages (in this repository is used to decrypt messages encrypted by function "encoder")"""
    text_new = ''
    digit = ''
    step1 = -1


    #Проходимося по кожному символу в тексті
    for a in text:
            #якщо цифра то збираємо в окрему стрінгу DIGIT
            range_ = ord(a)
            if range_ in range(48,58):
                digit = digit + a
                continue
            #якщо вжк не цифра і якщо DIGIT не пустий то зсовуємо його на 1 і запсуємо в результат і чистим DIGIT
            elif digit != "":
                    digit = int(digit)
                    digit = digit + step1
                    digit = str(digit)
                    text_new = text_new + digit
                    digit = ""

            #якщо буква то
            if range_ in range(97,122) or range_ in range(1072,1103) or range_ in range(65,90) or range_ in range(1040,1071) or range_ == "1168"or"1169"or"1028"or"1108"or"1031"or"1111": ###FOR LAST RANGE AND
                if a == "A":                                                                                                                                                              ###DESCIPRION ABOUT IT
                                                                                                                                                                                        ##YOU CAN SEE IN def_encoder.py
                    a = "Z"                                                                                                                                                             ##(also in this repository)
                    text_new = text_new + a
                    continue
                elif a == "a":
                    a = "z"
                    text_new = text_new + a
                    continue
                elif a == "А":
                    a = "Я"
                    text_new = text_new + a
                    continue
                elif a == "а":
                    a = "я"
                    text_new = text_new + a
                    continue
                else:
                    code_of_symbol = ord(a)
                    code_of_symbol += step1
                    a = chr(code_of_symbol)
                    text_new = text_new + a
                    continue
    #додаємо все з DIGIT якщо він не пустий в результат
    if digit != "":
        digit = int(digit)
        digit = digit + step1
        digit = str(digit)
        text_new = text_new + digit
    return text_new
help(decoder)
while True:
    abc_text = input()
    abc_text = decoder(abc_text)
    print(abc_text)
