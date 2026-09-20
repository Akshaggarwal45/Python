Stages=['''
                +--------------+
                  I                   I
                  O
              /    I   \                I
                 /    \                 I
              -------------------  I
''','''
                  +--------------+
                  I                   I
                   O
              /    I   \                I
                 /                    I
              
''',  '''
                   +--------------+
                  I                   I
                 O
              /    I   \               I
                                       I
              -------------------  I
''','''
                   +--------------+
                  I                   I
                  O
              /    I                  I
                                      I
              -------------------  I
''','''

                  I                   I
                  O
              /                       I   
                                      I  
             -------------------  I
''','''
                  +--------------+
                  I                   I
                 O
                                      I
                                      I
              -------------------  I
''',  '''
                   +--------------+
                  I                   I
                      I
                                      I
                                      I   
              -------------------  I
''']
import random
import sqlite3
connection=sqlite3.connect('hangman_score')
cursor=connection.cursor()
list_words=['apple','banana','orange','watermelon','gun','pistol','bomb','subject']
word=random.choice(list_words)
lives=6
display=[]
for i in range(len(word)):
     display+= '_'
print(display)
game_over=False
while not game_over:
    guess=input('enter  guess').lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if guess not in word:
         lives-=1
         if lives==0:
            game_over=True
            print('you lose')
    if '_' not in display:
        game_over=True
        print('you win')
    print (Stages[lives])
cursor.execute('CREATE TABLE IF NOT EXISTS user_score( score INTEGER DEFAULT 0)')
connection.commit()
connection.close()
connection=sqlite3.connect('hangman_score')
cursor=connection.cursor()
cursor.execute('INSERT INTO user_score(score)VALUES(?)',(lives,))  
connection.commit()
connection.close()
connection=sqlite3.connect('hangman_score')
cursor=connection.cursor()
a=cursor.execute('SELECT* FROM user_score').fetchall()
connection.commit()
connection.close()
for x in a:
    print(x)