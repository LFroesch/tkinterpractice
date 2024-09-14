from tkinter import ttk
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('Menus')
    window.geometry('600x400+1920+0')

    # menu
    menu = tk.Menu(window)

    # sub menu
    file_menu = tk.Menu(menu, tearoff = False)
    file_menu.add_command(label = 'New', command = lambda : print("New File"))
    # file_menu.add_separator()
    file_menu.add_command(label = 'Open', command = lambda : print("Open File"))
    menu.add_cascade(label = 'File', menu = file_menu)

    # sub menu 2
    help_menu = tk.Menu(menu, tearoff = False)
    help_menu.add_command(label = 'help entry', command = lambda : print(help_check_string.get()))
    help_check_string = tk.StringVar()
    help_menu.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)
    menu.add_cascade(label = 'Help', menu = help_menu)

    # "pack" stack
    window.configure(menu = menu)

    # menu button
    menu_button = ttk.Menubutton(window, text = 'Menu Button')
    menu_button.pack()

    button_sub_menu = tk.Menu(menu_button, tearoff = False)
    button_sub_menu.add_command(label = 'entry 1', command = lambda : print('Test 1'))
    button_sub_menu.add_checkbutton(label = 'check 1')
    menu_button.configure(menu = button_sub_menu)

    # game loop, catches updates
    window.mainloop()

# run
if __name__ == "__main__":
    main()