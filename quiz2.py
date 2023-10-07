import time
print("Quiz start in 10 sec \nTotal 5 question \nAnswer all questions in 1 minute\n10 mark for each question")
time.sleep(10)
added_time=time.time()+60 
ending_time=time.ctime(added_time)
question=['1.What is the extention of python file?','2. Is Python case sensitive when dealing with identifiers?','3.Which of the following functions is a built-in function in python?\na.factorial()    b.print()\nc.seed()         d.psqrt()','4.How is a code block indicated in Python?\na.Bracket    b.Indentation\nc.Key        d.None of these','5. Which of the following types of loops are not supported in Python?\na.for       b.while\nc.do-while  d.None of these']
answer=['.py','yes','b','b','c']
score=0
def quiz():
    if current_time>=ending_time:
        print('xx OOPS TIMEOUT xx')
        print('score:',score)
        print('Percentage:',(score/50)*100)
        exit()
for i in range(len(question)):
    current_time=time.ctime()
    print(current_time)
    print(question[i])
    quiz()
    user_input=input('Answer:')
    user_answer=user_input.lower()
    current_time=time.ctime()
    quiz()
    if user_answer==answer[i]:
        score=score+10
    else:
        score=score+0
print('Completed')
print('Score:',score)
print('Percentage:',(score/50)*100)
