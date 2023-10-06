import time
print("Quiz start in 10 sec \nTotal 5 question \nAnswer all questions in 3 minute\n10 mark for each question")
time.sleep(10)
list1=['1.What is the extention of python file?','2. Is Python case sensitive when dealing with identifiers?','3.Which of the following functions is a built-in function in python?\na.factorial()    b.print()\nc.seed()         d.psqrt()','4.How is a code block indicated in Python?\na.Bracket    b.Indentation\nc.Key        d.None of these','5. Which of the following types of loops are not supported in Python?\na.for       b.while\nc.do-while  d.None of these']
list2=['.py','yes','b','b','c']
score=0
remaining_time=90
def quiz():
    if remaining_time<=0:
        print('xx OOPS TIMEOUT xx')
        print('score:',score)
        print('Percentage:',(score/50)*100,'%')
        exit()
for i in range(len(list1)):
    print(list1[i])
    quiz()
    initial_time=time.time()
    user_input=input('Answer:')
    answer=user_input.lower()
    end_time=time.time()
    time_taken=int(end_time-initial_time)
    remaining_time=remaining_time-time_taken
    quiz()
    print('remain time',remaining_time,'sec')
    time1=time.ctime()
    if answer==list2[i]:
        print('Correct')
        score=score+10
    else:
        print('Incorrect answer\nThe correct answer is',list2[i])
        score=score+0
print('Completed')
print('Score:',score)
print('Percentage:',(score/50)*100,'%')
time.sleep(10)