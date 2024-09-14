from tkinter import ttk
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('Getting and setting Widgets')

    label = ttk.Label(master = window, text = 'Label Text')
    label.pack()

    entry = ttk.Entry(master=window, name='my_entry')
    entry.pack()

    button = ttk.Button(master = window, text = 'Set', command=lambda: disable_and_set(entry, label))
    button.pack()

    button2 = ttk.Button(master = window, text = 'Reset', command=lambda: enable_and_reset(entry, label))
    button2.pack()

    window.mainloop()

def disable_and_set(entry, label):
    entry_text = entry.get()
    label['text'] = entry_text
    print(entry_text)
    entry['state'] = 'disabled'

def enable_and_reset(entry, label):
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    entry = ""



if __name__ == "__main__":
    main()