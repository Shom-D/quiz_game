import pgzrun
import random
import time

WIDTH, HEIGHT, TITLE = 870, 650, "Quiz"
score = 0
time_left= 10
questions = []
question_count = 0
marquee_message = ""
question_index = 0 
isGameOver = False

#defining rects
marquee_box = Rect(0,0, 880, 80)
question_box = Rect(0,0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_1 = Rect(0,0, 300, 150)
answer_2 = Rect(0, 0, 300, 150)
answer_3 = Rect(0, 0, 300, 150)
answer_4 =  Rect(0, 0, 300, 150)
skip_box =  Rect(0,0, 150, 330)

answer_boxes = [answer_1, answer_2, answer_3, answer_4]

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700, 100)
answer_1.move_ip(20,270)
answer_2.move_ip(370, 270)
answer_3.move_ip(20, 450)
answer_4.move_ip(370, 450)
skip_box.move_ip(700,270)


def read_from_file(filename):
    global questions, question_count
    reader = open(filename, 'r')
    for line in reader:
        questions.append(line)
        question_count +=1
    reader.close()

def update():
    pass

def draw():
    global marquee_message
    screen.clear()
    screen.fill((240,240,240))
    screen.draw.filled_rect(marquee_box, ("#a45c40"))
    screen.draw.filled_rect(question_box, ("#c38370"))
    screen.draw.filled_rect(timer_box,("#c38370") )
    screen.draw.filled_rect(skip_box, ("#f6eee0"))
    for box in answer_boxes:
        screen.draw.filled_rect(box, ("#e4b7a0"))


   

pgzrun.go()