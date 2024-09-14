from tkinter import ttk
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('Buttons')

    button = ttk.Button(master = window, text = 'Set')
    button.pack()

    # multiple choice check boxes
    check_var = tk.BooleanVar(value = False)
    checkbox1 = ttk.Checkbutton(
        window,
        text = 'checkbox 1',
        command = lambda: print(check_var.get()),
        variable = check_var,
        onvalue = True,
        offvalue = False)
    checkbox1.pack()

    # multiple choice buttons single option
    radio1 = ttk.Radiobutton(window, text = 'Radiobutton 1', value = 'radio 1')
    radio1.pack()
    radio2 = ttk.Radiobutton(window, text = 'Radiobutton 1', value = 'radio 2')
    radio2.pack()


    window.mainloop()

if __name__ == "__main__":
    main()