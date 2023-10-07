import time
print("Quiz start in 10 sec \nTotal 5 question \nAnswer all questions in 3 minute\n10 mark for each question")
time.sleep(10)
question=['1.What is the extention of python file?','2. Is Python case sensitive when dealing with identifiers?','3.Which of the following functions is a built-in function in python?\na.factorial()    b.print()\nc.seed()         d.psqrt()','4.How is a code block indicated in Python?\na.Bracket    b.Indentation\nc.Key        d.None of these','5. Which of the following types of loops are not supported in Python?\na.for       b.while\nc.do-while  d.None of these']
answer=['.py','yes','b','b','c']
score=0
remaining_time=90
def quiz():
    if remaining_time<=0:
        print('xx OOPS TIMEOUT xx')
        print('score:',score)
        print('Percentage:',(score/50)*100,'%')
        exit()
for i in range(len(question)):
    print(question[i])
    quiz()
    initial_time=time.time()
    user_input=input('Answer:')
    user_answer=user_input.lower()
    end_time=time.time()
    time_taken=int(end_time-initial_time)
    remaining_time=remaining_time-time_taken
    quiz()
    print('remain time',remaining_time,'sec')
    time1=time.ctime()
    if user_answer==answer[i]:
        print('Correct answer')
        score=score+10
    else:
        print('Incorrect answer\nThe correct answer is',answer[i])
        score=score+0
print('Successfully Completed')
print('Score:',score)
print('Percentage:',(score/50)*100,'%')