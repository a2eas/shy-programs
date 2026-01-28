# Shy Programs – Automatic Window Minimizer

This project is a fun, experimental Python application that uses **OpenCV** to detect faces via your webcam and automatically minimizes active programs when someone is near. It's designed for users who like a bit of privacy, or just for a quirky demonstration of computer vision in action.

---

## Overview

The application continuously monitors the camera feed and detects whether one or more faces are visible. If faces are detected near the camera, it automatically minimizes the current active program windows.  

Originally, the idea was to integrate a pre-trained AI model for detection, but this version relies on **classical computer vision techniques** since it was built during an early learning phase.

Key points:

- Uses **OpenCV** for face detection  
- Detects **one or more faces** in front of the camera  
- Minimizes the active program windows to protect privacy  
- Lightweight and beginner-friendly  

---

## Features

- **Real-time face detection** via webcam  
- **Automatic window minimization** when faces are detected  
- Fully written in Python  
- Easy to run and experiment with  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/a2eas/ShyPrograms.git
cd ShyPrograms
```
2. Install dependencies:
 ```bash
   pip install opencv-python pygetwindow pyautogui
```


##Usage

Run the main Python script:

```bash
python shy_programs.py
```

Make sure your webcam is connected.

The program will continuously monitor the feed.

When faces are detected, the current active windows will minimize automaticall



Notes

This is an experimental and educational project.

Works best in environments with good lighting.

Can be extended with AI-based face detection models for improved accuracy.

It is also a mess of a code



Learning Goals

Practice OpenCV face detection

Learn automation of window management with Python

Experiment with real-time camera feeds

Understand the challenges of simple AI integration for personal projects

License

This project is for learning and experimentation purposes. You are free to explore and modify the code.
