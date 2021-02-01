# author: Adam Nowakowski


def minimax(state, search_depth, successor_fun, heuristics):
    """
    The minimax algorithm implementation
    :param state: initializing state
    :param search_depth: depth of the search for the next states
    :param successor_fun: successor function object
    :param heuristics: heuristics function object
    :return: payment for initial state
    """

    if state['is_terminal'] or search_depth == 0:
        out = heuristics(state)
    else:
        next_states = successor_fun(state)
        for next_state in next_states:
            next_state['payment'] = minimax(next_state, search_depth-1, successor_fun, heuristics)
        payments = [n_st['payment'] for n_st in next_states]
        if state['max_move']:
            out = max(payments)
        else:
            out = min(payments)

    return out
