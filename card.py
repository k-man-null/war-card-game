class Card:

  def __init__(self, rank, suit):
    self.suit = suit
    self.rank = rank
    return

  def get_suit(self):
    """
    gets the suit of this Card
    OUTPUT: the suit as a string
    """
    return str(self.suit)
    

  def get_rank(self):
    """
    gets the rank of this Card
    OUTPUT: the rank as an integer
    """
    return int(self.rank)

  def print_card(self):
    """
    prints the card formatted so that the rank symbol is displayed at opposite corners, and the suit symbol is displayed at the center.
    """
    card_str = self.__str__()
    if len(card_str) == 2:
        blank_card =  "┌─────────┐\n" 
        blank_card += "│%s        │\n"
        blank_card += "│         │\n"
        blank_card += "│         │\n"
        blank_card += "│    %s    │\n"
        blank_card += "│         │\n"
        blank_card += "│         │\n"
        blank_card += "│       %s │\n"
        blank_card += "└─────────┘\n"
        both_symbols = [card_str[0], card_str[1]]
        
    else:
        blank_card =  "┌─────────┐\n" 
        blank_card += "│%s       │\n"
        blank_card += "│         │\n"
        blank_card += "│         │\n"
        blank_card += "│    %s    │\n"
        blank_card += "│         │\n"
        blank_card += "│         │\n"
        blank_card += "│       %s│\n"
        blank_card += "└─────────┘\n"
        both_symbols = [card_str[0:2], card_str[2]]
        
    print(blank_card % (both_symbols[0], both_symbols[1], both_symbols[0]))
    return

  def __str__(self):
    """
    returns the string representation of this Card.
    The string includes the appropriate card rank symbol i.e. A, 2, 3, ..., 10, J, K, or Q, and the suit symbol.
    OUTPUT: a string containing the rank symbol and the suit symbol
    """
    return Card._get_rank_symbol(self.rank) + Card._get_suit_symbol(self.suit)


  def __lt__(self, other):
    """
    overloads the < operator by comparing the rank of this Card to the rank of the other Card
    INPUT:
          - other : the other object to compare to, i.e.   this Card < other
    OUTPUT: Boolean value 
          - returns True if this Card is compared to another Card object, and the rank of this Card is smaller than the rank of the other Card object, keeping in mind that an ace, although rank 1, is regarded as higher rank when compared by itself;
          - returns False otherwise
    """
    if isinstance(other, Card):
      if self.rank < other.rank:
        return True
    else:
      raise TypeError("Can not compare Card to" + type(other))



  def __gt__(self, other):
    """
    overloads the > operator by comparing the rank of this Card to the rank of the other Card
    INPUT:
          - other : the other object to compare to, i.e.   this Card > other
    OUTPUT: Boolean value 
          - returns True if this Card is compared to another Card object, and the rank of this Card is greater than the rank of the other Card object, keeping in mind that an ace, although rank 1, is regarded as higher rank when compared by itself;
          - returns False otherwise
    """
    if isinstance(other, Card):
      if self.rank > other.rank:
        return True
    else:
      raise TypeError("Can not compare Card to" + type(other))


  def __eq__(self, other):
    """
    overloads the == operator by comparing the rank of this Card to the rank of the other Card
    INPUT:
          - other : the other object to compare to, i.e.   this Card == other
    OUTPUT: Boolean value 
          - returns True if this Card is compared to another Card object, and the ranks of both cards are the same
          - returns False otherwise
    """
    if isinstance(other, Card):
      if self.rank == other.rank:
        return True
    else:
      raise TypeError("Can not compare Card to" + type(other))


  def _get_rank_symbol(rank):
    """
    gets the rank symbol A, 2, 3, ..., 10, J, K, or Q that corresponds to the given integer rank
    INPUT: rank - the rank of this Card as an integer
    OUTPUT: 
          - if the given rank is in the range 1 - 13, returns the rank symbol A, 2, 3, ..., 10, J, Q, or K as a string
          - otherwise returns the string "Invalid rank"
    """
    if rank in range(1, 14):
      if rank == 1:
        return "A"
      elif rank == 11:
        return "J"
      elif rank == 12:
        return "Q"
      elif rank == 13:
        return "K"
      else:
        return str(rank)
    else:
      return "Invalid rank."

  def _get_suit_symbol(suit):
    """
    helper method; retrieves the correct Unicode codepoint character for the given suit
    INPUT: suit - the suit name of this Card as a string
    OUTPUT: the suit symbol as a string
    """
    if suit.upper() == 'HEARTS':
      return "\u2665"
    elif suit.upper() == 'SPADES':
      return "\u2660"
    elif suit.upper() == 'DIAMONDS':
      return "\u2666"
    elif suit.upper() == 'CLUBS':
      return "\u2663"
    else:
      return "Invalid suit."