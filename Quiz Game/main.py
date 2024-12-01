import pgzrun
import random
import time

WIDTH, HEIGHT, TITLE = 870, 650, "Quiz"
time_left= 10
questions = []
question_count = 0
marquee_message = ""
question_index = 0 
last_time = time.time()
wrong = 0
right = 0

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
        question_info = manage_line(line)
        questions.append(question_info)
        question_count +=1
        print(question_count)
    random.shuffle(questions)
    reader.close()

def manage_line(line):
    question= []
    temp= ''
    for char in line:
        if char !=',':
            temp+=char
        else:
            question.append(temp)  
            temp= ''
    print(question)  
    return question    

def on_mouse_down(pos):
    if question_count >= question_index+1:
        for box in answer_boxes:
            if box.collidepoint(pos):
                manage_click(box)
        if skip_box.collidepoint(pos):
            level_over(False)

def manage_click(box):
    correct_answer = int(questions[question_index][5])
    answer = answer_boxes.index(box)+1
    print(f"Answer is at index: {correct_answer}. Answer provided is {answer}")
    if correct_answer == answer:
        correct= True
    else:
        correct= False
    level_over(correct)

def level_over(correct):
    global level_start_time, question_index, time_left,right,wrong
    if correct:
        right+=1
    else:
        wrong+=1
    level_start_time= time.time()
    question_index+=1
    time_left = 10

def handle_time():
    global last_time, time_left
    if time.time()- last_time > 1:
        time_left-=1
        last_time=time.time()

def update():
    pass

def draw_boxes():
    global marquee_message
    screen.fill((240,240,240))
    screen.draw.filled_rect(marquee_box, ("#a45c40"))
    screen.draw.filled_rect(question_box, ("#c38370"))
    screen.draw.filled_rect(timer_box,("#c38370") )
    screen.draw.filled_rect(skip_box, ("#f6eee0"))
    for box in answer_boxes:
            screen.draw.filled_rect(box, ("#e4b7a0"))
    marquee_message= "Welcome to this quiz game"
    screen.draw.textbox(marquee_message, marquee_box, color = (255,255,255))
    screen.draw.textbox(questions[question_index][0], question_box, color = (255,255,255))
    for x in range(4):
        screen.draw.textbox(questions[question_index][1+x], answer_boxes[x],color = (255,255,255))
    screen.draw.textbox(str(time_left), timer_box, color = (255,255,255))
    screen.draw.textbox('Skip', skip_box, color= (255,255,255))

def gameOver():
    screen.fill((50,50,50))
    screen.draw.text("You finished the quiz", (WIDTH/4, HEIGHT/3), color= (255,255,255), fontsize= 70)
    screen.draw.text(f"You got {right}/{question_count} questions correct!",(WIDTH/5, HEIGHT/3+70), color= (255,255,255), fontsize= 45)

def draw():
    screen.clear()
    if question_count >= question_index+1:
        draw_boxes()
        handle_time()
        if not time_left:
            level_over(False)
    else:
        gameOver()

read_from_file("questions.txt")

pgzrun.go()