# 🎯 Guess the Number Game

Welcome to the **Guess the Number** game — a fun and interactive Python project where the computer randomly selects a number between 1 and 100, and you try to guess it!

## 🧠 How It Works

- The computer generates a random number between 1 and 100.
- You enter your guess.
- The game gives you hints:
  - If your guess is too high, it tells you to try a lower number.
  - If your guess is too low, it tells you to try a higher number.
- The game continues until you guess the correct number.
- It also tracks how many attempts you made to guess correctly.

## 💻 Features

- Simple and beginner-friendly Python code
- Input validation for numbers outside the valid range
- Helpful hints to guide your guesses
- Tracks and displays the number of attempts

## 🚀 Getting Started

### Requirements

- Python 3.x installed on your system

### Run the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/salamsofi/guess-the-number-game.git
   ```
2. Navigate to the project folder:
   ```bash
   cd guess-the-number-game
   ```
3. Run the script:
   ```bash
   python guess_the_number.py
   ```

## 🛠️ Code Overview

```python
from random import randint

guess = randint(1, 100)
no_of_guesses = 0

while True:
    num = int(input("Guess the number between 1 to 100: "))
    ...
```

The game uses Python’s `randint()` to generate a number and a `while` loop to keep asking until the correct guess is made.

## 📦 Future Improvements

- Add difficulty levels (e.g., Easy: 1–50, Hard: 1–500)
- Include a GUI using Tkinter
- Save high scores or attempt history

## 🙌 Author

Made with ❤️ by [Md](https://github.com/salamsofi)