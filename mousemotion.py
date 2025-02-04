import tkinter as tk

def on_mouse_click(event):
    print(f"Mouse Clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Mouse Event")

root.bind("<Button-1>", on_mouse_click)  # Left-click
root.bind("<Button-2>", on_mouse_click)  # Middle-click
root.bind("<Button-3>", on_mouse_click)  # Right-click

root.mainloop()
