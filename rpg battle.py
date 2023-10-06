import random
player=100
dragon=100

when=['Yesterday','Today','A long time ago','A few years ago','Last night','Early morning','A few days ago']
who=['a dog','a cat','a man','a lady','a lion','a donkey','a boy']
place=['kerala','Goa','Chennai','Bangalore','Mumbai','Kolkata','Bopal']
went=['market','forest','home','school','beach','road','park']
happened=['eat food','sings s song','wrote a book','found a box','drive a car','play a game','laugh louder']

for i in range(10):
    player1=random.randint(5,20)
    dragon1=random.randint(5,20)
    print(random.choice(when)+', '+random.choice(who)+' that lived in '+random.choice(place)+', went to the '+random.choice(went)+' and '+random.choice(happened))
    player=player-player1
    dragon=dragon-dragon1
    print('***Battle Score***')
    if player<=0 and dragon<=0:
        if player>dragon:
            print('Player HP=',player)
            print('dragon HP=',dragon)  
            print('Player win')
            exit()
        else:
            print('Player HP=',player)
            print('Dragon HP=',dragon)  
            print('Dragon win')
            exit()
    if player<=0:
        print('Player HP=',player)
        print('Dragon HP=',dragon)  
        print('Dragon win')
        exit()
    if dragon<0:
        print('Player HP=',player)
        print('Dragon HP=',dragon)
        print('Player win')
        exit()
    print('Player HP=',player)
    print('Dragon HP=',dragon)
