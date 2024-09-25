# DFA Project 1

## Overview
This project implements a Deterministic Finite Automaton (DFA) that processes input strings consisting of the characters 'a' and 'b'. The DFA is designed to accept specific patterns defined by its states and transitions. Additionally, the project includes file cleaning and lexical analysis functionalities.

## Features
- Initializes with a set of states, a start state, accept states, and transitions.
- Processes input strings and determines if they are accepted by the DFA.
- Displays a transition table for better understanding of state transitions.
- Cleans input files by removing unnecessary whitespace and comments.
- Performs lexical analysis on input statements.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

### Programs
- **Prog1**: This program implements a Deterministic Finite Automaton (DFA) that processes input strings consisting of the characters 'a' and 'b'. It defines states, transitions, and accepts specific patterns. The main function allows users to input strings and checks if they are accepted by the DFA, displaying the transition table at the end.

- **Prog2**: This program cleans a specified input file by removing unnecessary whitespace and comments. It processes each line, handles special cases (like `cin>>`), and writes the cleaned content to an output file. The main function specifies the input and output file names and executes the cleaning process.

- **Prog3**: This program performs lexical analysis on input statements. It defines arrays for reserved words, operators, and special symbols. The program splits input statements into lexemes and analyzes each lexeme to determine its type (reserved word, operator, special symbol, number, identifier, or invalid). The main function interacts with the user, allowing them to input statements for analysis and displaying the results.