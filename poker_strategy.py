import numpy as np

# rank of the type
type_rank = { 'HighCard':    0,
             'OnePair':      1,
             'TwoPairs':     2,
             '3ofakind':     3,
             'straight':     4,
             'flush':        5,
             'fullhouse':    6,
             '4ofakind':     7,
             'straightflush':8}


# strength of each type
hand_rank = {'2':0,
             '3':1,
             '4':2,
             '5':3,
             '6':4,
             '7':5,
             '8':6,
             '9':7,
             'T':8,
             'J':9,
             'Q':10,
             'K':11,
             'A':12}

def poker_strategy_example(opponent_hand,
                           opponent_hand_rank,
                           opponent_stack,
                           agent_action_,
                           agent_action_value,
                           agent_stack,
                           current_pot,
                           bidding_nr):

    opponent_action = None
    opponent_action_value = None

    max_phase = 8

    def compute_hand_strength(type_rank, hand_rank):
        return type_rank*13+hand_rank

    def getStrengthInterval(type_rank, hand_rank):
        strength = type_rank*13+hand_rank
        if strength <= 13: return 'weak'
        elif strength <= 13*3: return 'median'
        else: return 'strong'

    opponent_hand_strength = getStrengthInterval(opponent_hand, opponent_hand_rank)

    if bidding_nr >= max_phase:
        opponent_action = 'Call'
        opponent_action_value = 5

    elif opponent_stack >= 25:

        if opponent_hand_strength is 'weak':
            if bidding_nr < 3:
                if agent_action_value == 25:
                    opponent_action = 'Bet'
                    opponent_action_value = 10
                else:
                    opponent_action = 'Bet'
                    opponent_action_value = [10, 25][np.random.randint(2)]

            elif bidding_nr >= 3:
                if agent_action_value == 25:
                    opponent_action = 'Fold'
                    opponent_action_value = 0
                else:
                    opponent_action = 'Call'
                    opponent_action_value = 25

        elif opponent_hand_strength is 'median':
            if bidding_nr < 2:
                if agent_action_value == 25:
                    opponent_action = 'Bet'
                    opponent_action_value = 10
                else:
                    opponent_action = 'Bet'
                    opponent_action_value = 25

            elif bidding_nr >= 2:
                if agent_action_value == 25:
                    opponent_action = 'Bet'
                    opponent_action_value = 25
                else:
                    opponent_action = 'Call'
                    opponent_action_value = 5

        elif opponent_hand_strength is 'strong':
            if bidding_nr < 2:
                if agent_action_value == 25:
                    opponent_action = 'Bet'
                    opponent_action_value = 25
                else:
                    opponent_action = 'Bet'
                    opponent_action_value = 10

            elif bidding_nr >= 2:
                if agent_action_value == 25:
                    opponent_action = 'Bet'
                    opponent_action_value = 25
                else:
                    opponent_action = 'Call'
                    opponent_action_value = 5

    else:
        opponent_action = 'Call'
        opponent_action_value = 5

    return opponent_action, opponent_action_value

