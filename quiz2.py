import time
print("Quiz start in 10 sec \nTotal 5 question \nAnswer all questions in 1 minute\n10 mark for each question")
time.sleep(10)
time0=time.time()+60 
time2=time.ctime(time0)
list1=['1.What is the extention of python file?','2. Is Python case sensitive when dealing with identifiers?','3.Which of the following functions is a built-in function in python?\na.factorial()    b.print()\nc.seed()         d.psqrt()','4.How is a code block indicated in Python?\na.Bracket    b.Indentation\nc.Key        d.None of these','5. Which of the following types of loops are not supported in Python?\na.for       b.while\nc.do-while  d.None of these']
list2=['.py','yes','b','b','c']
score=0
def quiz():
    if time1>=time2:
        print('xx OOPS TIMEOUT xx')
        print('score:',score)
        exit()
for i in range(len(list1)):
    time1=time.ctime()
    print(time1)
    print(list1[i])
    quiz()
    user_input=input('Answer:')
    answer=user_input.lower()
    time1=time.ctime()
    quiz()
    if answer==list2[i]:
        score=score+10
    else:
        score=score+0
print('Completed')
print('Score:',score)
