from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, shuffle
from time import sleep

app = QApplication([])

from card_window import *
from main_window import *
card_win.setWindowTitle("Memory card")

card_win.setLayout(card_layout)

#клас з питаннями
class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.is_asking = True
        self.count_ask = 0
        self.count_right = 0

    #def get_right(self):
    #    self.count_ask += 1
    #    self.count_right += 1
    #
    #
    #def get_wrong(self):
    #    self.count_ask += 1

count_ask = 0
count_right = 0  
#сворення об'єктів запитань
q1 = Question("Апельсин", "orange", "apple", "pineapple", "cucumber")
q2 = Question("Знати", "know", "like", "be", "smoke")
q3 = Question("Купити", "buy", "think", "love", "sociable")
q4 = Question("Машина", "car", "bike", "flash", "bicycle")
#списки з запитаннями та кнопками 
radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]
questions = [q1, q2, q3, q4]
#створення функцій для питань
def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_correct.setText(cur_quest.answer)

    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.wrong_ans1)
    radio_buttons[1].setText(cur_quest.wrong_ans2)
    radio_buttons[2].setText(cur_quest.wrong_ans3)
    radio_buttons[3].setText(cur_quest.answer)


new_question()


def check():
    global count_ask, count_right
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lbl_correct.text():
                count_ask += 1
                count_right += 1
                lbl_result.setText("Правильно")
                answer.setChecked(False)
                break
    else:
        lbl_result.setText("Не правильно!")
        count_ask += 1
    RadioGroup.setExclusive(True)
#функція яка перемикає питання 
def switch_screen():
    if btn_ok.text() == "Відповісти":
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_ok.setText("Наступне запитання")
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_ok.setText("Відповісти")
#функція яка зупиняє програму на деякий час       
def rest():
    card_win.hide()
    n = box_min.value() * 60
    sleep(n)
    card_win.show()

def back_menu():
    if count_ask == 0:
        c = 0
    else:
        c = (count_right/count_ask) * 100

    text = f"Всього вдіповідей: {count_ask}\n" \
           f"Правильних відповідей: {count_right}\n" \
           f"Успішність: {round(c, 2)}%"
    lbl_stat.setText(text)

    card_win.hide()
    main_win.show()

def to_card():
    main_win.hide()
    card_win.show()
    
def clear():
    le_quest.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def add_question():
    new_q = Question(le_quest.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
print(questions)

#підключаємо кнопки дор функцій
btn_ok.clicked.connect(switch_screen)
btn_sleep.clicked.connect(rest)
btn_menu.clicked.connect(back_menu)
btn_back.clicked.connect(to_card)
btn_clear.clicked.connect(clear)
btn_add_quest.clicked.connect(add_question)


card_win.show()

app.exec_()