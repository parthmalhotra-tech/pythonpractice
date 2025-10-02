import random
l=[11,2,3,4,5,6,7,8,9,10,10,10,10]
y=[l[random.randint(0,len(l)-1)],l[random.randint(0,len(l)-1)]]
dealer=[l[random.randint(0,len(l)-1)],l[random.randint(0,len(l)-1)]]

def calculate_score(c):
    if 11 in c and 10 in c and len(c)==2:
        return 0
    if 11 in c and sum(c)>21:
        c.remove(11)
        c.append(1)
    return sum(c)
is_game_over=False
while not is_game_over:
    print("Your cards numbers are:",y)
    print("computer's first card is ",dealer[0])
    dealer_score=calculate_score(dealer)
    your_score=calculate_score(y)
    print("your current score:",your_score)
    if dealer_score==0 or your_score==0 or your_score>dealer_score:
                    is_game_over=True
    if is_game_over==False:
                   n=input("Do you want to draw anopther card?(yes/no)").lower()
                   if n=="yes":
                       y.append(l[random.randint(0,len(l)-1)])
                   else:
                         is_game_over=True
                         print("yes")
while dealer_score!=0 and dealer_score<17:
       dealer.append(l[random.randint(0,len(l)-1)])
def compare(dealer_score,your_score):
               if dealer_score==your_score:
                       print("draws")
               if dealer_score==0 or your_score>21 :
                       print("computer wins")
               elif your_score==0 or dealer_score>21: 
                       print("You wins")
               else:
                       if dealer_score>your_score:
                               print("Computer wins")
                       else:
                               print("you wins") 
print("Your final cards:",y)
print("Computer Final cards",dealer)
compare(dealer_score,your_score)
             
                

