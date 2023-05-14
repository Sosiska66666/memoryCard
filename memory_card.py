from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(vopros: Question):
    #прячем
    RadioGroupButton.hide()
    Groupbox.hide()
	
    Radiobutton1.setText(vopros.right_answer)
    Radiobutton2.setText(vopros.wrong1)
    Radiobutton3.setText(vopros.wrong2)
    Radiobutton4.setText(vopros.wrong3)
	
    shuffle(answers)                #перемешиваем
    VertLayout1.addWidget(answers[0]) 
    VertLayout1.addWidget(answers[1])
    VertLayout2.addWidget(answers[2]) 
    VertLayout2.addWidget(answers[3])

	
    RadioGroup.setExclusive(False)    #сброс флагов
    Radiobutton1.setChecked(False)
    Radiobutton2.setChecked(False)
    Radiobutton3.setChecked(False)
    Radiobutton4.setChecked(False)
    RadioGroup.setExclusive(True)
	
    question.setText(vopros.quest)
    answer.setText(vopros.right_answer)
    RadioGroupButton.show()
    pushbutton.setText('Ответить')

def check_answer():    #функция проверки
    ans_correct = 'Correct!'
    ans_wrong = 'Неверно! Получится в следующий раз.'
    missed = 'Надо выбрать вариант ответа!'

    if Radiobutton1.isChecked():
        show_correct(ans_correct)
        main_win.correct += 1
    elif Radiobutton2.isChecked() or Radiobutton3.isChecked() or Radiobutton4.isChecked():
        show_correct(ans_wrong)
        main_win.wrong += 1
    else:
        show_correct(missed)
        main_win.wrong += 1

def show_correct(res):
    #скрываем
    RadioGroupButton.hide()
    Groupbox.hide()
    
    #заполняем переменные
    result.setText(res)
    
    #проявляем
    Groupbox.show()
    pushbutton.setText('Следующий вопрос')

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(quest_list):
        main_win.cur_question = 0
        statistics = main_win.correct / len(quest_list)
        statistics = str(statistics * 100) + '%'
        print('Статистика')
        print('-Всего вопросов: ' + str(len(quest_list)))
        print('-Правильных ответов: ' + str(main_win.correct))
        print('Рейтинг: ' + statistics)
        main_win.correct = 0

    vopros = quest_list[main_win.cur_question]
    ask(vopros)

def click_ok():
    if pushbutton.text() == 'Ответить':
        check_answer()
    else:
        next_question()

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memo Card')
main_win.correct = 0
main_win.wrong = 0

question = QLabel('')

RadioGroupButton = QGroupBox('')  #группа
Radiobutton1 = QRadioButton('')
Radiobutton2 = QRadioButton('')
Radiobutton3 = QRadioButton('')
Radiobutton4 = QRadioButton('')

answers = [Radiobutton1, Radiobutton2, Radiobutton3, Radiobutton4]     #список с кнопками
HorLayout1 = QHBoxLayout()   
VertLayout1 = QVBoxLayout() 
VertLayout2 = QVBoxLayout()

RadioGroup = QButtonGroup() #группа кнопок
RadioGroup.addButton(Radiobutton1)
RadioGroup.addButton(Radiobutton2)
RadioGroup.addButton(Radiobutton3)
RadioGroup.addButton(Radiobutton4)

VertLayout1.addWidget(Radiobutton1) #закрепление
VertLayout1.addWidget(Radiobutton2)
VertLayout2.addWidget(Radiobutton3) 
VertLayout2.addWidget(Radiobutton4)
HorLayout1.addLayout(VertLayout1)
HorLayout1.addLayout(VertLayout2)
VertLayout1.setSpacing(35)
VertLayout2.setSpacing(35)
HorLayout1.setSpacing(35)
RadioGroupButton.setLayout(HorLayout1)

pushbutton = QPushButton('Ответить')     #ответ
MainVertLayout = QVBoxLayout()
horisontalLayout1 = QHBoxLayout()
horisontalLayout2 = QHBoxLayout()

horisontalLayout1.addWidget(question, alignment=Qt.AlignHCenter)   #обработка виджетов и группы
horisontalLayout2.addStretch(2)
horisontalLayout2.addWidget(pushbutton, stretch=5)
horisontalLayout2.addStretch(2)
MainVertLayout.addLayout(horisontalLayout1)
MainVertLayout.addWidget(RadioGroupButton, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Groupbox = QGroupBox('Результат ответа')
result = QLabel('Прав/неправ')
answer = QLabel('Правильный ответ')
BoxLayout = QVBoxLayout()

BoxLayout.addWidget(result)
BoxLayout.setSpacing(35)
BoxLayout.addWidget(answer, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Groupbox.setLayout(BoxLayout)

MainVertLayout.addWidget(Groupbox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #сбор виджетов и двух групп

MainVertLayout.addLayout(horisontalLayout2)
main_win.setLayout(MainVertLayout)

main_win.cur_question = -1

quest_list = list()
q1 = Question('Что из этого не игровой движок?','Game Engine', 'Unreal Engine', 'Amethyst', 'Unity')
quest_list.append(q1)
q1 = Question('Столица Северной Кореи', 'Пхеньян', 'Оттава', 'Зиньгау', 'Токио')
quest_list.append(q1)
q1 = Question('Год начала II Мировой Войны', '1939', '1941', '1945', '1942')
quest_list.append(q1)
q1 = Question('ВВП это -', 'Валовый внутренний продукт', 'Владимир Владимирович Путин', 'Victory, Victory, Победа!', 'Верти Внутри Почку')
quest_list.append(q1)
q1 = Question('Мангустин это -', 'Фрукт', 'Вид обезьян', 'Самка мангуста', 'Мексиканский маньяк')
quest_list.append(q1)
q1 = Question('Столица США', 'Вашингтон', 'Мехико', 'Алжир', 'Нью-Йорк')
quest_list.append(q1)
shuffle(quest_list)

next_question()
pushbutton.clicked.connect(click_ok)

RadioGroupButton.show()
Groupbox.hide()

main_win.show()
app.exec_()