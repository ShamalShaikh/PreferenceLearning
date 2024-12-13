# import spot
# import networkx as nx
# import random

# # Step 1: Natural Language to LTL Formula
# def natural_language_to_ltl(nl_input):
#     """Convert natural language to an LTL formula."""
#     phrase_to_ltl = {
#         "eventually": "F",
#         "always": "G",
#         "next": "X",
#         "until": "U",
#         "and": "&&",
#         "or": "||",
#         "not": "!",
#     }

#     tokens = nl_input.lower().split()
#     ltl_formula = ""

#     for token in tokens:
#         if token in phrase_to_ltl:
#             ltl_formula += phrase_to_ltl[token] + " "
#         else:
#             ltl_formula += token.upper() + " "  # Assume propositions

#     return ltl_formula.strip()

# # Step 2: Generate Product MDP from LTL Formula
# def generate_product_mdp(ltl_formula):
#     """Generate a Büchi automaton from an LTL formula."""
#     # Translate LTL formula to Büchi automaton using Spot
#     automaton = spot.translate(ltl_formula, 'buchi', 'sbacc').to_str('spin')
#     # print(spot.formula('GFa -> GFb').translate('BA').to_str('spin'))
#     print(f"Büchi Automaton:\n{automaton}")

#     # Create a mock MDP using NetworkX
#     mdp = nx.DiGraph()
#     states = ["s0", "s1", "s2"]
#     actions = ["a", "b"]

#     # Add states and transitions
#     for state in states:
#         for action in actions:
#             next_state = random.choice(states)
#             mdp.add_edge(state, next_state, action=action)

#     return mdp, automaton

# # Step 3: Verify Trajectories
# def verify_trajectory(mdp, trajectory, ltl_formula):
#     """Verify a trajectory against an LTL formula."""
#     # Translate LTL formula to Büchi automaton
#     automaton = spot.translate(ltl_formula)
#     is_valid = True

#     # Check each step in the trajectory
#     for i, (state, action) in enumerate(trajectory):
#         print(f"Step {i}: State={state}, Action={action}")
#         if state not in mdp:
#             is_valid = False
#             break

#     return is_valid

# # Example Usage
# if __name__ == "__main__":
#     # Convert natural language to LTL
#     nl_input = "eventually A and always B"
#     ltl_formula = natural_language_to_ltl(nl_input)
#     print(f"Natural Language Input: {nl_input}")
#     print(f"LTL Formula: {ltl_formula}")

#     # Generate product MDP
#     mdp, automaton = generate_product_mdp(ltl_formula)
#     print("Generated MDP:")
#     for edge in mdp.edges(data=True):
#         print(edge)

#     # Step 3: Verify a sample trajectory
#     sample_trajectory = [("s0", "a"), ("s1", "b"), ("s2", "a")]
#     is_valid = verify_trajectory(mdp, sample_trajectory, ltl_formula)
#     print(f"Is the trajectory valid? {'Yes' if is_valid else 'No'}")



import spot
dir(spot)
gcount = 0
# def countg(f):
#     global gcount
#     print(f)
#     if f._is(spot.op_G):
#         gcount += 1
#     return f.is_sugar_free_ltl()

# f = spot.formula("FGa -> (GFb & GF(c & b & d))")
# f.traverse(countg)
# print("===", gcount, "G seen ===")
