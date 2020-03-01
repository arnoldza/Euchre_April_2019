###############################################################################
#   Honors Project #2
#       
#   Algorithm
#       Play games of euchre
#           Prints game data into text file
#       Prompts user for integer of additional rounds to play
#           Prints statistics over number of rounds
#
###############################################################################

import cards, players2, random

dict_suits = {0: "None", 1: "Clubs", 2: "Diamonds", 3: "Hearts", 4: "Spades"}

player1 = players2.AmazingPlayer()
player2 = players2.StrategyPlayer()
player3 = players2.AmazingPlayer()
player4 = players2.StrategyPlayer()
# assigns players to amazing or strategy classes

player_dict = {
    player1: "Player 1", player2: "Player 2", player3: "Player 3", player4: "Player 4"}

layout_new = '''

                 Player 3
                  {:s}
                
      Player 2              Player 4
       {:s}                      {:s}
                
                 Player 1
                  {:s}



'''

header = '''
        
        
     TURN = {:d}
-------------------------------------------------------------------------------
        
'''

data = '''
MULTI-PLAY STATISTICS
---------------------


NUMBER OF ROUNDS -> {:d}

AVERAGE SCORE ->  1) Team One (Amazing)  = {:.2f}
                  2) Team Two (Strategy)   = {:.2f}
                  3) Both Teams           = {:.2f}
    
MEDIAN SCORES ->  1) Team One (Amazing)  = {:.2f}
                  2) Team Two (Strategy)   = {:.2f}
                  3) Both Teams           = {:.2f}

HIGHEST SCORES -> 1) Team One (Amazing)  = {:.2f}
                  2) Team Two (Strategy)   = {:.2f}

LOWEST SCORES ->  1) Team One (Amazing)  = {:.2f}
                  2) Team Two (Strategy)   = {:.2f}
    
    
Team One Won {:.2f}% of the Time

while...

Team Two Won {:.2f}% of the Time

therefore...

{:s}
    
'''

trump_clubs = [cards.Card(9, 1), cards.Card(10, 1), cards.Card(12, 1), cards.Card(
    13, 1), cards.Card(1, 1), cards.Card(11, 4), cards.Card(11, 1)]
trump_diamonds = [cards.Card(9, 2), cards.Card(10, 2), cards.Card(12, 2), cards.Card(
    13, 2), cards.Card(1, 2), cards.Card(11, 3), cards.Card(11, 2)]
trump_hearts = [cards.Card(9, 3), cards.Card(10, 3), cards.Card(12, 3), cards.Card(
    13, 3), cards.Card(1, 3), cards.Card(11, 2), cards.Card(11, 3)]
trump_spades = [cards.Card(9, 4), cards.Card(10, 4), cards.Card(12, 4), cards.Card(
    13, 4), cards.Card(1, 4), cards.Card(11, 1), cards.Card(11, 4)]
list_trumps = [trump_clubs, trump_diamonds, trump_hearts, trump_spades]


# rankings of cards based on trump

def single_play(boolean, play):
    '''
    Function to run one full game of euchre
    
    Inputs:
        boolean -> if True, strategy players begin game
                    if False, amazing players begin game
        play -> if "single", game prints out all details for the game into
                file called single_play.txt
    
    Returns:
        None
    '''

    if play == "single":
        fp = open("single_play.txt", "w")

        fp.write("\nPlayer 1 and Player 3 are Amazing Players\n\n")
        fp.write("Player 2 and Player 4 are Strategy Players\n\n")
        fp.write("Team One -> Player 1 and Player 3\n\n")
        fp.write("Team Two -> Player 2 and Player 4\n\n")

    if boolean == True:
        player_lst = [player1, player2, player3, player4]
    elif boolean == False:
        player_lst = [player2, player3, player4, player1]

    team_one_points = 0
    team_two_points = 0
    turn = 1
    rotation = 0  # Initializes all scoring system and round system to 0,1

    while team_one_points < 10 and team_two_points < 10:

        if play == "single":
            fp.write(header.format(turn))

            if rotation == 0:
                fp.write(layout_new.format("", "", "Dealer", "Lead"))
            elif rotation == 1:
                fp.write(layout_new.format("", "Lead", "", "Dealer"))
            elif rotation == 2:
                fp.write(layout_new.format("Lead", "Dealer", "", ""))
            else:
                fp.write(layout_new.format("Dealer", "", "Lead", ""))
            # This will display in text file the roles of each player that round

        rank_clubs = [cards.Card(9, 1), cards.Card(10, 1), cards.Card(11, 1
                                                                      ), cards.Card(12, 1), cards.Card(13, 1),
                      cards.Card(1, 1)]
        rank_diamonds = [cards.Card(9, 2), cards.Card(10, 2), cards.Card(11, 2
                                                                         ), cards.Card(12, 2), cards.Card(13, 2),
                         cards.Card(1, 2)]
        rank_hearts = [cards.Card(9, 3), cards.Card(10, 3), cards.Card(11, 3
                                                                       ), cards.Card(12, 3), cards.Card(13, 3),
                       cards.Card(1, 3)]
        rank_spades = [cards.Card(9, 4), cards.Card(10, 4), cards.Card(11, 4
                                                                       ), cards.Card(12, 4), cards.Card(13, 4),
                       cards.Card(1, 4)]
        list_ranks = [rank_clubs, rank_diamonds, rank_hearts, rank_spades]
        # rankings of cards based on non trump

        euchre_deck = cards.Deck()
        euchre_deck.euchre_deck()
        euchre_deck.shuffle()

        trump = 0

        player1.__init__()
        player2.__init__()
        player3.__init__()
        player4.__init__()  # initializes each player

        i = 0
        while i != 21:  # Deals each player cards
            top_deck = euchre_deck.deal()
            if i in range(0, 5):
                player_lst[0].take_card(top_deck)
            elif i in range(5, 10):
                player_lst[1].take_card(top_deck)
            elif i in range(10, 15):
                player_lst[2].take_card(top_deck)
            elif i in range(15, 20):
                player_lst[3].take_card(top_deck)
            else:
                potential_trump = top_deck
            i += 1

        if play == "single":
            fp.write("* {:s} deals the cards".format(player_dict[player_lst[3]]
                                                     ) + "\n\n\n")  # Writes in dealer to text file

        player_lst[3].is_dealer(True)
        player_lst[0].is_lead(True)
        player_lst[1].is_teammate_dealer(True)  # Assigns players roles

        for j in range(4):  # First Round of bidding
            if player_lst[j].first_round(potential_trump) == True:
                player_lst[j].is_maker(True)
                # Assigns player and teammate as Makers
                try:
                    player_lst[j + 2].is_maker(True)
                except IndexError:
                    player_lst[j - 2].is_maker(True)

                player_lst[3].take_card(potential_trump)
                player_lst[3].remove_card()

                trump = potential_trump.suit()
                if play == "single":
                    fp.write("* Player {:d} Took Kitty\n\n".format(j + 1))
                    fp.write("Trump -> {:s}\n\n\n".format(dict_suits[trump]))
                break
            else:
                j += 1

        if trump == 0:
            for k in range(4):  # Second Round of bidding
                if player_lst[k].second_round(potential_trump.suit()) != False:
                    player_lst[k].is_maker(True)
                    # Assigns player and teammate as Makers
                    try:
                        player_lst[k + 2].is_maker(True)
                    except IndexError:
                        player_lst[k - 2].is_maker(True)
                    trump = player_lst[k].second_round(potential_trump.suit())
                    if play == "single":
                        fp.write("* Player {:d} Chose {:s}\n\n".format(
                            k + 1, dict_suits[trump]))
                        fp.write("Trump -> {:s}\n\n\n".format(dict_suits[trump]
                                                              ))
                    break
                else:
                    k += 1

        if play == "single":
            fp.write("Player 1's Hand = " + str(player1.show_deck()) + "\n")
            fp.write("Player 2's Hand = " + str(player2.show_deck()) + "\n")
            fp.write("Player 3's Hand = " + str(player3.show_deck()) + "\n")
            fp.write("Player 4's Hand = " + str(player4.show_deck()) + "\n\n\n")
            # Shows all players hands in text file

        for m in range(4):  # Assigns Trump
            player_lst[m].assign_trump_suit(trump)

        if play == "single":
            if trump == 0:  # If all players passed both rounds, new turn starts
                fp.write("All players passed both rounds, new turn begins\n\n")

        if trump != 0:  # If trump has been assigned

            if play == "single":
                fp.write("* {:s}".format(
                    player_dict[player_lst[0]]) + " leads for this turn.\n\n")

            for i in range(4):  # Creates Ranking system based off of Trump
                list_ranks[i] += list_trumps[trump - 1]

            for j in range(6):
                list_ranks[trump - 1][j] = 0

            if trump == 1:
                rank_spades[2] = 0
            elif trump == 2:
                rank_hearts[2] = 0
            elif trump == 3:
                rank_diamonds[2] = 0
            else:
                rank_clubs[2] = 0

            if player_lst[3].play_alone(trump) == False:
                # Dealer does not play alone

                if play == "single":
                    fp.write(
                        "* The dealer ({:s}) decided to NOT play alone.\n\n".format(player_dict[
                                                                                        player_lst[3]]))

                trick_order = []
                for player in player_lst:
                    trick_order.append(player)

                for p in range(5):  # range 5 is number of tricks to play

                    if play == "single":
                        fp.write("\nTrick {:d}".format(p + 1) + "\n\n")

                    round_cards = []
                    round_points = []

                    round_cards.append(trick_order[0].play_card_lead(trump))
                    # Plays Card for lead

                    for n in range(1, 4):
                        round_cards.append(trick_order[n].play_card_not_lead(
                            round_cards[0].suit()))  # plays cards for rest of group

                    if play == "single":
                        for card in range(4):
                            fp.write("{:s} played {:s}".format(player_dict[
                                                                   trick_order[card]],
                                                               round_cards[card].__str__()) + "\n")
                    # writes player moves in text file

                    for i in round_cards:

                        if i.suit() == 1:
                            round_points.append(rank_clubs.index(i))
                        elif i.suit() == 2:
                            round_points.append(rank_diamonds.index(i))
                        elif i.suit() == 3:
                            round_points.append(rank_hearts.index(i))
                        else:
                            round_points.append(rank_spades.index(i))

                    trick_order[round_points.index(max(round_points))
                    ].add_point()  # adds a point to the player with the highest rank card

                    if play == "single":
                        fp.write("\n{:s} wins Trick!!!\n\n\n".format(
                            player_dict[trick_order[round_points.index(max(round_points))]]))

                    if trick_order[round_points.index(max(round_points))
                    ] == player1:
                        trick_order = [player1, player2, player3, player4]
                    elif trick_order[round_points.index(max(round_points))
                    ] == player2:
                        trick_order = [player2, player3, player4, player1]
                    elif trick_order[round_points.index(max(round_points))
                    ] == player3:
                        trick_order = [player3, player4, player1, player2]
                    elif trick_order[round_points.index(max(round_points))
                    ] == player4:
                        trick_order = [player4, player1, player2, player3]
                    # Changes order of play based on who won previous trick

                total_team_points = [player1.return_points(
                ) + player3.return_points(), player2.return_points() + player4.return_points()]

                if total_team_points[0] == 3 or total_team_points[0] == 4:
                    # Adds points according to whether or not players are makers
                    if player1.return_maker() == True:
                        team_one_points += 1
                    else:
                        team_one_points += 2

                elif total_team_points[0] == 5:
                    team_one_points += 2


                elif total_team_points[1] == 3 or total_team_points[1] == 4:
                    if player2.return_maker() == True:
                        team_two_points += 1
                    else:
                        team_two_points += 2

                elif total_team_points[1] == 5:
                    team_two_points += 2


            else:  # Dealer plays alone

                if play == "single":
                    fp.write(
                        "* The dealer ({:s}) decided to play alone.\n\n".format(player_dict[player_lst[
                            3]]))

                trick_order = []
                trick_order.append(player_lst[0])
                trick_order.append(player_lst[2])
                trick_order.append(player_lst[3])

                for p in range(5):  # Number of tricks to play

                    if play == "single":
                        fp.write("\nTrick {:d}".format(p + 1) + "\n\n")

                    round_cards = []
                    round_points = []

                    round_cards.append(trick_order[0].play_card_lead(trump))

                    for n in range(1, 3):
                        round_cards.append(trick_order[n].play_card_not_lead(
                            round_cards[0].suit()))

                    if play == "single":
                        fp.write("{:s} played {:s}".format(player_dict[
                                                               trick_order[0]], round_cards[0].__str__()) + "\n")
                        fp.write("{:s} played {:s}".format(player_dict[
                                                               trick_order[1]], round_cards[1].__str__()) + "\n")
                        fp.write("{:s} played {:s}".format(player_dict[
                                                               trick_order[2]], round_cards[2].__str__()) + "\n")
                    # writes player moves in text file

                    for i in round_cards:

                        if i.suit() == 1:
                            round_points.append(rank_clubs.index(i))
                        elif i.suit() == 2:
                            round_points.append(rank_diamonds.index(i))
                        elif i.suit() == 3:
                            round_points.append(rank_hearts.index(i))
                        else:
                            round_points.append(rank_spades.index(i))

                    trick_order[
                        round_points.index(max(round_points))].add_point()
                    # adds a point to the player with the highest rank card

                    if play == "single":
                        fp.write("\n{:s} wins Trick!!!\n\n\n".format(
                            player_dict[trick_order[round_points.index(max(round_points))]]))

                    if trick_order[round_points.index(max(round_points))
                    ] == player_lst[0]:
                        trick_order = [player_lst[0], player_lst[2
                        ], player_lst[3]]
                    elif trick_order[round_points.index(max(round_points))
                    ] == player_lst[2]:
                        trick_order = [player_lst[2], player_lst[3
                        ], player_lst[0]]
                    elif trick_order[round_points.index(max(round_points))
                    ] == player_lst[3]:
                        trick_order = [player_lst[3], player_lst[0
                        ], player_lst[2]]
                    # changes order of play based on who won previous trick

                total_team_points = [player1.return_points(
                ) + player3.return_points(), player2.return_points() + player4.return_points()]

                if total_team_points[0] == 3 or total_team_points[0] == 4:
                    # Adds points according to whether or not players are makers
                    if player1.return_maker() == True:
                        team_one_points += 1
                    else:
                        team_one_points += 2

                elif total_team_points[0] == 5:
                    if player_lst[3] == player1 or player_lst[3] == player3:
                        team_one_points += 4
                    else:
                        team_one_points += 2


                elif total_team_points[1] == 3 or total_team_points[1] == 4:
                    if player2.return_maker() == True:
                        team_two_points += 1
                    else:
                        team_two_points += 2

                elif total_team_points[1] == 5:
                    if player_lst[3] == player2 or player_lst[3] == player4:
                        team_two_points += 4
                    else:
                        team_two_points += 2

        player_lst += [player_lst.pop(0)]  # Rotate players for assignment
        turn += 1  # next turn
        if rotation < 3:
            rotation += 1
        else:
            rotation = 0  # changes assignment

        if play == "single":
            fp.write("-" * 23)
            fp.write("\n\nTeam One's Points -> {:d}\n\n".format(
                team_one_points))
            fp.write("Team Two's Points -> {:d}\n\n".format(team_two_points))
        # write points of each team in text file after turn

    if play == "single":
        fp.write("-" * 80)
        if team_one_points >= 10:
            fp.write("\n\nTEAM ONE WINS!!!!")

        elif team_two_points >= 10:
            fp.write("\n\nTEAM TWO WINS!!!!")

        fp.close()  # close text file

    return (team_one_points, team_two_points)


def multi_play(rounds):
    '''
    Runs through single_play function multiple times
    Writes statistics for games in file called multiple_play.txt
    
    
    Input:
        rounds -> number of rounds to play
        
    Returns:
        None
    '''
    fp = open("multiple_play.txt", "w")
    scores_lst = []
    for i in range(int(rounds)):
        random.seed(i)
        boolean = random.choice([True, False])
        scores = single_play(boolean, "multi")
        # plays single_play multiple times
        scores_lst.append(scores)

    one_total_points = 0
    two_total_points = 0
    lst_one_scores = []
    lst_two_scores = []
    one_total_wins = 0
    two_total_wins = 0

    for i in scores_lst:
        one_total_points += i[0]
        two_total_points += i[1]
        lst_one_scores.append(i[0])
        lst_two_scores.append(i[1])
        if i[0] > i[1]:
            one_total_wins += 1
        elif i[1] > i[0]:
            two_total_wins += 1

    full_lst = lst_one_scores + lst_two_scores

    lst_one_scores.sort()
    lst_two_scores.sort()
    full_lst.sort()

    if len(lst_one_scores) % 2 == 1:
        median_one = lst_one_scores[len(lst_one_scores) // 2]
    else:
        median_one = (lst_one_scores[len(lst_one_scores) // 2] + lst_one_scores[
            len(lst_one_scores) // 2 - 1]) / 2

    if len(lst_two_scores) % 2 == 1:
        median_two = lst_two_scores[len(lst_two_scores) // 2]
    else:
        median_two = (lst_two_scores[len(lst_two_scores) // 2] + lst_two_scores[
            len(lst_two_scores) // 2 - 1]) / 2

    median_full = (full_lst[len(full_lst) // 2] + full_lst[len(full_lst) // 2 - 1]
                   ) / 2

    try:
        ratio_wins = "The Amazing Team Wins {:.2f} Times as Often as the Strat\
egy Team".format(one_total_wins / two_total_wins)
    except:
        ratio_wins = "The Amazing Team Won Every Time!"

    fp.write(data.format(int(rounds), one_total_points / int(rounds
                                                             ), two_total_points / int(rounds),
                         (one_total_points + two_total_points) / (2 * int(
                             rounds)), median_one, median_two, median_full, lst_one_scores[len(
            lst_one_scores) - 1], lst_two_scores[len(lst_two_scores) - 1], lst_one_scores[0
                         ], lst_two_scores[0], one_total_wins * 100 / int(rounds), two_total_wins * 100 / int(
            rounds), ratio_wins))
    # Writes in statistics to multiple_play.txt

    fp.close()  # close multiple_play.txt


def main():
    '''
    Prompts user for number of rounds to play for multi_play
    
    Input:
        None
        
    Return:
        None
    '''
    number_rounds = input("Please enter number of rounds to be played during Multi-Play: ")
    single_play(True, "single")
    multi_play(number_rounds)


main()  # plays main function
