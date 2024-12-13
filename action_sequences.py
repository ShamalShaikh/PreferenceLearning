import spot
import numpy as np

# Define the LTL formula (from previous step)
ltl_formula = spot.formula('F A && G B')

# Convert LTL to Büchi Automaton using Spot
ba = ltl_formula.translate()

# Display the automaton
print("Büchi Automaton:")
print(ba.to_str('hoa'))

# Simple MDP representation (states, actions, transitions)
mdp_states = ['s0', 's1', 's2']
mdp_actions = ['a0', 'a1']
mdp_transitions = {
    ('s0', 'a0'): 's1',
    ('s0', 'a1'): 's2',
    ('s1', 'a0'): 's2',
    ('s1', 'a1'): 's0',
    ('s2', 'a0'): 's0',
    ('s2', 'a1'): 's1',
}

# Construct the Product MDP
product_states = []
for mdp_state in mdp_states:
    for ba_state in ba.get_states():
        product_states.append((mdp_state, ba_state))

print("\nProduct MDP States:")
for state in product_states:
    print(state)
