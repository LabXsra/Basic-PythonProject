# Basic-PythonProject
This is begineers guide to learn the basic concept through small projects like guessing random number,password generator,rock,paper,scissors and
weather_app

# 🎲 Number Guessing Game

A simple command-line game built in Python. The computer picks a random number
between 1 and 100, and you try to guess it — with hints along the way to help
you narrow it down.

This was built as a beginner Python project to practice:
- Loops (`while`)
- Conditionals (`if` / `elif` / `else`)
- User input and type conversion
- The `random` module

## 🕹️ How to Play

1. Run the script.
2. Think of a number between 1 and 100 (the computer already picked one!).
3. Type your guess when prompted.
4. The game tells you if your guess is too high or too low.
5. Keep guessing until you get it right 🎉

## ▶️ Running the Game

Make sure you have Python 3 installed, then run:

```bash
python guessing_game.py
```

(Replace `guessing_game.py` with whatever you named the file.)

## 📋 Requirements

- Python 3.x
- No external libraries — just the built-in `random` module

## 🐛 Known Issues

- The attempt counter (`guess_attempts`) doesn't currently work as intended.
  `guess_attempts=+1` assigns `1` every time instead of incrementing, so the
  count never actually goes up. To fix it, use:
```python
  guess_attempts += 1
```
- There's currently no input validation — entering non-numeric text will
  crash the program with a `ValueError`.


## 📄 License

Feel free to use, modify, and share this project — great for learning!
