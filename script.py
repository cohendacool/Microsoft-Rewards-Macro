import pyautogui
import webbrowser
import time
import random

queries = [
    "Why do cats purr?",
    "How far away is the Moon?",
    "What causes thunderstorms?",
    "Why do people dream?",
    "How do airplanes stay in the air?",
    "What is the deepest part of the ocean?",
    "Why is the sky blue?",
    "How do magnets work?",
    "What is the tallest mountain on Earth?",
    "Why do leaves change color in fall?",
    "How do rockets launch into space?",
    "What is the fastest animal in the world?",
    "Why do we get hiccups?",
    "How does the internet work?",
    "What causes earthquakes?",
    "Why do dogs wag their tails?",
    "How do bees make honey?",
    "What is inside a black hole?",
    "Why do people yawn?",
    "How do batteries store energy?",
    "What is the coldest place on Earth?",
    "Why do stars twinkle?",
    "How do submarines go underwater?",
    "What causes rainbows?",
    "Why do humans need sleep?"
]

def loop():
    # Open bing and move the mouse to the search bar
    webbrowser.open("https://bing.com")
    time.sleep(2.5)
    pyautogui.moveTo(1000, 325, duration=0.5)
    time.sleep(1.25)

    # Click the search bar and type a query
    pyautogui.click(1000, 325)
    time.sleep(0.5)
    pyautogui.write(random.choice(queries), interval=0.1)
    time.sleep(0.75)
    pyautogui.press("enter")

    # Scroll down a little bit to simulate reading the results
    time.sleep(1.5)

    for _ in range(50):
        pyautogui.scroll(random.randint(-75, -35))

    time.sleep(3)

    # Restart the process by opening a new tab
    pyautogui.hotkey("ctrl", "w")
    time.sleep(1.5)

print("Macro will begin shortly, press Ctrl+C to stop.")
time.sleep(3.5)

while True:
    loop()