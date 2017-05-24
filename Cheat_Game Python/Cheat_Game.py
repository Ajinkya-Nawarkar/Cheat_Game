#######################################################################################

#"Cheat_Game.py" Module
#Name: Ajinkya Nawarkar   
#
#Date Created: 11/28/15

#This program defines a class named Game for the logic of the game in the card game "CHEAT".

#######################################################################################

#import the attributes and methods from the Random and os classes
from random import *
import os

#Define the class Cheat_Game
class Cheat_Game:

#Initialize all the variables and create objects of the imported class
    def __init__(self):
        self.players=[]
        self.cards=[] 
        self.player1_deck=[]
        self.player2_deck=[]
        self.player1_cards=[]
        self.player2_cards=[]
        self.player1_cards_updated=[]
        self.player2_cards_updated=[]
        self.pile=[]

#Define a function which gives the players usefull information and rules about the game
    def game_rules(self):
        print("\t\t\t\t\t\t\t*/**/*/*\t*/    */\t*/*/*/*/*\t     *     \t*/*/*//*/*/")
        print("\t\t\t\t\t\t\t*/      \t*/    */\t*/       \t   */ \*   \t     ||    ")
        print("\t\t\t\t\t\t\t*/      \t*/*/*/*/\t*/*/*/*  \t  */   \*  \t     ||    ")
        print("\t\t\t\t\t\t\t*/      \t*/    */\t*/       \t */ *** \* \t     ||    ")
        print("\t\t\t\t\t\t\t*/*/*/*/\t*/    */\t*/*/*/**/\t*/       \*\t     ||    ")
        print("\n\t\t\t\t\t\t\t============================================================================")

        print("\n\n\tThe object of the game is to get rid of all your cards. The winner is the first\
 person to get rid of all their cards.\n")
            
        print("\tTo start the game, the entire deck of 52 cards is dealt evenly to the two players equally.\
 On this first turn, he or she is allowed to put down all of his or her aces.\
 He or she will take the cards(This is called the move), place them face-down on the pile of cards\
 and say the number of cards they are putting down and that turn's card (ex \"2 twos\", \"1 jack\")(This is called a claim).\
 The next player will put down twos, the next three, etc. until king, then it goes back to aces.\n")

        print("\tOn each player's turn, they will have to cheat if they do not have\
 any of the correct card. This means they will put down cards other than the correct\
 ones. You are NOT allowed to put\tdown your cards and say that you are putting down\
 a different number of cards (ex say \"1 king\" but actually put down two). So\
 you can put down an ace and an eight when you are supposed to put down kings\
 and say \"2 kings\". You can also cheat even if you don't have to, if you are\
 supposed to put down fours and you have 2 fours, you could put the fours down\
 and also put a queen and say \"3 fours\", or even put down a jack and say\
 \"1 four\", and not even put down the fours that you have at all!\n")

        print("\tAfter any player's turn, any other player can challenge them by accusing\
 \"Cheat!\". If the player cheated, they must take up the entire pile. If the\
 player hasn't cheated, the challenger must add the entire pile to their hand.")

        print("\tThis will continue until a player wins to be on the first place.\n")

        print("#############////////////////////////////////////////////////////////////////////////////*****////////////////////////////////////////////////////////////////////////#############\n")

        print("\tType the move in a format for ex: '1 King 2 Jacks' or '3 Aces 1 Two'")
        print("\tCorrespondingly, Type your claim as '3 Fives' or '4 Queens'")
        print("\tThe INPUTS should be types as shown above with CARD TYPE'S FIRST LETTER CAPATALIZED\
 and SPACE between the NUMERICAL and STRING values of no. of cards\
 and card type respectively!!\n")

        print("#############////////////////////////////////////////////////////////////////////////////*****////////////////////////////////////////////////////////////////////////#############\n\n")
        ch=input("Press enter to continue: ")
        if ch=='':
            obj.cls()
    
#Define the function cls to clear the screen
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
#Define the function deck() to create a deck of 52 cards
    def deck(self):
        #Create a list for deck of 52 cards
        for suit in range(1,5):
            for value in range(1,14):
                temp_card=[suit,value]
                self.cards.append(temp_card)
        shuffle(self.cards)

#Define the function get_players() to get the players names 
    def get_players(self):
        for i in range(2):
            name=input("Enter your name player %d: " %(i+1))
            self.players.append(name)

#Define the function deal_cards() to distribute the cards to each of the players
    def deal_deck(self):
        for j in range(52):
            if (j%2==0):
                self.player1_deck.append(self.cards[j])
            elif(j%2==1):
                self.player2_deck.append(self.cards[j])

#Define the function deal_cards() to get the number of each card in each player's deck; for eg: 2 aces 3 kings...,etc
    def deal_cards(self):
        c=0
        for val in range(1,14):
            for card_value in self.player1_deck:
                if (card_value[1]==val):
                    c=c+1
            self.player1_cards.append(c)
            c=0

        c=0
        for val in range(1,14):
            for card_value in self.player2_deck:
                if (card_value[1]==val):
                    c=c+1
            self.player2_cards.append(c)
            c=0

#Define a function to get VALUE of a card as a string
    def get_value_asString(self,value):
        return ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"][value]

#Define a function to get the value as integer using dictionary
    def get_value(self,valuestring):
        scores={"Ace":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13}
        value=scores.get(valuestring)
        return value

#Define the function hand_status() for printing the status for player's hand
    def hand_status(self,player_cards,name):
        print("These are your cards %s : \n"%name)
        for i in range(0, 13):
            print("%d %ss" %(player_cards[i],obj.get_value_asString(i)))
            

#Define the function to remove particular cards from the player's deck
    def remove_cards(self,player_cards,player_move):
        for i,j in zip(range(0,len(player_move),2),range(1,len(player_move),2)):
            try:
                val=obj.get_value(player_move[j])
                player_cards[val-1] -= int(player_move[i])
            except:
                print("Oops! Had told you to follow the format! Now you lose ur chance")
                return 0
        return player_cards          
            
#Define the function to add particular cards from the player's deck                  
    def add_cards(self,pile,player_cards):
        for i,j in zip(range(0,len(pile),2),range(1,len(pile),2)):
            val=obj.get_value(pile[j])
            player_cards[val-1]+=int(pile[i])
            return player_cards


#Define the function strip_off the last 's' character from the given list's elements      
    def strip_s(self,list_s):
        for i in range(1,len(list_s),2):
                list_s[i]=list_s[i].rstrip('s')
        return list_s
                
#Define the function challenge() to 
    def challenge(self,challenger,challenged,move,claim,challenger_cards,challenged_cards,pile,fl):
        choice=input("\n%s, Do you wanna challenge %s? press Y/N: " %(challenger,challenged))
        if (choice=='Y') or (choice=='y'):
            challenger_cards_updated=[]
            challenged_cards_updated=[]
            if (move==claim):
                print("\nxxxxx :\n\tYou are wrong %s, the whole pile of cards is yours %s!" %(challenger,challenger))
                challenger_cards_updated=obj.add_cards(pile,challenger_cards)
                if fl==0:
                    self.player2_cards=challenger_cards_updated
                elif fl==1:
                    self.player1_cards=challenger_cards_updated
                self.pile=[]
                cont=1
                while(cont!=0):
                    cont=(input("Press enter to continue: "))
                    if cont=='':
                        obj.cls()
                        break

            else:
                print("\n^^^^^ :\n\t%s cheated!!  The whole pile of cards is yours %s" %(challenged,challenged))
                challenged_cards_updated=obj.add_cards(pile,challenged_cards)
                if fl==0:
                    self.player1_cards=challenged_cards_updated
                elif fl==1:
                    self.player2_cards=challenged_cards_updated
                self.pile=[]
                cont=1
                while(cont!=0):
                    cont=(input("Press enter to continue: "))
                    if cont=='':
                        obj.cls()
                        break
            
#define the function for the next turn to keep the status of player1's hand with the next move 
    def next_turn_player1(self,n):
        card_type=obj.get_value_asString(n)
        obj.hand_status(self.player1_cards,self.players[0])

        #Ask the player for the move and claim
        print("\nWhat do you wanna play %s?: " % self.players[0])
        player1_move_initial=input("Type your move: ").strip().split()
        player1_move=obj.strip_s(player1_move_initial)

        #Make the claim
        player1_claim=""
        count=0
        for i in range(0,len(player1_move),2):
            count+=int(player1_move[i])
        if count==1:
            player1_claim=str(count)+" "+card_type
        else:
            player1_claim=str(count)+" "+card_type+"s"

        # now, to clear the screen
        obj.cls()
        
        #remove the cards from the player1's cards according to the move played
        self.player1_cards_updated=obj.remove_cards(self.player1_cards,player1_move)

        if self.player1_cards_updated==0:
            return sum(self.player1_cards)

        self.player1_cards=[]
        self.player1_cards=self.player1_cards_updated

        #display the game status
        print("\n%s claims to have played %s" %(self.players[0],player1_claim))
        player1_claim=player1_claim.split()
        player1_claim=obj.strip_s(player1_claim)

        #Add the cards played by the player to the pile
        self.pile=self.pile+player1_move

        #call the function to operate the challenge
        obj.challenge(self.players[1],self.players[0],player1_move,player1_claim,self.player2_cards,self.player1_cards,self.pile,0)
        return sum(self.player1_cards)

#Define the function for the next turn to keep the status of player2's hand with the next move        
    def next_turn_player2(self,n):
        card_type=obj.get_value_asString(n)
        obj.hand_status(self.player2_cards,self.players[1])

        #Ask the player for the move and claim
        print("\nWhat do you wanna play %s?: " % self.players[1])
        player2_move_initial=input("Type your move: ").strip().split()
        player2_move=obj.strip_s(player2_move_initial)
        
        #Make the claim
        count=0
        player2_claim=""
        for i in range(0,len(player2_move),2):
            count+=int(player2_move[i])
        if count==1:
            player2_claim=str(count)+" "+card_type
        else:
            player2_claim=str(count)+" "+card_type+"s"
 
        # now, to clear the screen
        obj.cls()
        
        #remove the cards from the player1's cards according to the move played
        self.player2_cards_updated=obj.remove_cards(self.player2_cards,player2_move)
        if self.player2_cards_updated==0:
            return sum(self.player2_cards)
        self.player2_cards=[]
        self.player2_cards=self.player2_cards_updated

        #display the game status
        print("\n%s claims to have played: %s" %(self.players[1],player2_claim))
        player2_claim=player2_claim.split()
        player2_claim=obj.strip_s(player2_claim)

        #Add the cards played by the player to the pile
        self.pile=self.pile+player2_move

        #call the function to operate the challenge
        obj.challenge(self.players[0],self.players[1],player2_move,player2_claim,self.player1_cards,self.player2_cards,self.pile,1)
        return sum(self.player2_cards)


#Declare the winner
    def declare_winner(flag):
        if (flag==1):
            print("\n\t\t%s is Winner!" %self.players[0])
        elif (flag==2):
            print("\n\t\t%s is Winner!" %self.players[1])
          
obj=Cheat_Game()

obj.game_rules()
obj.deck()
obj.get_players()  
obj.cls()
obj.deal_deck()
obj.deal_cards()
p1=1
p2=1
while (True):
    i=0
    while (i<13):
        if(p1==0):
            flag=1
            break 
        else:
            p1=obj.next_turn_player1(i)
            i+=1
        if(p2==0):
            flag=2
            break
        else:  
            p2=obj.next_turn_player2(i)
            i+=1
obj.declare_winner(flag)
