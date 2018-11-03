# from random import *
# deck=[x for x in range(52)]
# shuffle(deck)
# print(deck)
# ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
# suits=['Spades','Hearts','Clubs','Diamonds']
# cards=[]
# for card in deck:
#     rank=ranks[card%13]
#     suit=suits[card//13]
#     #print(rank,"of",suit)
#     cards.append([rank,suit])
# player1=cards[:len(cards)//2]
# player2=cards[len(cards)//2:]
# prev_rank=player1.pop(0)[0]
# cur_rank=player2.pop(0)[0]
# print(prev_rank)
# print(cur_rank)
# i=2
# while cur_rank!=prev_rank:
#     i+=1
#     prev_rank=cur_rank
#     if i%2==1:
#         cur_rank=player1.pop(0)[0]
#     else:
#         cur_rank=player2.pop(0)[0]
#     print(cur_rank)
# if i==52:
#     print('Draw')
# elif i%2==0:
#     print("Player 2 Won...!!!")
# else:
#     print("Player 1 Won...!!!")
