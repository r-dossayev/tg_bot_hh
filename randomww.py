# ----------------------------------LAB-2---------------------------------

import string


def cipher_vigenere(word, key, isDecrypt=False):
    letters = string.ascii_lowercase
    table = [[letters[(j + i) % 26] for j in range(26)] for i in range(26)]
    result = ""
    key_repeated = (key * (len(word) // len(key))) + key[:len(word) % len(key)]

    for i in range(len(word)):
        if word[i].isalpha():
            if isDecrypt:
                row = letters.find(key_repeated[i])
                col = table[row].index(word[i].lower())
                result += letters[col]
            else:
                row = letters.find(word[i].lower())
                col = letters.find(key_repeated[i])
                result += table[col][row]
        else:
            result += word[i]

    return result


data = "vigenere"
keyword = "english"
encrypt = cipher_vigenere(data, keyword)
print("encrypt result:", encrypt)

decrypt = cipher_vigenere(encrypt, keyword, isDecrypt=True)
print("decrypt result:", decrypt)

# viginere
# arip2 = ["а", "ә", "б", "в", "г", "ғ", "д", "е", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п",
#          "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "ъ", "ы", "і", "ь", "э", "ю", "я"]
#
#
# def valueIndexOfArray(a, arr):
#     for i in range(0, len(arr)):
#         if a == arr[i]:
#             return i


# def kazVigenere(word, key, encrypt=True):
#     key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
#     result = ""
#     for i in range(len(text)):
#         if encrypt:
#             cg = valueIndexOfArray(text[i], arip2)
#             cg2 = valueIndexOfArray(key_repeated[i], arip2) + 1
#         else:
#             cg = valueIndexOfArray(text[i], arip2) + 1
#             cg2 = valueIndexOfArray(key_repeated[i], arip2) + 1
#         # print(cg)
#         # print(cg)
#         if encrypt:
#             if cg > cg2:
#                 result += arip2[cg - cg2]
#                 # print(result)
#             elif cg < cg2:
#                 result += arip2[42 - (cg2 - cg) - 1]
#                 # print(result)
#             else:
#                 result += arip2[0]
#         else:
#             if cg + cg2 <= 42:
#                 result += arip2[cg + cg2 - 1]
#             else:
#                 result += arip2[cg + cg2 - 42]
#     return result
# #
# #
# a = kazVigenere("кушікасырапитеттімолбалтырымдықанатты", "абай", False)
# print(a)
# print(kazVigenere(a, "абай"))
# def kazVigenere(text, key, encrypt=True):
#     key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
#     result = ""
#     key_index = 0
#
#     for i in range(len(text)):
#         if text[i] in arip2:
#             if encrypt:
#                 cg = valueIndexOfArray(text[i], arip2)
#                 cg2 = valueIndexOfArray(key_repeated[key_index], arip2)
#             else:
#                 cg = valueIndexOfArray(text[i], arip2)
#                 cg2 = valueIndexOfArray(key_repeated[key_index], arip2)
#
#             key_index = (key_index + 1) % len(key)
#
#             if encrypt:
#                 result += arip2[(cg + cg2) % len(arip2)]
#             else:
#                 result += arip2[(cg - cg2) % len(arip2)]
#         else:
#             result += text[i]  # Add spaces or non-Kazakh characters as they are
#     return result
#
# text = "кушік асырап ит еттім ол балтырымды қанатты"
# encrypted_text = kazVigenere(text, "абай")
# print(encrypted_text)
# decrypted_text = kazVigenere(encrypted_text, "абай", False)
# print(decrypted_text)


# def kazVigenere2(text, key, encrypt=True):
#     key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
#     result = ""
#     index = 0
#     for i in range(len(text)):
#         if text[i] in arip2:
#             if encrypt:
#                 cg = valueIndexOfArray(text[i], arip2)
#                 cg2 = valueIndexOfArray(key_repeated[index], arip2) + 1
#             else:
#                 cg = valueIndexOfArray(text[i], arip2) + 1
#                 cg2 = valueIndexOfArray(key_repeated[index], arip2) + 1
#
#             index += 1
#
#             if index == len(key):
#                 index = 0
#
#             if encrypt:
#                 if cg > cg2:
#                     result += arip2[cg - cg2]
#                 elif cg < cg2:
#                     result += arip2[42 - (cg2 - cg) - 1]
#                 else:
#                     result += arip2[0]
#             else:
#                 if cg + cg2 <= 42:
#                     result += arip2[cg + cg2 - 1]
#                 else:
#                     result += arip2[cg + cg2 - 42]
#         else:
#             result += text[i]  # Add spaces or non-Kazakh characters as they are
#     return result
#
# text = "кушік асырап ит еттім ол балтырымды қанатты"
# encrypted_text = kazVigenere2(text, "абай")
# print(encrypted_text)
# decrypted_text = kazVigenere2(encrypted_text, "абай", False)
# print(decrypted_text)


# import random
#
# ans1 = "Это несомненно"
# ans2 = "Это определенно так"
# ans3 = "Без сомнения"
# ans4 = "Да - определенно"
# ans5 = "Вы можете на это положиться"
# ans6 = "Как я понимаю, да"
# ans7 = "Скорее всего, да"
# ans8 = "Перспективы хорошие"
# ans9 = "Да"
# ans10 = "признаки указывают на да"
# ans11 = "Ответить туманно, попробуйте еще раз"
# ans12 = "Спросите позже"
# ans13 = "Лучше не говорить вам сейчас"
# ans14 = "Сейчас предсказать невозможно"
# ans15 = "Сосредоточьтесь и спросите еще раз"
# ans16 = "Не рассчитывайте на это"
# ans17 = "Мой ответ отрицательный"
# ans18 = "Мои источники говорят нет"
# ans19 = "Прогноз не очень хороший"


# ans20 = "Очень сомнительно"
# answers = [ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15, ans16, ans17,
#            ans18, ans19, ans20]
# name = input("Введите свое имя: ")
# input(name + ",какой у вас вопрос по поводу Magic fortune ball?")
#
#
# def choiceAnswer(choice):
#     return answers[choice - 1]
#
#
# print("****************************")
# print("Magic fortune ball:", choiceAnswer(random.randint(1, 20)))
#
#
# def playAgain():
#     print('Хочешь задать  еще вопрос  (да или нет)')
#     return input().lower().startswith('д')
#
#
# while True:
#     if playAgain() == 1:
#         print("Задавай свой вопрос?")
#         input()
#
#         print("Magic fortune ball:", choiceAnswer(random.randint(1, 20)))
#     else:
#         break
