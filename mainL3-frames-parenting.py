from tkinter import ttk
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('Frames and Parenting')
    window.geometry('600x400')

    # frame
    frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
    frame.pack_propagate(False)
    frame.pack(side = 'left')
    # master setting = frame (INSIDE FRAME)
    label = ttk.Label(frame, text = 'Label in frame')
    label.pack()
    button = ttk.Button(frame, text = 'Button Text')
    button.pack()
    # master setting = window (OUTSIDE FRAME)
    label2 = ttk.Label(window, text = 'Label outside frame')
    label2.pack()

    # frame 2
    frame2 = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
    frame2.pack_propagate(False)
    frame2.pack(side = 'left')
    # frame 2 widgets
    label3 = ttk.Label(frame2, text = "Frame 2 Label")
    button2 = ttk.Button(frame2, text = "Frame 2 Button")
    entry2 = ttk.Entry(frame2)
    label3.pack()
    button2.pack()
    entry2.pack()

    # pack stack
    

    # game loop, catches updates
    window.mainloop()

# run
if __name__ == "__main__":
    main()