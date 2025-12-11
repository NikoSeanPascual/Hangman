# Hangman Quiz Game (Python)

This is a command-line Hangman game that combines classic letter-guessing gameplay with general knowledge trivia.  
Each round begins with a random question, and the answer to that question becomes the word the player must guess.

The project was built entirely from scratch and this was my first attempt at trying to make something a that has 100+ lines of code without any help from others

---

## Features

- Random trivia question each game
- Hangman ASCII art that progresses with each wrong guess
- Full-word guessing supported
- Tracks used letters and remaining attempts
- Clean and readable function-based architecture

---

## How to Play

1. The program shows a random question.  
2. You guess letters one at a time.  
3. Each incorrect guess draws more of the hangman.  
4. You have **6 wrong guesses** before losing.  
5. You may also try to guess the entire word at once.

---

## Requirements

- Python 3.10

No external libraries are needed.

---

## How to Run

```bash
python hangman.py
```

---

## Project Structure

```
hangman.py      # Main game logic
README.md       # Project documentation
```

---

## Future Improvements
(I will probably check back on this repo and add this features in like 2 years, when I finally mastered this Language)

- Add more questions  
- Add difficulty levels  
- Add colors using ANSI escape codes  
- Add a scoring system 

---

## License

This project is free to use, modify, and learn from.
