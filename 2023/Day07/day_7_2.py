import re

class hand:
    def __init__(self,cards, bid):
        self.cards = cards
        self.bid = bid
        self.CardToNum()
        self.DetectCardStrength()
    
    def CardToNum(self):
        for i in range(len(self.cards)):
            if self.cards[i] == 'A':
                self.cards[i] = 14
            elif self.cards[i] == 'K':
                self.cards[i] = 13
            elif self.cards[i] == 'Q':
                self.cards[i] = 12
            elif self.cards[i] == 'J':
                self.cards[i] = 1
            elif self.cards[i] == 'T':
                self.cards[i] = 10
            else:
                self.cards[i] = int(self.cards[i])
                
    def DetectCardStrength(self):
        cards = self.cards
        c_value = []
        c_amount = []
        for c in cards:
            if c in c_value:
                i = c_value.index(c)
                c_amount[i] += 1
            else:
                c_value.append(c)
                c_amount.append(1)
            
        if 5 in c_amount:                 # Five of a kind
            self.strength = 6
                
        elif 4 in c_amount:               # Four of a kind
            self.strength = 5
            if 1 in c_value:
                self.strength = 6
                        
        elif 3 in c_amount:
            if 2 in c_amount:             # Full house
                self.strength = 4
                if 1 in c_value:
                    self.strength = 6                    
            else:                         # Three of a kind
                self.strength = 3
                if 1 in c_value:
                    self.strength = 5 
                        
        elif 2 in c_amount:
            if c_amount.count(2) == 2:    # Two pair
                self.strength = 2
                if 1 in c_value:
                    i = c_value.index(1)
                    if c_amount[i] == 2:
                        self.strength = 5
                    else:
                        self.strength = 4
                        
            else:                         # One pair
                self.strength = 1
                if 1 in c_value:
                    self.strength = 3 
                        
        else:                             # High card
            self.strength = 0
            if 1 in c_value:
                self.strength = 1

f = open("day_7_input.txt","r")

card_info = []
winning = 0
        

for line in f:
    line = line.strip()
    cards, bid = re.split(" ",line)
    cards = [x for x in cards]
    c_hand = hand(cards, int(bid))
    card_info.append(c_hand)
f.close()

sorted_card_info = sorted(card_info,key=lambda x:(x.strength,x.cards[0],x.cards[1],x.cards[2],x.cards[3],x.cards[4]))
for i in range(len(sorted_card_info)):
    #print(sorted_card_info[i].cards, sorted_card_info[i]. bid, sorted_card_info[i].strength)
    rank = i + 1
    winning += sorted_card_info[i].bid * rank

print(winning)
