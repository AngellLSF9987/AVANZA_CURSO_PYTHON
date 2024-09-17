import random
import Quiz
import os
quizs = []

def read_file():
    os.system
    with open("quiz-list.txt") as f:
        lines=f.readlines()
        question=""
        answer1=""
        answer2=""
        answer3=""
        correct=0
        count=0
        for line in lines:
            if (line.startswith("Pregunta:")):
                question=line
                answer1=lines[count+1]
                answer2=lines[count+2]
                answer3=lines[count+3]
                correct=lines[count+4]
                quiz=Quiz.Quiz(question,answer1,answer2,answer3,correct)
                quizs.append(quiz)
            count+=1


read_file()

while True:
    rn=random.randint(0,len(quizs))
    quiz=quizs[rn-1]
    print("Pregunta: ",quiz.question.replace("Pregunta:",""))
    print(quiz.answer1)
    print(quiz.answer2)
    print(quiz.answer3)
    #(quiz.correct)
    answer = input("Respuesta: ")
    answer=answer.strip()
    correct=quiz.correct.strip()
    #if (answer.strip() == quiz.correct.strip()):
    if (answer == correct):
        print("Correcto")
    else:
        print("Incorrecto, la repuesta correcta es: ",quiz.correct, ", seleccionaste la: ", answer)
 
    quizs.pop(rn-1)
    espera=input("Presiona para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(quizs) == 0:
        break


