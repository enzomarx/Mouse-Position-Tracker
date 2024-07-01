# Mouse-Position-Tracker

The Mouse Position Tracker is a simple GUI application built using Python's tkinter and pyautogui libraries. It allows you to capture and log the current position of the mouse cursor after a specified countdown period.

## Features
- **User Interface**: Provides a basic graphical interface using tkinter.
- **Capture Mouse Position**: Click a button to initiate a countdown, after which the current mouse position is logged.
- **Logging**: Displays the captured mouse positions in a text area for easy reference.
- **Clipboard Support**: Allows copying logged positions to the clipboard using keyboard shortcuts.

## Requirements
- Python 3.x
- tkinter library
- pyautogui library

## Usage
1. **Input Waiting Time**: Enter the waiting time in seconds (integer or float) in the provided entry field.
2. **Capture Mouse Position**: Click on the "Get Mouse Position" button to start the countdown.
3. **View Captured Positions**: The mouse position coordinates are displayed in the text area once captured.
4. **Copy to Clipboard**: Use `Ctrl+A` to select all positions, `Ctrl+C` to copy them to the clipboard.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```
2. Install required libraries:
   ```bash
   pip install tkinter pyautogui
   ```
3. Run the application:
   ```bash
   python mouse_position_logger.py
   ```

## Notes
- Ensure the application window is in focus during the countdown to capture accurate mouse positions.
- The captured positions remain visible until the application is closed or reset.

## Example
Here's a simple example to illustrate how to use the Mouse Position Logger:

```python
python mouse_position_logger.py
```
