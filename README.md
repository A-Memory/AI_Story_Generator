# AI Story Generator

A Python application that generates creative stories and characters using LM Studio as the AI backend.

## Overview

This application creates cute little stories with characters using a local AI model through LM Studio. It features a user-friendly interface built with Python Flet UI.

## Features

- Automatic story generation
- Character creation
- Clean, intuitive user interface
- Stories refresh automatically every 60 seconds

## Requirements

- Python 3.13+
- LM Studio application
- Required Python packages (managed via Poetry):
  - flet
  - lmstudio

## Installation

1. Clone this repository
2. Install dependencies using Poetry:
   ```
   poetry install
   ```
3. Install and set up LM Studio (if not already installed)

## Usage

1. Start LM Studio and ensure it's running properly
2. Launch the AI Story Generator by running
    ```
    flet run main.py
    ```

**IMPORTANT**: LM Studio must be running before starting the application. If LM Studio is not running, the application will start but no story generation will occur.

## How It Works

The application connects to LM Studio running locally, which provides the AI model capabilities. The UI displays characters and generated stories in a visually appealing format.

## Project Structure

- `main.py`: Core application logic and UI implementation
- `ShortBaby-Mg2w.ttf`: Custom font for the UI

## Credits

Developed by A-Memory

GitHub: [https://github.com/A-Memory](https://github.com/A-Memory)
