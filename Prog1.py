class DFA:
    def __init__(self):
        """Initialize the DFA with states, start state, accept states, and transitions."""
        # Define states
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.start_state = 'q0'  # The starting state of the DFA
        self.accept_states = {'q4'}  # Accepting states
        
        # Define transition function
        self.transitions = {
            'q0': {'a': 'q3'},  # From q0, on 'a' go to q3
            'q1': {'a': 'q2', 'b': 'q1'},  # From q1, on 'a' go to q2, on 'b' stay in q1
            'q2': {'b': 'q2'},  # From q2, on 'b' stay in q2
            'q3': {'a': 'q4', 'b': 'q3'},  # From q3, on 'a' go to q4 and 'b' stay on q3
            'q4': {'a': 'q2', 'b': 'q2'}   # From q4, on 'a' and 'b' go to q2
        }
    
    def process_input(self, input_string):
        """Process the input string and determine if it is accepted by the DFA."""
        current_state = self.start_state  # Start processing from the initial state
        
        for char in input_string:
            if char == '$':  # Stop processing if the end character is encountered
                break
            if char not in {'a', 'b'}:  # Check for valid input characters
                return "NO"  # Invalid input character
            if current_state not in self.transitions or char not in self.transitions[current_state]:
                return "NO"  # No valid transition from the current state
            current_state = self.transitions[current_state][char]  # Move to the next state
        
        # Check if the final state is an accepting state
        return "YES" if current_state in self.accept_states else "NO"
    
    def print_transition_table(self):
        print("Transition Table:")
        print("State | a | b")
        print("------|---|---")
        # Sort the states to ensure consistent order
        sorted_states = sorted(self.states)
        for state in sorted_states:
            a_transition = self.transitions.get(state, {}).get('a', '-')
            b_transition = self.transitions.get(state, {}).get('b', '-')
            print(f"{state:5} | {a_transition} | {b_transition}")

def main():
    """Main function to run the DFA and process user input."""
    dfa = DFA()  # Create an instance of the DFA
    
    while True:
        user_input = input("Enter a statement: ")  # Get user input
        if user_input.lower() == 'quit':  # Check for exit condition
            break
        
        result = dfa.process_input(user_input.rstrip('$'))  # Process the input string
        print(f"Output: {result}")  # Output the result


        continue_input = input("CONTINUE(y/n)? ")  # Prompt to continue or exit
        if continue_input.lower() != 'y':
            break
    
    dfa.print_transition_table() #print the transition table
    
if __name__ == "__main__":
    main()  # Run the main function
