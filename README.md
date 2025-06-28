# PRODIGY_CS_04
Python-based keylogger that records keystrokes to a log file

This project is part of the **Prodigy InfoTech Cybersecurity Internship**.

##  Objective

To create a basic **Python keylogger** that captures user keystrokes and logs them into a time-stamped file. This project demonstrates how background monitoring works and is intended **for educational purposes only**.

## Features

- Records all keystrokes (letters, numbers, special keys)
- Logs data into a `.txt` file with timestamps
- File is automatically named using the current date and time
- Easy to run from terminal (no GUI required)

## How It Works

- The program runs in the background using `pynput`
- It listens to all keyboard inputs
- Each key is logged in a timestamped `.txt` file
- You can stop it manually using `Ctrl + C` or closing the terminal or using 'ESC' key

