import numpy as np

def minimax_decision():

    return np.argmax()

def max_value(state):
    if terminal_test(state):
        return utility(state)
    v = -1
    for a in get_actions(state):
        s = "state"
        v =np.max(v,min_value(result(s,a)))
    return v

def terminal_test(state):
    return False

def utility(state):
    return None

def get_actions(state):
    return []

def min_value(state):
    if terminal_test(state):
        return utility(state)
    v=-1
    for a in get_actions(state):
        s = "state"
        v =np.min(v,min_value(result(s,a)))
    return v

def result(s,a):
    return 0
