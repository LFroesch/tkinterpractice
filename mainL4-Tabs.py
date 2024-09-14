from tkinter import ttk
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('Tabs')
    window.geometry('600x400')

    # Notebook Widget
    notebook = ttk.Notebook(window)
    # Tab 1
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text = "Tab 1")
    label1 = ttk.Label(tab1, text = "Tab 1 Button")
    label1.pack()
    button1 = ttk.Button(tab1, text = "Tab 1 Button")
    button1.pack()

    # Tab 2
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text = "Tab 2")
    label2 = ttk.Label(tab2, text = "Tab 2 Button")
    label2.pack()
    button2 = ttk.Button(tab2, text = "Tab 2 Button")
    button2.pack()

    # Tab 3
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text = "Tab 3")
    label3 = ttk.Label(tab3, text = "Tab 3 Button")
    label3.pack()
    button3 = ttk.Button(tab3, text = "Tab 3 Button")
    button3.pack()

    # pack stack
    notebook.pack()


    # game loop, catches updates
    window.mainloop()

# run
if __name__ == "__main__":
    main()