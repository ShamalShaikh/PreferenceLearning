def verify_trajectory(trajectory, ba):
    """
    Verifies if the given trajectory satisfies the LTL specification represented by the Büchi automaton.
    
    Parameters:
        trajectory (list): A list of propositions observed at each step.
        ba (spot.twa_graph): The Büchi automaton representing the LTL formula.
        
    Returns:
        bool: True if the trajectory satisfies the LTL formula, False otherwise.
    """
    current_states = set([ba.get_init_state_number()])

    for obs in trajectory:
        next_states = set()
        for state in current_states:
            for edge in ba.out(state):
                # Evaluate the edge condition with the current observation
                acceptance = edge.cond.eval_formula(obs)
                if acceptance:
                    next_states.add(edge.dst)
        if not next_states:
            return False  # No accepting states reachable
        current_states = next_states

    # Check if any of the current states is accepting
    for state in current_states:
        if ba.state_acc(state):
            return True

    return False

# Example usage
trajectory = ['A', 'B', 'A', 'B']
ba = 
result = verify_trajectory(trajectory, ba)
print(f"\nTrajectory: {trajectory}")
print(f"Satisfies LTL Formula: {result}")
