# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python. You will practice string manipulation, loops, conditionals, and working with user input.

## 📝 Tasks

### 🛠️ Create the Word Selection System

#### Description
Set up a list of words and implement random word selection for each game session.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words
- Randomly select one word when the game starts
- Store the selected word for use throughout the game


### 🛠️ Build the Game Loop

#### Description
Implement the main game loop that accepts player guesses and tracks progress.

#### Requirements
Completed program should:

- Display the current word progress using underscores (e.g., `_ _ _ _`)
- Accept single letter guesses from the player
- Reveal correctly guessed letters in their positions
- Track and display the number of incorrect guesses remaining
- Continue until the word is guessed or attempts are exhausted


### 🛠️ Handle Game End Conditions

#### Description
Implement win and lose conditions with appropriate messages for the player.

#### Requirements
Completed program should:

- Display a win message when all letters are correctly guessed
- Display a lose message and reveal the word when attempts run out
- Show the final game state before ending
