
import random
import cards


class AmazingPlayer():
    """ Model a player that often makes decisions based on a better strategy. """
    
    
    trump_clubs = [cards.Card(9,1),cards.Card(10,1),cards.Card(12,1
),cards.Card(13,1),cards.Card(1,1),cards.Card(11,4),cards.Card(11,1)]
    trump_diamonds = [cards.Card(9,2),cards.Card(10,2),cards.Card(12,2
),cards.Card(13,2),cards.Card(1,2),cards.Card(11,3),cards.Card(11,2)]
    trump_hearts = [cards.Card(9,3),cards.Card(10,3),cards.Card(12,3
),cards.Card(13,3),cards.Card(1,3),cards.Card(11,2),cards.Card(11,3)]
    trump_spades = [cards.Card(9,4),cards.Card(10,4),cards.Card(12,4
),cards.Card(13,4),cards.Card(1,4),cards.Card(11,1),cards.Card(11,4)]
    list_trumps = [trump_clubs, trump_diamonds, trump_hearts, trump_spades]
    #Ranking of trump suit based on trump
    
    def __init__(self): 
        """ Initialize player. """
        self.__hand = []
        self.__trump = 0
        self.__lead_suit = 0
        self.__points = 0
        self.__is_lead = False
        self.__is_dealer = False
        self.__is_teammate_dealer = False
        self.__is_maker = False
        
        
    def take_card(self, card):
        """ Add card to player's hand. """
        self.__hand.append(card)
        
        
    def show_deck(self):
        """ Returns player's current hand. """
        return self.__hand
    
    
    def assign_trump_suit(self, trump):
        """ Assigns trump suit to player. """
        self.__trump = trump
        
        
    def remove_card(self): #AMAZING Player Contition A
        """ Removes card from player's hand with AMAZING STRATEGY. """
        
        trump_cards = [] #list of cards in player's hand that are trumps
        non_trump_cards = [] #list of cards in player's hand that aren't trumps
        trump_suit = self.__hand[5].suit() #trump suit based on kitty
        
        lst_clubs = []
        lst_diamonds = []
        lst_hearts = []
        lst_spades = []
        lst_suits = [lst_clubs,lst_diamonds,lst_hearts,lst_spades]
        
        lst_ranks = []
        
        for card in self.__hand:
            if card in self.list_trumps[trump_suit - 1]:
                trump_cards.append(card) #adds to trumps
            else:
                non_trump_cards.append(card) #adds to non trumps
        
        for card in non_trump_cards:
            if card.rank() == 9:
                self.__hand.remove(card) #if card in non trumps is 9, discard
                return None 
        
        for card in non_trump_cards:
            if card.rank() == 10:
                self.__hand.remove(card) #if card in non trumps is 10, discard
                return None
        
        for card in non_trump_cards:
            if card.suit() == 1:
                lst_clubs.append(card)
            elif card.suit() == 2:
                lst_diamonds.append(card)
            elif card.suit() == 3:
                lst_hearts.append(card)
            else:
                lst_spades.append(card)
        
        
        if len(non_trump_cards) == 1 or len(non_trump_cards) == 2:
            for card in non_trump_cards:
                if card.rank() == 1:
                    lst_ranks.append(14)
                else:
                    lst_ranks.append(card.rank())
            self.__hand.remove(non_trump_cards[lst_ranks.index(min(lst_ranks))]
)
            return None
        
        
        elif len(non_trump_cards) == 3:
            for lst in lst_suits:
                if len(lst) == 2:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for card in non_trump_cards:
                if card.rank() == 1:
                    lst_ranks.append(14)
                else:
                    lst_ranks.append(card.rank())
            self.__hand.remove(non_trump_cards[lst_ranks.index(min(lst_ranks))]
)
            return None
        
        
        elif len(non_trump_cards) == 4:
            for lst in lst_suits:
                if len(lst) == 3:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for lst in lst_suits:
                if len(lst) == 2:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for card in non_trump_cards:
                if card.rank() == 1:
                    lst_ranks.append(14)
                else:
                    lst_ranks.append(card.rank())
            self.__hand.remove(non_trump_cards[lst_ranks.index(min(lst_ranks))]
)
            return None
        
        
        elif len(non_trump_cards) == 5:
            for lst in lst_suits:
                if len(lst) == 4:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for lst in lst_suits:
                if len(lst) == 3:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for lst in lst_suits:
                if len(lst) == 2:
                    for other in lst_suits:
                        if len(other) == 1:
                            self.__hand.remove(other[0])
                            return None
            
            for card in non_trump_cards:
                if card.rank() == 1:
                    lst_ranks.append(14)
                else:
                    lst_ranks.append(card.rank())
            self.__hand.remove(non_trump_cards[lst_ranks.index(min(lst_ranks))]
)
            return None
            
        #########
        
        for card in self.list_trumps[trump_suit - 1]:
            if card in self.__hand:
                self.__hand.remove(card)
                return None
        
        
    def add_point(self):
        """ Adds point (Trick) to player. """
        self.__points += 1
        
        
    def return_points(self):
        """ Returns points (Tricks) of player. """
        return self.__points
    
    
    def return_maker(self): 
        """ Returns whether or not player is a maker. """
        return self.__is_maker
    

    def play_card_lead(self, Trump): #AMAZING Player Condition B
        """ Returns card with AMAZING strategy if player is the lead. """
        
        if self.list_trumps[Trump - 1][5] in self.__hand:
            return self.__hand.pop(self.__hand.index(self.list_trumps[Trump - 1
][5]))
        
        elif self.list_trumps[Trump - 1][6] in self.__hand:
            return self.__hand.pop(self.__hand.index(self.list_trumps[Trump - 1
][6]))
        
        for card in self.__hand:
            if card.rank() == 13 and card.suit() != Trump:
                return self.__hand.pop(self.__hand.index(card))
            
        for card in self.__hand:
            if card.rank() == 1 and card.suit() != Trump:
                return self.__hand.pop(self.__hand.index(card))
        
                
        return self.__hand.pop(random.randrange(len(self.__hand)))         
        
        
    
    def play_card_not_lead(self, leadsuit): #AMAZING Player Condition B
        """ Returns legal card with AMAZING strategy if player is not lead. """
        
        legal_cards = []
        lst_trumps = []
        lst_ranks = []

        if self.list_trumps[leadsuit - 1][6] in self.__hand:
            return self.list_trumps[leadsuit - 1][6] #if jack in hand, play it


        if self.__trump == leadsuit:
            if self.list_trumps[leadsuit - 1][5] in self.__hand:
                legal_cards.append(self.list_trumps[leadsuit - 1][5])


        for card in self.__hand:
            if card.suit() == leadsuit:
                legal_cards.append(card)
        
        for card in self.__hand:
            if card in self.list_trumps[self.__trump - 1]:
                lst_trumps.append(card)
                
                
        if len(legal_cards) != 0: #If there are legal cards
            if self.__trump != leadsuit or len(lst_trumps) == 0:
                for card in legal_cards:
                    if card.rank() == 1:
                        lst_ranks.append(14)
                    else:
                        lst_ranks.append(card.rank())
                return self.__hand.pop(self.__hand.index(legal_cards[
lst_ranks.index(max(lst_ranks))]))
            
            else:
                for card in lst_trumps:
                    lst_ranks.append(self.list_trumps[self.__trump - 1].index(
card))
                return self.__hand.pop(self.__hand.index(lst_trumps[
lst_ranks.index(max(lst_ranks))]))
                    
        
        else: #If no legal cards
            if len(lst_trumps) == 0:
                for card in self.__hand:
                    if card.rank() == 1:
                        lst_ranks.append(14)
                    else:
                        lst_ranks.append(card.rank())
                return self.__hand.pop(lst_ranks.index(min(lst_ranks)))
            
            else:
                for card in lst_trumps:
                    lst_ranks.append(self.list_trumps[self.__trump - 1].index(
card))
                return self.__hand.pop(self.__hand.index(lst_trumps[
lst_ranks.index(min(lst_ranks))]))
        

    
    def play_alone(self, Trump): #AMAZING Player Condition C
        """ Returns if to play alone using AMAZING strategy. """


        lst_trumps = []
          
        for card in self.__hand:
            if card in self.list_trumps[Trump - 1]:
                lst_trumps.append(card)    
            

        if len(lst_trumps) == 4:
            return True
        elif self.list_trumps[Trump - 1][6
] in self.__hand and self.list_trumps[Trump - 1][5
] in self.__hand and self.list_trumps[Trump - 1][4] in self.__hand:
            return True
        elif self.list_trumps[Trump - 1][6
] in self.__hand and self.list_trumps[Trump - 1][5
] in self.__hand and self.list_trumps[Trump - 1][3] in self.__hand:
            return True
        elif self.list_trumps[Trump - 1][6
] in self.__hand and self.list_trumps[Trump - 1][5
] in self.__hand and self.list_trumps[Trump - 1][2] in self.__hand:
            return True
        return False


    
    def is_lead(self, boolean):
        """ Changes whether or not player is lead based on boolean value. """
        self.__is_lead = boolean
    
    
    def is_dealer(self, boolean):
        """ Changes whether or not player is dealer based on boolean value. """
        self.__is_dealer = boolean
        
        
    def is_teammate_dealer(self, boolean):
        """ Changes if player's teammate is dealer based on boolean value. """
        self.__is_teammate_dealer = boolean
        
        
    def is_maker(self, boolean):
        """ Changes whether or not player is maker based on boolean value. """
        self.__is_maker = boolean
        
    
    def first_round(self, card): #Naming Trump First Round
        """ Returns if to assign trump in first round of bidding. """


        potential_trump_suit = card.suit()
        points = 0
        
        for card in self.__hand:
            if card == self.list_trumps[potential_trump_suit - 1][6
] or card == self.list_trumps[potential_trump_suit - 1][5]:
                points += 3
            elif card == self.list_trumps[potential_trump_suit - 1][4
] or card == self.list_trumps[potential_trump_suit - 1][3
] or card == self.list_trumps[potential_trump_suit - 1][2]:
                points += 2
            elif card == self.list_trumps[potential_trump_suit - 1][1
] or card == self.list_trumps[potential_trump_suit - 1][0] or card.rank() == 1:
                points += 1
        
        if points >= 6:
            return True


        return False


    def second_round(self, suit): #Naming Trump Second Round
        """ Returns if to assign trump in second round of bidding. """
        

        points_clubs = 0
        points_diamonds = 0
        points_hearts = 0
        points_spades = 0
        points_lst = [points_clubs,points_diamonds,points_hearts,points_spades]
        
        for card in self.__hand:
            for i in range(4):
                if card == self.list_trumps[i][6] or card == self.list_trumps[i
][5]:
                    points_lst[i] += 3
                elif card == self.list_trumps[i][4
] or card == self.list_trumps[i][3] or card == self.list_trumps[i][2]:
                    points_lst[i] += 2
                elif card == self.list_trumps[i][1
] or card == self.list_trumps[i][0]:
                    points_lst[i] += 1
                    
        for obj in points_lst:
            if suit - 1 == points_lst.index(obj):
                continue
            else:
                if obj >= 5:
                    return points_lst.index(obj) + 1



        return False


     
class StrategyPlayer():
    """ Model a player that often makes decisions based on a strategy. """
    
    
    trump_clubs = [cards.Card(9,1),cards.Card(10,1),cards.Card(12,1
),cards.Card(13,1),cards.Card(1,1),cards.Card(11,4),cards.Card(11,1)]
    trump_diamonds = [cards.Card(9,2),cards.Card(10,2),cards.Card(12,2
),cards.Card(13,2),cards.Card(1,2),cards.Card(11,3),cards.Card(11,2)]
    trump_hearts = [cards.Card(9,3),cards.Card(10,3),cards.Card(12,3
),cards.Card(13,3),cards.Card(1,3),cards.Card(11,2),cards.Card(11,3)]
    trump_spades = [cards.Card(9,4),cards.Card(10,4),cards.Card(12,4
),cards.Card(13,4),cards.Card(1,4),cards.Card(11,1),cards.Card(11,4)]
    list_trumps = [trump_clubs, trump_diamonds, trump_hearts, trump_spades]
    #Ranking of trump suit based on trump
    
    def __init__(self):
        """ Initialize player. """
        self.__hand = []
        self.__trump = 0
        self.__lead_suit = 0
        self.__points = 0
        self.__is_lead = False
        self.__is_dealer = False
        self.__is_teammate_dealer = False
        self.__is_maker = False
      
        
    def take_card(self, card):
        """ Add card to player's hand. """
        self.__hand.append(card)
        
        
    def show_deck(self):
        """ Returns player's current hand. """
        return self.__hand
    
    
    def assign_trump_suit(self, trump):
        """ Assigns trump suit to player. """
        self.__trump = trump
        
        
    def remove_card(self): #StrategyPlayer Contition A
        """ Removes card from player's hand based on strategy. """
       
        number_clubs = []
        number_diamonds = []
        number_hearts = []
        number_spades = []
        list_nums = [
number_clubs, number_diamonds, number_hearts, number_spades]
        
        rank_clubs = [cards.Card(9,1),cards.Card(10,1),cards.Card(11,1
),cards.Card(12,1),cards.Card(13,1),cards.Card(1,1)]
        rank_diamonds = [cards.Card(9,2),cards.Card(10,2),cards.Card(11,2
),cards.Card(12,2),cards.Card(13,2),cards.Card(1,2)]
        rank_hearts = [cards.Card(9,3),cards.Card(10,3),cards.Card(11,3
),cards.Card(12,3),cards.Card(13,3),cards.Card(1,3)]
        rank_spades = [cards.Card(9,4),cards.Card(10,4),cards.Card(11,4
),cards.Card(12,4),cards.Card(13,4),cards.Card(1,4)]
        list_ranks = [rank_clubs, rank_diamonds, rank_hearts, rank_spades]
        #Ranks of cards based on not trump
        ranking = [cards.Card(9,1),cards.Card(9,2),cards.Card(9,3
),cards.Card(9,4),cards.Card(10,1),cards.Card(10,2),cards.Card(10,3
),cards.Card(10,4),cards.Card(11,1),cards.Card(11,2),cards.Card(11,3
),cards.Card(11,4),cards.Card(12,1),cards.Card(12,2),cards.Card(12,3
),cards.Card(12,4),cards.Card(13,1),cards.Card(13,2),cards.Card(13,3
),cards.Card(13,4),cards.Card(1,1),cards.Card(1,2),cards.Card(1,3
),cards.Card(1,4)]
        #Ranks of cards based on not trump
                
        for k in range(4):
            for i in list_ranks[k]:
                if i in self.__hand:
                    list_nums[k].append(i)
            
        for j in list_nums:
            if len(j) >= 3:
                self.__hand.pop(self.__hand.index(j[0]))
                return None
        
        if len(self.__hand) == 6:
            for i in ranking:
                if i in self.__hand:
                    self.__hand.pop(self.__hand.index(i))
                    return None
                
            
    def add_point(self):
        """ Adds point (Trick) to player. """
        self.__points += 1
        
        
    def return_points(self):
        """ Returns points (Tricks) of player. """
        return self.__points
    
    
    def return_maker(self): 
        """ Returns whether or not player is a maker. """
        return self.__is_maker
    

    def play_card_lead(self, Trump): #StrategyPlayer Condition B
        """ Returns card based on strategy if player is the lead. """
        
    
        trump_list = []
        for i in self.__hand:
            if i in self.list_trumps[Trump - 1]:
                trump_list.append(i)
        
        if len(trump_list) > 0:
            x = trump_list.pop(random.randrange(len(trump_list)))
            return self.__hand.pop(self.__hand.index(x))
        
        else:
            return self.__hand.pop(random.randrange(len(self.__hand)))
            
    
    def play_card_not_lead(self, leadsuit): #StrategyPlayer Condition B
        """ Returns legal card based on strategy if player is not the lead. """
        legal_cards = []
        
        if self.list_trumps[leadsuit - 1][6] in self.__hand:
            return self.list_trumps[leadsuit - 1][6]
        
        else:
        
            if leadsuit == self.__trump: #If the leading card's suit is a trump
                
                for i in range(7):
                    if self.list_trumps[leadsuit - 1][i] in self.__hand:
                        legal_cards.append(self.list_trumps[leadsuit - 1][i]) 
                        #Counts how many of lead suit are available
                
                if len(legal_cards) == 0:
                   
                    return self.__hand.pop(random.randrange(len(self.__hand))) 
                    #Play random card from hand
                    
                    
                else:
                    x = legal_cards.pop(random.randrange(len(legal_cards))) 
                    self.__hand.remove(x) #Play random card from legal options
                    return x
                
            else: #If the leading card's suit is not the trump suit
                
                for i in range(5):
                    if self.list_trumps[leadsuit - 1][i] in self.__hand:
                        legal_cards.append(self.list_trumps[leadsuit - 1][i]) 
                
                if self.list_trumps[leadsuit - 1][6] in self.__hand:
                    legal_cards.append(self.list_trumps[leadsuit - 1][6]) 
                    #Counts how many of lead suit are available
                
                if len(legal_cards) == 0:
                    
                    return self.__hand.pop(random.randrange(len(self.__hand))) 
                    #Play random card from hand
                   
                else:
                    x = legal_cards.pop(random.randrange(len(legal_cards))) 
                    self.__hand.remove(x) #Play random card from legal options
                    return x
    

    def play_alone(self, Trump): #StrategyPlayer Condition C
        """ Returns if player will play alone based on strategy. """

        trump_cards = []
        non_cards = []
        
        for i in self.__hand:
            if i in self.list_trumps[Trump - 1]:
                trump_cards.append(i)
            else:
                non_cards.append(i)
        
        if len(trump_cards) == 5:
            return True
        elif len(trump_cards) == 4:
            if non_cards[0].rank() == 1:
                return True
        elif len(trump_cards) == 3:
            if self.list_trumps[Trump - 1][5
] in trump_cards or self.list_trumps[Trump - 1][6] in trump_cards:
                if non_cards[0].suit() == non_cards[1].suit():
                    return True
            if non_cards[0].rank() == 1:
                if non_cards[1].rank() == 1 or non_cards[1].rank() == 13:
                    return True
            if non_cards[1].rank() == 1:
                if non_cards[0].rank() == 1 or non_cards[0].rank() == 13:
                    return True
            if self.list_trumps[Trump - 1][2
] in trump_cards and self.list_trumps[Trump - 1][3
] in trump_cards and self.list_trumps[Trump - 1][4] in trump_cards:
                if non_cards[0].rank() == 1:
                    if non_cards[1].rank() == 13:
                        return True
                elif non_cards[1].rank() == 1:
                    if non_cards[0].rank() == 13:
                        return True
        elif len(trump_cards) == 2:
            if self.list_trumps[Trump - 1][5
] in trump_cards and self.list_trumps[Trump - 1][6] in trump_cards:
                if non_cards[0].suit() == non_cards[1].suit() == non_cards[2
].suit():
                    if non_cards[0].rank() == 1:
                        if non_cards[1].rank() == 13 or non_cards[2
].rank == 13:
                            return True
                    elif non_cards[1].rank() == 1:
                        if non_cards[0].rank() == 13 or non_cards[2
].rank == 13:
                            return True
                    elif non_cards[2].rank() == 1:
                        if non_cards[0].rank() == 13 or non_cards[1
].rank == 13:
                            return True
        
        return False
        
  
    def is_lead(self, boolean):
        """ Changes whether or not player is lead based on boolean value. """
        self.__is_lead = boolean
    
    
    def is_dealer(self, boolean):
        """ Changes whether or not player is dealer based on boolean value. """
        self.__is_dealer = boolean
        
        
    def is_teammate_dealer(self, boolean):
        """ Changes if player's teammate is dealer based on boolean value. """
        self.__is_teammate_dealer = boolean
        
        
    def is_maker(self, boolean):
        """ Changes whether or not player is maker based on boolean value. """
        self.__is_maker = boolean
        
    
    def first_round(self, card): #Naming Trump First Round
        """ Returns if to assign trump in first round of bidding. """
        n = 0
        not_n = [1,2,3,4,5]
        list_index = 0
        
        for i in range(5):
            if self.list_trumps[card.suit()-1][i] in self.__hand:
                n += 1
        for p in range(5):
            if self.__hand[p].suit() != card.suit():
                not_n[list_index] = self.__hand[p]
                list_index += 1 #Adds to list of non-lead cards
        
        if self.__is_dealer == False and self.__is_teammate_dealer == False:
        #NOT the dealer
            if self.list_trumps[card.suit()-1][5
] in self.__hand and self.list_trumps[card.suit()-1][6] in self.__hand:
                if n >= 2:
                    return True #Two Bowers and 2 other Trumps
            elif self.list_trumps[card.suit()-1][5
] in self.__hand or self.list_trumps[card.suit()-1][6] in self.__hand:
                if n >= 3:
                    return True #One Bower and 3 other Trumps
            elif n >= 5:
                return True #5 Trumps
            try:
                x = not_n[0].suit()
                y = not_n[1].suit()
                if n >= 3 and x == y:
                    return True #2 Suited and 3 Trumps
            except:
                pass
                
        
        else:   #IS the dealer
            if self.list_trumps[card.suit()-1][5
] in self.__hand and self.list_trumps[card.suit()-1][6] in self.__hand:
                return True #Both Bowers
            elif self.list_trumps[card.suit()-1][5
] in self.__hand or self.list_trumps[card.suit()-1][6] in self.__hand:
                if n >= 2:
                    return True #One Bower and 2 other Trumps
            elif n >= 4:
                return True #Four or Five Trumps
            try:
                x = not_n[0].suit()
                y = not_n[1].suit()
                if n >= 3 and x == y:
                    return True #2 Suited and 3 Trumps
            except:
                pass
        
        return False
    
    
    def second_round(self, suit): #Naming Trump Second Round
        """ Returns if to assign trump in second round of bidding. """
        
        for i in range(4):
            if i + 1 == suit:
                continue
            else:
                if self.list_trumps[i][5] in self.__hand and self.list_trumps[i
][6] in self.__hand:
                    return i + 1 #Both Bowers of that class
        
        for i in range(4):
            n = 0
            if i + 1 == suit:
                continue
            else:
                for p in range(5):
                    if self.list_trumps[i][p] in self.__hand:
                        n += 1
                if self.list_trumps[i][5] in self.__hand or self.list_trumps[i
][6] in self.__hand:
                    if n >= 2:
                        return i + 1 #One Bower and two of same class
        
        for i in range(4):
            n = 0
            if i + 1 == suit:
                continue
            else:
                for p in range(5):
                    if self.list_trumps[i][p] in self.__hand:
                        n += 1
                if n >= 4:
                    return i + 1 #Four or more of the same class
                    
        return False
    
