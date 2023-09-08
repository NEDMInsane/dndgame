import tkinter as tk
import character

class GUI:
    def __init__(self):
        self.width = 800
        self.height = 600

class Main_Menu(GUI):
    """
    A class representing the main menu of a DnD campaign game.

    Attributes:
        root (tk.Tk): The main tkinter window.
    
    Methods:
        __init__(self, root):
            Initializes the main menu with buttons for Continue, New Game, Load Game, and Quit.
        
        start_new_game(self):
            Initiates the process of starting a new game.

        continue_game(self):
            Initiates the process of continuing the last game played.

        load_game(self):
            Initiates the process of loading a saved game.

        quit_game(self):
            Closes the main menu window and quits the game.

    Note:
        This class provides a graphical user interface (GUI) for the DnD campaign game
        and allows the player to choose from various options, including starting a new game,
        continuing an existing game (if available), loading a saved game, or quitting the game.
    """

    def __init__(self, root):
        """
        Initialize the main menu.

        Args:
            root (tk.Tk): The main tkinter window.

        Initializes the main menu with buttons for Continue, New Game, Load Game, and Quit.
        """
        super().__init__()
        self.root = root
        root.title("DnD Campaign")
        self.width = 450
        self.height = 300
        root.geometry(f'{self.width}x{self.height}')
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
        """
        Start a new game.

        Initiates the process of starting a new game.
        """
        print('Starting new game...')
        new_game_window = tk.Tk()
        new_game = New_Game(new_game_window)

    def continue_game(self):
        """
        Continue the last game played.

        Initiates the process of continuing the last game played.
        """
        print('Continuing last game played...')

    def load_game(self):
        """
        Load a saved game.

        Initiates the process of loading a saved game.
        """
        print('Choose which game to load')

    def quit_game(self):
        """
        Quit the game.

        Closes the main menu window and quits the game.
        """
        self.root.destroy()

    # TODO: Implement a function to make the window invisible/visible.

class New_Game(GUI):
    """
    A class representing the character creation process for a new game.

    Attributes:
        new_game (tk.Tk): The tkinter window for character creation.
        race (str): The selected race for the character.
        character_class (str): The selected character class for the character.

    Methods:
        __init__(self, new_game):
            Initializes the character creation process with race selection.

        select_race(self, race):
            Handles race selection and transitions to class selection.

        select_class(self, character_class):
            Handles character class selection and transitions to character confirmation.

        start_over(self):
            Allows the player to start the character creation process over.

        create_character(self):
            Finalizes character creation and displays the character's race and class.

        race_human(self):
            Selects the Human race.

        race_elf(self):
            Selects the Elf race.

        race_dwarf(self):
            Selects the Dwarf race.

        race_halfling(self):
            Selects the Halfling race.

        class_cleric(self):
            Selects the Cleric character class.

        class_fighter(self):
            Selects the Fighter character class.

        class_rogue(self):
            Selects the Rogue character class.

        class_wizard(self):
            Selects the Wizard character class.

    Note:
        This class provides a graphical user interface (GUI) for character creation in the DnD campaign game.
        It allows the player to select a race, character class, and confirm their character's attributes.
    """

    def __init__(self, new_game):
        """
        Initialize the character creation process with race selection.

        Args:
            new_game (tk.Tk): The tkinter window for character creation.

        Initializes the character creation process with race selection and GUI elements for race choices.
        """
        super().__init__()
        self.new_game = new_game
        new_game.title('New Game')
        self.width = 800
        self.height = 600
        new_game.geometry(f'{self.width}x{self.height}')
        new_game.resizable(False, False)
        
        self.race = ''
        self.character_class = ''

        self.lbl_new_game = tk.Label(self.new_game, text = "Choose a race:", font = ("Helvetica", 24))
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
        """
        Handle race selection and transition to class selection.

        Args:
            race (str): The selected race for the character.

        Handles race selection, stores the chosen race, and transitions to class selection.
        """
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

    def select_class(self, character_class):
        """
        Handle character class selection and transition to character confirmation.

        Args:
            character_class (str): The selected character class for the character.

        Handles character class selection, stores the chosen class, and transitions to character confirmation.
        """
        print(f'You chose: {character_class}')
        self.character_class = character_class
        
        self.btn_cleric.destroy()
        self.btn_fighter.destroy()
        self.btn_rogue.destroy()
        self.btn_wizard.destroy()
        
        self.lbl_new_game['text'] = f'Your new character is a {self.race} {self.character_class}. Is this correct?'
        self.lbl_new_game.pack()
        
        self.btn_confirm = tk.Button(self.new_game, text = "Confirm", width = self.btn_width, height = self.btn_height, command = self.create_character)
        self.btn_confirm.pack()
        
        self.btn_start_over = tk.Button(self.new_game, text = "Start Over", width = self.btn_width, height = self.btn_height, command = self.start_over)
        self.btn_start_over.pack()

    def start_over(self):
        """
        Allow the player to start the character creation process over.

        Clears previous selections and resets the character creation process.
        """
        self.race = ''
        self.character_class = ''
        
        self.btn_start_over.destroy()
        self.btn_confirm.destroy()
        
        self.btn_cleric.destroy()
        self.btn_fighter.destroy()
        self.btn_rogue.destroy()
        self.btn_wizard.destroy()
        
        self.lbl_new_game['text'] = "Choose a race:"
        self.lbl_new_game.pack()
        
        self.btn_human = tk.Button(self.new_game, text = "Human", width = self.btn_width, height = self.btn_height, command = self.race_human)
        self.btn_human.pack()
        self.btn_elf = tk.Button(self.new_game, text = "Elf", width = self.btn_width, height = self.btn_height, command = self.race_elf)
        self.btn_elf.pack()
        self.btn_dwarf = tk.Button(self.new_game, text = "Dwarf", width = self.btn_width, height = self.btn_height, command = self.race_dwarf)
        self.btn_dwarf.pack()
        self.btn_halfling = tk.Button(self.new_game, text = "Halfling", width = self.btn_width, height = self.btn_height, command = self.race_halfling)
        self.btn_halfling.pack()

    def create_character(self):
        """
        Finalize character creation and display the character's race and class.

        Completes the character creation process and shows the character's race and class.
        """
        print(f'You are now a {self.race} {self.character_class}')
        self.lbl_new_game['text'] = f'You are now a {self.race} {self.character_class}'
        self.lbl_new_game.pack()
        
        self.btn_start_over.destroy()
        self.btn_confirm.destroy()        
        self.new_game.destroy()   
        
        main_game_window = tk.Tk()
        main_game = Main_Game(main_game_window, self.race, self.character_class)
 

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

class Main_Game(GUI):
    def __init__(self, main_game, race, character_class):
        super().__init__()
        self.main_game = main_game
        self.race = race
        self.character_class = character_class
        main_game.geometry(f'{self.width}x{self.height}')
        
        game_panel = tk.Frame(self.main_game)
        game_panel.configure(bg = "white", padx = 10, pady = 10)
        info_panel = tk.Frame(self.main_game)
        info_panel.configure(bg = "red", padx = 10, pady = 10)
        entry_panel = tk.Frame(self.main_game)
        entry_panel.configure(bg = "blue", padx = 10, pady = 10)
        
        game_panel.place(width = 550, height = 450, x = 0, y = 0)
        info_panel.place(width = 250, height = 450, x = 550, y = 0)
        entry_panel.place(width = 800, height = 150, x = 0, y = 450)

        self.party = []

        player_1 = character.create_character('Jimmy', self.race, self.character_class)
        self.party.append(player_1)

        partylabel = tk.Label(info_panel)
        partylabel.configure(text = self.list_player_characters_in_party(self.party))
        partylabel.pack(side = "top")


    def list_player_characters_in_party(self, party_list):
        party_string = 'Party List:'
        for player_character in party_list:
            party_string = party_string + '\n' + str(player_character)
        return party_string


if __name__ == "__main__":
    root = tk.Tk()
    gui = Main_Menu(root)
    root.mainloop()