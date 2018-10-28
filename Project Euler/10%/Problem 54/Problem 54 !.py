import time
start_time = time.clock()


def same_suit(player):
    suit = list(player[0]).pop()

    for card in player:
        if(list(card).pop() != suit):
            return False
    
    return True

def pair(cards):
    if(len(cards[0]) != len(cards[1])):
        return False

    ln = len(cards[0])
    if(ln==2):
        if(cards[0][0]==cards[1][0]):
            return True

    else:
        if(cards[0][1]==cards[1][1]):
            return True

    return False

def unique_card(player):
    if(player[0][:(len(player[0])-1)] != player[1][:(len(player[1])-1)]):
        return player[0][:(len(player[0])-1)]
    elif(player[2][:(len(player[2])-1)] != player[3][:(len(player[3])-1)]):
        return player[2][:(len(player[2])-1)]
    else:
        return player[4][:(len(player[4])-1)]
    

#______________________________________________________________________________________________________________________________________________________________________

def royal_flush(player):
    if not same_suit(player):
        return False

    if(player[0][:2]=="9V" and player[1][:2]=="9W" and player[2][:2]=="9X" and player[3][:2]=="9Y" and player[4][:2]=="9Z"):
        return True

    return False

def straight_flush(player):
    return (straight(player) and same_suit(player))

def four_of_a_kind(player):

    for i in xrange(2):
        if(player[i][0] == player[i+1][0]):
            length = len(player[i])
            if(player[i][0]!="9"):
                if(player[i+1][0] == player[i+2][0] and player[i+2][0] == player[i+3][0]):
                    return ("T" + player[i][0])

            else:
                if(length==3):
                    middle = player[i][1]
                    if(player[i+1][1]==middle and player[i+2][1]==middle and player[i+3][1]==middle):
                        return ("T" + player[i][:2])
                else:
                    if(len(player[i+3])==2):
                        return ("T" + player[i][0])

    return "F0"   
    
def full_house(player):
    toak = three_of_a_kind(player)
    if(toak[0] == "T"):
        tp = two_pair(player)
        if(tp[0] == "T"):
            return toak

    return "F0"    

def flush(player):
    return same_suit(player)

def straight(player):
    value_set = set([card[:(len(card)-1)] for card in player])
    if(len(value_set) < 5):
        return False    
    
    least = int(player[0][0])
    if(least<5):
        if(int(player[4][0]) == (least+4)):
            return True

    if(least == 5):
        if(len(player[4])==2 and player[4][0]==9):
            return True
    
    if(least == 6):
        if(player[4][:2] == "9V"):
            return True

    if(least == 7):
        if(player[4][:2] == "9W"):
            return True

    if(least == 8):
        if(player[4][:2] == "9X"):
            return True

    if(least == 9):
        if(len(player[0]) == 2):
            if(player[4][:2] == "9Y"):
                return True
        elif(len(player[0]) == 3):
            if(player[4][:2] == "9Z"):
                return True

    return False

def three_of_a_kind(player):

    for i in xrange(3):
        if(player[i][0] == player[i+1][0]):
            length = len(player[i])
            if(player[i][0]!="9"):
                if(player[i+1][0] == player[i+2][0]):
                    return ("T" + player[i][0])

            else:
                if(length==3):
                    middle = player[i][1]
                    if(player[i+1][1]==middle and player[i+2][1]==middle):
                        return ("T" + player[i][:2])
                else:
                    if(len(player[i+2])==2):
                        return ("T" + player[i][0])

    return "F0"

def two_pair(player):
    count = 0; i = 0
    while(i<4):
        if(pair(player[i:i+2])):
            count += 1
            i += 2
        else:
            i += 1    

    if(count>=2):
        card = player[3]
        return ("T" + card[:(len(card)-1)])

    return "F0"

def one_pair(player):
    for i in xrange(4):
        if(pair(player[i:i+2])):
            return ("T" + player[i][:(len(player[i])-1)])

    return "F0"

def high_card(player1, player2):

    count = (len(player1) - 1)
    while(count>=0):
        high1 = player1[count]
        high2 = player2[count]

        if(len(high1) > len(high2)):
            return "one"
        elif(len(high2) > len(high1)):
            return "two"

        else:
            if(high1[1]>high2[1]):
                return "one"
            elif(high2[1]>high1[1]):
                return "two"

        count -= 1    

#______________________________________________________________________________________________________________________________________________________________________

def winner(player1, player2):
    
    #royal flush
    #print "royal flush"
    if(royal_flush(player1)):
        return "one"

    if(royal_flush(player2)):
        return "two"

    #straight flush
    #print "straight flush"
    if(straight_flush(player1)):
        if(straight_flush(player2)):
            return high_card(player1, player2)

        return "one"

    if(straight_flush(player2)):
        return "two"

    #four of a kind
    #print "four of a kind"
    foak1 = four_of_a_kind(player1)
    foak2 = four_of_a_kind(player2)
    if(foak1[0] == "T"):
        if(foak2[0] == "T"):
            if(len(foak1) > len(foak2)):
                return "one"
            elif(len(foak1) < len(foak2)):
                return "two"

            else:
                if(foak1[1:] > foak2[1:]):
                    return "one"
                elif(foak1[1:] < foak2[1:]):
                    return "two"

        return "one"

    if(foak2[0] == "T"):
        return "two"

    #full house
    #print "full house"
    fh1 = full_house(player1)
    fh2 = full_house(player2)
    if(fh1[0] == "T"):
        if(fh2[0] == "T"):
            if(len(fh1) > len(fh2)):
                return "one"
            elif(len(fh1) < len(fh2)):
                return "two"

            else:
                if(fh1[1:] > fh2[1:]):
                    return "one"
                elif(fh1[1:] < fh2[1:]):
                    return "two"

        return "one"

    if(fh2[0] == "T"):
        return "two"

    #flush
    #print "flush"
    if(flush(player1)):
        if(flush(player2)):
            return high_card(player1, player2)

        return "one"

    if(flush(player2)):
        return "two"

    #straight
    #print "straight"
    if(straight(player1)):
        if(straight(player2)):
            return high_card(player1, player2)

        return "one"

    if(straight(player1)):
        return "two"

    #three of a kind
    #print "three of a kind"
    toak1 = three_of_a_kind(player1)
    toak2 = three_of_a_kind(player2)
    if(toak1[0] == "T"):
        if(toak2[0] == "T"):
            if(len(toak1) > len(toak2)):
                return "one"
            elif(len(toak1) < len(toak2)):
                return "two"

            else:
                if(toak1[1:] > toak2[1:]):
                    return "one"
                elif(toak1[1:] < toak2[1:]):
                    return "two"

        return "one"

    if(toak2[0] == "T"):
        return "two"
    
    #two pair
    #print "two pair"
    tp1 = two_pair(player1)
    tp2 = two_pair(player2)
    if(tp1[0] == "T"):
        if(tp2[0] == "T"):
            if(len(tp1) > len(tp2)):
                return "one"
            elif(len(tp1) < len(tp2)):
                return "two"

            else:
                if(tp1[1:] > tp2[1:]):
                    return "one"
                elif(tp1[1:] < tp2[1:]):
                    return "two"
                else:
                    uc1 = unique_card(player1)
                    uc2 = unique_card(player2)
                    if(uc1 > uc2):
                        return "one"
                    else:
                        return "two"

        return "one"

    if(tp2[0] == "T"):
        return "two"

    #one pair
    #print "one pair" 
    p1 = one_pair(player1)
    p2 = one_pair(player2)
    if(p1[0] == "T"):
        if(p2[0] == "T"):
            if(len(p1) > len(p2)):
                return "one"
            elif(len(p1) < len(p2)):
                return "two"

            else:
                if(p1[1:] > p2[1:]):
                    return "one"
                elif(p1[1:] < p2[1:]):
                    return "two"
                else:
                    return high_card(player1, player2)

        return "one"

    if(p2[0] == "T"):
        return "two"

    #high card
    #print "high card"
    return high_card(player1, player2)
    
    
if __name__ == "__main__":
    
    fp = open("p054_poker.txt", "r")
    hands = fp.read().split("\n")
    hands.pop()


    win_one = -7; win_two = 7

    for hand in hands:
        player1 = (hand[:14]).split()
        player2 = (hand[15:]).split()

        for index in xrange(5):
            card1 = player1[index]
            card2 = player2[index]
            
            card1 = card1.replace("T", "9V")
            card1 = card1.replace("J", "9W")
            card1 = card1.replace("Q", "9X")
            card1 = card1.replace("K", "9Y")
            card1 = card1.replace("A", "9Z")

            card2 = card2.replace("T", "9V")
            card2 = card2.replace("J", "9W")
            card2 = card2.replace("Q", "9X")
            card2 = card2.replace("K", "9Y")
            card2 = card2.replace("A", "9Z")

            player1[index] = card1
            player2[index] = card2
        
            
        player1.sort()
        player2.sort()

        #print player1, player2
        #break

        if(winner(player1, player2) == "one"):
            win_one += 1
        if(winner(player1, player2) == "two"):
            win_two += 1    

    print win_one, win_two        
    
print "Execution time: %.4f" %(time.clock() - start_time) + " sec"

#______________________________________________________________________________________________________________________________________________________________________

# test

##hands = ["2H 6H 4H 3H 5H AS KS QS TS JS"]
##player1 = (hands[0][:14]).split()
##player2 = (hands[0][15:]).split()
###print player1, player2
##
##for index in xrange(5):
##    card1 = player1[index]
##    card2 = player2[index]
##    
##    card1 = card1.replace("T", "9V")
##    card1 = card1.replace("J", "9W")
##    card1 = card1.replace("Q", "9X")
##    card1 = card1.replace("K", "9Y")
##    card1 = card1.replace("A", "9Z")
##
##    card2 = card2.replace("T", "9V")
##    card2 = card2.replace("J", "9W")
##    card2 = card2.replace("Q", "9X")
##    card2 = card2.replace("K", "9Y")
##    card2 = card2.replace("A", "9Z")
##
##    player1[index] = card1
##    player2[index] = card2
##
##    
##player1.sort()
##player2.sort()
##
##print player1, player2
##print straight(player1), straight(player2)
##print straight_flush(player1), straight_flush(player2)
##print royal_flush(player1), royal_flush(player2)
###print two_pair(player1), two_pair(player2)
##print winner(player1, player2)

