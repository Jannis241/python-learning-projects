# Screenshot-Taker

A small script that automatically takes screenshots of the screen and saves them.

## Run

Needs `pyautogui` (`pip install pyautogui`).

```sh
python src/takeScreenshot.py
```

It needs a real desktop with a display. It doesn't work headless or in a sandbox without a screen, then you get an Xlib error.

