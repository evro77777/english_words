from random import randint, shuffle
import openpyxl


def word_and_answer_options(num_opt=4):
    book = openpyxl.open("reg/static/reg/data/english_words.xlsx", read_only=True)
    sheet = book.active
    row = randint(1, sheet.max_row)
    answer_options = []
    english_word = sheet[row][0].value
    right_answer = sheet[row][1].value
    answer_options.append(right_answer)
    for i in range(num_opt - 1):

        answer_options.append(sheet[randint(1, sheet.max_row)][1].value)
    shuffle(answer_options)
    return {'english_word': english_word,
            'right_answer': right_answer,
            'answer_options': answer_options}
