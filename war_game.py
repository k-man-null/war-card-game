import card_util as cu
import game_util as gu

def play():

  # creating the standard deck
  standard_deck = cu.create_std_deck()

  # shuffling the deck 7 times
  cu.shuffle_cards(standard_deck)

  # dealing 26 cards from the standard deck to the computer
  computer_hand = cu.deal_cards_from(standard_deck, 26)

  # dealing 26 cards from the standard deck to the user
  player_hand = cu.deal_cards_from(standard_deck, 26)

  # initializing gaming option
  play_again = "Y"

  # printing game message
  print("=" *60)
  print("%20s%-50s%20s" % ("", "IT'S TIME FOR WAR AGAINST GREED!", ""))
  print("=" *60)

  # round counter
  ronda = 1

  # while the user does not enter 'Q' or 'q'
  while play_again != "Q" and play_again != "q":

    # printing the round number
    print( "\n"+ "=" * 20 + "Round #" +str(ronda) + "=" * 20)

    # removing a card from the computer hand
    comp_card = computer_hand.pop()
    # removing a card from the user hand
    player_card = player_hand.pop()

    # printing the computer deck, face-down
    print("Computer plays....")
    cu.print_deck(computer_hand, False)

    # printing the computer's playing card face-up
    comp_card.print_card()

    # printing the user deck, face-down
    print("\nYou play...")
    cu.print_deck(player_hand, False)

    # printing the user's playing card face-up
    player_card.print_card()

    # keeping a list of the cards that are currently up for grabs
    at_stake = [player_card, comp_card]

    # if the user's card is an ace
    if player_card.get_rank() == 1 and comp_card.get_rank() != 1:
      print("You've got an unbeatable ACE! You WIN this battle!")
      # adding the cards to the user's hand
      player_hand.extend(at_stake)
      #shuffling the user's hand
      cu.shuffle_cards(player_hand)


    # if the computer's card is an ace
    elif player_card.get_rank()  != 1 and comp_card.get_rank()  == 1:
      print("Can't win against an ACE! You LOSE this battle!")
      # adding the cards to the computer's hand
      computer_hand.extend(at_stake)
      # shuffling the computer's hand
      cu.shuffle_cards(computer_hand)

    # if the ranks of both cards are the same  
    elif player_card == comp_card:
      print("This means WAR!! ...")
      print("Cards up for grabs:", len(at_stake))
      at_war = True

      while(at_war):
        
        # getting the computer's War cards and printing the appropriate amount of X's
        print("\nComputer's war hand...")
        comp_war_hand = gu.get_war_hand(computer_hand)
        
        # the first card of the computer's War hand is its playing card
        c_war_card = comp_war_hand[0]

        # printing the computer's playing War card
        c_war_card.print_card()

        # adding the computer's War cards the pile that is up for grabs
        cu.add_cards_to(at_stake, comp_war_hand)
        print("Cards up for grabs:", len(at_stake))
   
        # getting the user's War cards and printing the appropriate amount of X's
        print("\nYour war hand...")
        player_war_hand = gu.get_war_hand(player_hand)
        
        # the first card of the user's War hand is their playing card
        p_war_card = player_war_hand[0]
        p_war_card.print_card()
        

        # adding the user's War cards the pile that is up for grabs
        cu.add_cards_to(at_stake, player_war_hand)
        print("Total cards up for grabs:", len(at_stake))

        # if the user's War card has a higher rank
        if p_war_card > c_war_card:
          print("\nYou WIN this WAR!")
          # print("FIXME: FINISH IMPLEMENTATION!")
          # adding the cards to the user's hand
          player_hand.extend(at_stake)
          #shuffling the user's hand
          cu.shuffle_cards(player_hand)

          at_war = False

        # if the computer's War card has a higher rank
        elif p_war_card < c_war_card:
          print("\nYou LOSE this WAR!")
          # print("FIXME: FINISH IMPLEMENTATION!")
          # adding the cards to the computer's hand
          computer_hand.extend(at_stake)
          #shuffling the deck
          cu.shuffle_cards(computer_hand)
          at_war = False

        # if both playing War cards have the same rank
        else:
          if len(player_hand) > 0 and len(computer_hand) > 0:
            print("\nThis WAR IS NOT OVER!!!\nEntering ANOTHER WAR ROUND...\n")
          else:
            print("One of you does NOT have any more cards to play...")
            at_war = False


    # if the user's card has a higher rank
    elif player_card > comp_card:
      print("You WIN this battle!")
      #print("FIXME: FINISH IMPLEMENTATION!")
      # adding the cards to the user's hand
      player_hand.extend(at_stake)
      #shuffling the user's hand
      cu.shuffle_cards(player_hand)
    
    # if the user's card has a lower rank
    else:
      print("The computer has OUT-RANKED you,\nBUT you might still have an opportunity to win this battle.\nJust be wise and don't get too greedy...")
      play_sc = input("\nWould you like to PLAY A SECOND card? Y/N: ").strip().upper()
      
      # if the user decides to play a second card
      if play_sc == "Y":
        #print("FIXME: FINISH IMPLEMENTATION!")
        #print the second card
        print("Your response : ", play_sc)
        print("Your second card:")
        #play the second card
        player_card2 = player_hand.pop()
        #add the second card to the pile that is up for grabs
        at_stake.append(player_card2)
        player_card2.print_card()
        #sum of the two cards
        sum_cards = player_card2.get_rank() + player_card.get_rank()
        print("Sum of the ranks: ", sum_cards)

        if sum_cards <= at_stake[1].get_rank():
          print("Nice play! You SAVED yourself in this round!")
          #print player hand

          # adding the cards to the user's hand
          player_hand.extend(at_stake)
          #shuffling the user's hand
          cu.shuffle_cards(player_hand)

        else:
          print("OOF! You got GREEDY and for that you LOSE BOTH cards!")
          # adding the cards to the computer's hand
          computer_hand.extend(at_stake)
          #shuffling the deck
          cu.shuffle_cards(computer_hand)

      # if the user decides to NOT play a second card
      else:
        print("You LOSE this round but at least its only one card.")
        cu.add_cards_to(computer_hand, at_stake)
        cu.shuffle_cards(computer_hand)
    

    print("\nYour deck size:", len(player_hand))
    print("Computer deck size:", len(computer_hand))

    ronda += 1
    if len(player_hand) == 0:
      print("You have NO MORE CARDS, so sadly, YOU LOSE THE GAME.")
      print("COMPUTER WINS!")
      break
    elif len(computer_hand) == 0:
      print("Computer has NO MORE CARDS, so, YOU WIN THE GAME!!!")
      break
    else:
      play_again = input("\nPress any key to play again or 'Q' to quit: ").strip().upper()
