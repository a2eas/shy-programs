import tkinter as tk
from tkinter import messagebox
from GetVed import on
import cv2
import threading

# Global variables
off = False
video_capture = None
capture_thread = None

# Button functions
def on_button_click():
    global off, video_capture, capture_thread
    off = False
    messagebox.showinfo("Shy programs!", 'Shy programs is on')

    video_capture = cv2.VideoCapture(0)

    def capture():
        global off
        while not off:
            result, video_frame = video_capture.read()
            if not result:
                break
            on(video_frame)
        video_capture.release()
        cv2.destroyAllWindows()

    capture_thread = threading.Thread(target=capture)
    capture_thread.start()

def off_button_click():
    global off
    off = True
    messagebox.showinfo("Shy programs!", 'Shy programs is off')

# Gradient background function
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Tkinter UI
root = tk.Tk()
root.title("Shy programs")
root.geometry("400x300")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, 400, 300, (255, 140, 0), (75, 0, 130))

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

label = tk.Label(frame, text="Shy Programs", font=("Arial", 14), bg="#ffffff", fg="#333333")
label.pack(pady=10)

# ON Button
on_button = tk.Button(frame, text="Click to turn on", font=("Arial", 12), bg="#4CAF50", fg="white", command=on_button_click)
on_button.pack(pady=10)

# OFF Button
off_button = tk.Button(frame, text="Click to turn off", font=("Arial", 12), bg="#f44336", fg="white", command=off_button_click)
off_button.pack(pady=10)

# Entry field
entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0", fg="#333333")
entry.pack(pady=10)

root.mainloop()
