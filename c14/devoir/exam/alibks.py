import re
import os
import csv
import json
import random


class insult_detector():
    def init(self):
        self.banned_words:list[str] = [
        "bête", "bete", "idiot", "stupide", "nul", "imbécile", "imbecile", "abruti",
        "incapable", "fainéant", "faineant", "méchant", "mechant", "agaçant", 
        "insolent", "prétentieux", "pretentieux", "paresseux","menteur", 
        "boulet", "clown", "rigolo", "maladroit", "distrait"
        ]
        self.commands = {
                'h': {'fn': self.print_help, 'help': 'Prints the help'},
                'c': {'fn': self.clear_screen, 'help': 'Clears the screen'},
                'l': {'fn': self.load, 'help': 'Load the the list'},
                'q': {'fn': self.end_prg, 'help': 'Quits the program'}
        }
        self.running = False
        self.start()
        with open('insults_found.txt', 'w+') as f:
            pass

    def load(self):
        with open('insultes.json') as f:
            self.banned_words = json.load(f)
        
    def clean(self, text:str) -> str:
        full_list = []
        for word in self.banned_words:
            found = re.findall(word, text)
            text = re.sub(word, '*'*len(word), text.lower())
            for i in found:
                full_list.append(i)
        with open('insults_found.txt', 'a') as f:
            f.writelines(full_list)
        return text

    def print_help(self):
        self.clear_screen()
        print('Commands')
        for i, v in self.commands.items():
            print(f'{i} -> {v['help']}')

    def clear_screen(self):
        os.system('cls') if os.name == 'nt' else os.system('clear')

    def start(self):
        self.running = True
        while self.running:
            inp = input('Enter un message > ')
            if inp in self.commands.keys():
                self.commands[inp]['fn']()
            else:
                out = self.clean(inp)
                print(out)
        self.clear_screen()
        print('Goodbye!')

    def end_prg(self):
        self.running = False 

class car_guess():
    def init(self):
        self.models = []
        self.retries = 6
        self.models_file = 'models.txt'
        self.scores_file = 'scores.csv'
        self.name = ''

        self.load()
        self.play()

    def load(self):
        with open(self.models_file) as f:
            self.models = [l.strip() for l in f.readlines()]
        return

    def save(self, model:str, found:bool):
        with open(self.scores_file, 'a+') as f:
            w = csv.writer(f)
            w.writerow((self.name, model, 'Oui' if found else 'Non', self.retries, 'gagné' if found else 'perdu'))

    def play(self):
        self.name:str = input('Enter your name > ').strip()
        model:str = random.choice(self.models)
        annon_name:str = ('_ '*len(model)).strip()
        wrong_entries = []
        while self.retries > 0 and '_' in annon_name:
            print(f'model: {annon_name}')
            # print(model)
            print(f'{self.retries} left')
            guess = input('Enter a letter > ')
            if guess in wrong_entries:
                print('This letter was already used')
            if guess in model:
                temp:list[str] = annon_name.split()
                for i, c in enumerate(model):
                    if c == guess:
                        temp[i] = guess
                # print(temp, idx)
                annon_name = ' '.join(temp)
            else:
                wrong_entries.append(guess)
                self.retries -= 1
        annon_name = annon_name.replace(' ', '')
        if annon_name == model:
            print('You won!')
        else:
            print('You lost better luck next time!')

        self.save(model, annon_name==model)

class sports_mngr():
    def init(self):
        self.teams:list[dict] = []
        pass

    def make_team(self, name:str, points:int, goals_scored:int, goals_conceded:int):
        return {
                'nom': name,
                'points': points,
                'buts_marques': goals_scored,
                'buts_encaisses': goals_conceded,
        }

    def save_teams(self) -> None:
        with open('equipes.json', 'w+') as f:
            json.dump(self.teams, f, indent=4)
        return

    def load_teams(self) -> None:
        with open('equipes.json') as f:
            self.teams = json.load(f)
        return

    def save_match(self):
        pass

def make_files():
    if not os.path.isfile('models.txt'):
        models = ["tesla","audi", "toyota", "ford", "bmw", "renault", "peugeot", "mercedes"]
        with open('models.txt', 'w+') as f:
            f.writelines(models)
    if not os.path.isfile('scores.csv'):
        with open('scores.csv', 'w+') as f:
            f.write('joueur,mot,trouvé,essais_restants,résultat')


if __name__ == '__main__':
    make_files()
    running = True
    def halt():
        global running
        running = False
    selections = {
            '1': {
                'start': car_guess().init,
                'text': 'Exercice 1: Devine le modèle de voiture',
                },
            '2': {
                'start': insult_detector().init,
                'text': 'Exercice 2: Détecteur d’insultes'
                },
            '3': {
                'start': sports_mngr().init,
                'text': 'Exercice 3: Gestion d’un tournoi sportif'
                },
            'q': {
                'start': halt,
                'text': 'Quit'
                }
        }

    def help():
        for i, v in selections.items():
            print(f'{i} -> {v['text']}')

    while running:
        help()
        inp = input('Select a program > ')
        if inp in selections.keys():
            selections[inp]['start']()
        else:
            os.system('cls') if os.name('nt') else os.system('clear')
            help()

        if input('Press enter to continue or q to quit\n') in ['q', 'quit']:
            halt()
    print('Goodbye!')
    

