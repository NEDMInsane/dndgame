import tkinter as tk


class Main_Menu:
    def __init__(self, root):
        self.root = root
        root.title("DnD Campaign")
        width = 450
        height = 300
        root.geometry(f'{width}x{height}')
        root.resizable(False, False)

        self.lbl_title = tk.Label(root, text = "DnD Campaign", font = ("Helvetica", 55))
        self.lbl_title.pack(pady = 15)

        #TODO: Create a conditional to see if there is a recent save game
        self.btn_contine = tk.Button(root, text = "Continue", state = "disabled", command = self.continue_game, width = 10)
        self.btn_contine.pack(pady = 10)
        self.btn_new_game = tk.Button(root,text = "New Game", command = self.start_new_game, width = 10)
        self.btn_new_game.pack(pady = 5)
        self.btn_load_game = tk.Button(root, text = "Load Game", command = self.load_game, width = 10)
        self.btn_load_game.pack(pady = 5)
        self.btn_quit = tk.Button(root, text = "Quit", command = self.quit_game, width = 10)
        self.btn_quit.pack(pady = 5)

    def start_new_game(self):
        print('Starting new game...')
        new_game = New_Game(tk.Tk())

    def continue_game(self):
        print('Continuing last game played...')

    def load_game(self):
        print('Choose which game to load')

    def quit_game(self):
        self.root.destroy()

    #TODO: Function to make the window invisible/visible.

class New_Game:
    def __init__(self, parent, root):
        self.root = root
        root.title('New Game')
        width = 800
        height = 600
        root.geometry(f'{width}x{height}')
        root.resizable(False, False)

        self.lbl_new_game = tk.Label(root, text = "Choose a race:", font = ("Helvetica", 24))
        self.lbl_new_game.pack()

        self.btn_width = 10
        self.btn_height = 5
        self.btn_human = tk.Button(root, text = "Human", width = self.btn_width, height = self.btn_height, command = self.select_race('Human'))
        self.btn_human.pack()
        self.btn_elf = tk.Button(root, text = "Elf", width = self.btn_width, height = self.btn_height, command = self.select_race('Elf'))
        self.btn_elf.pack()
        self.btn_dwarf = tk.Button(root, text = "Dwarf", width = self.btn_width, height = self.btn_height, command = self.select_race('Dwraf'))
        self.btn_dwarf.pack()
        self.btn_halfling = tk.Button(root, text = "Halfling", width = self.btn_width, height = self.btn_height, command = self.select_race('Halfling'))
        self.btn_halfling.pack()

    def select_race(self, race):
        print(f'{race} chose, please pick a class.')

        self.lbl_new_game["text"] = "Choose a Class:"
        self.lbl_new_game.pack()

        self.btn_cleric = tk.Button(root, text = "Cleric", width = self.btn_width, height = self.btn_height)
        self.btn_cleric.pack()
        self.btn_fighter = tk.Button(root, text = "Fighter", width = self.btn_width, height = self.btn_height)
        self.btn_cleric.pack()
        self.btn_rogue = tk.Button(root, text = "Rogue", width = self.btn_width, height = self.btn_height)
        self.btn_rogue.pack()
        self.btn_wizard = tk.Button(root, text = "Wizard", width = self.btn_width, height = self.btn_height)
        self.btn_wizard.pack()

    def select_class(self, character_class):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    gui = Main_Menu(root)
    root.mainloop()