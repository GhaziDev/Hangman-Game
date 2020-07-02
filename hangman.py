import random
f=open('wordgenerator.txt','r')
words_list=[i for i in f.read().splitlines()]


class Hangman:
    def __init__(self):
        self.word=random.choice(words_list)
        self.guess='-'*len(self.word)
        self.lives=8
        self.occurences=[]
    def play(self):
        wordlist=list(self.word)
        
        while(self.lives>0):
            print(self.guess)
            ask=input("Guess the correct letter of this word :  ").lower()
            if ask in self.occurences:
                print("\nYou have already guessed that letter")
            
            
            elif ask not in  wordlist:
                self.lives-=1
                self.occurences.append(ask)
                print(f"\nWrong guess,you have {self.lives} lives left")
                if(self.lives==0):
                    print("\nyou lost")
                    print(f"\nthe word is : {self.word}")
            else:
                self.guess=list(self.guess)
                i=0
                while(i<len(self.word)):
                    if ask==wordlist[i]:
                        self.guess[i]=ask
                    i+=1
                self.guess=''.join(self.guess)
                self.occurences.append(ask)
                if('-' not in self.guess):
                    print(f"\nThe word is : {self.guess}")
                    print("\nYou have guessed the word!")
                    break
def play_game():
    while(True):
        h=Hangman()
        h.play()
        t=input("Do you want to play again? (1.yes or 2.no) :  ")
        if(t=='1' or t=='yes' or t=='y'):
            continue
        else:
            print("Thanks for playing!")
            break 


play_game()


#O(n^2) worst case
#o(n) best case
            




