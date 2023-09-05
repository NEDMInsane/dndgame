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
        new_game_window = tk.Tk()
        new_game = New_Game(new_game_window)

    def continue_game(self):
        print('Continuing last game played...')

    def load_game(self):
        print('Choose which game to load')

    def quit_game(self):
        self.root.destroy()

    #TODO: Function to make the window invisible/visible.


class New_Game:
    def __init__(self, new_game):
        self.new_game = new_game
        new_game.title('New Game')
        width = 800
        height = 600
        new_game.geometry(f'{width}x{height}')
        new_game.resizable(False, False)
        
        self.race = ''
        self.character_class = ''

        self.lbl_new_game = tk.Label(new_game, text = "Choose a race:", font = ("Helvetica", 24))
        self.lbl_new_game.pack()

        self.btn_width = 10
        self.btn_height = 5
        self.btn_human = tk.Button(self.new_game, text = "Human", width = self.btn_width, height = self.btn_height, command = self.race_human)
        self.btn_human.pack()
        self.btn_elf = tk.Button(self.new_game, text = "Elf", width = self.btn_width, height = self.btn_height, command = self.race_elf)
        self.btn_elf.pack()
        self.btn_dwarf = tk.Button(self.new_game, text = "Dwarf", width = self.btn_width, height = self.btn_height, command = self.race_dwarf)
        self.btn_dwarf.pack()
        self.btn_halfling = tk.Button(self.new_game, text = "Halfling", width = self.btn_width, height = self.btn_height, command = self.race_halfling)
        self.btn_halfling.pack()
        
    def select_race(self, race):
        print(f'You chose: {race}')
        self.race = race
        self.btn_dwarf.destroy()
        self.btn_elf.destroy()
        self.btn_halfling.destroy()
        self.btn_human.destroy()
        
        self.lbl_new_game['text'] = 'Choose a class:'
        self.lbl_new_game.pack()
        
        self.btn_cleric = tk.Button(self.new_game, text = "Cleric", width = self.btn_width, height = self.btn_height, command = self.class_cleric)
        self.btn_cleric.pack()
        self.btn_fighter = tk.Button(self.new_game, text = "Fighter", width = self.btn_width, height = self.btn_height, command = self.class_fighter)
        self.btn_fighter.pack()
        self.btn_rogue = tk.Button(self.new_game, text = "Rogue", width = self.btn_width, height = self.btn_height, command = self.class_rogue)
        self.btn_rogue.pack()
        self.btn_wizard = tk.Button(self.new_game, text = "Wizard", width = self.btn_width, height = self.btn_height, command = self.class_wizard)
        self.btn_wizard.pack()
        
    def race_human(self):
        self.select_race('Human')
        
    def race_elf(self):
        self.select_race('Elf')
        
    def race_dwarf(self):
        self.select_race('Dwarf')
        
    def race_halfling(self):
        self.select_race('Halfling')
    
    def class_cleric(self):
        self.select_class('Cleric')
        
    def class_fighter(self):
        self.select_class('Fighter')
        
    def class_rogue(self):
        self.select_class('Rogue')
        
    def class_wizard(self):
        self.select_class('Wizard')
        
    def select_class(self, character_class):
        print(f'You chose: {character_class}')
        self.character_class = character_class
        
        self.btn_cleric.destroy()
        self.btn_fighter.destroy()
        self.btn_rogue.destroy()
        self.btn_wizard.destroy()
        
        self.lbl_new_game['text'] = f'Your new character is a {self.race} {self.character_class}. Is this correct?'
        self.lbl_new_game.pack()
        
        btn_confirm = tk.Button(self.new_game, text = "Confirm", width = self.btn_width, height = self.btn_height, command = self.create_character)
        btn_confirm.pack()
        
    def create_character(self):
        print(f'You are now a {self.race} {self.character_class}')
        
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    gui = Main_Menu(root)
    root.mainloop()