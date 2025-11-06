import os
import re
import json


class App():
    def __init__(self):
        self.cached_contacts:list = []
        self.debug_flag:bool = False
        self.running:bool = True
        
        self.controls = {
            "a": {
                'help': 'Add Contact',
                'alias': ['add'],
                'fn': self.add_contact
            },
            "d": {
                'help': 'Delete contact',
                'alias': ['delete', 'remove', 'del', 'rm'],
                'fn': self.del_contact
            },
            "f": {
                'help': 'Find contact',
                'alias': ['find', 'search'],
                'fn': lambda: self.show_all(self.find_contact())
            },
            "l": {
                'help': 'Show All Contacts',
                'alias': ['list', 'show'],
                'fn': lambda : self.show_all(self.cached_contacts)
            },
            "s": {
                'help': 'Sort Contacts',
                'alias': ['sort'],
                'fn': self.sort_contacts
            },
            "c": {
                'help': 'Clear Screen',
                'alias': ['clear'],
                'fn': self.clear_scr
            },
            "h": {
                'help': 'Show help',
                'alias': ['help', '?'],
                'fn': self.show_help
            },
            "q": {
                'help': 'Quit',
                'alias': ['quit', 'exit'],
                'fn': self.stop
            }
        }
        
        try:
            self.run()
        except KeyboardInterrupt:
            self.clear_scr()
            print("Goodbye!")

    def load(self) -> list[dict]:
        self.debug("loading contacts")
        if os.path.isfile("./contacts.json"):
            with open('./contacts.json') as f:
                self.cached_contacts = json.load(f)

    def save(self) -> None:
        self.debug("Saving contacts")
        with open('./contacts.json', 'w+') as f:
            json.dump(self.cached_contacts, f, indent=4)

    def debug(self, *args) -> None:
        if self.debug_flag == True:
            for i in args:
                print(i)

    def add_contact(self, name=None, number=None, msg=None) -> None:
        self.clear_scr()
        if msg:
            print(msg)
            
        name = name or input("enter a name: ").strip()
        
        # name validation
        if re.match(r'^[a-zA-Z ]{2,30}$', name) == None:
            self.add_contact(msg='Invalid name')
        elif any(c['name'].lower() == name.lower() for c in self.cached_contacts):
            self.add_contact(name, msg='Name already exists')
        elif name == '\\c':
            print('Cancelled')
            return
        
        number = number or input("enter a phone number: ")
        
        # number validation
        if re.match(r'[0-9]{10}', number) == None:
            self.add_contact(name, msg='Invalid number')
        elif any(c['number'] == number for c in self.cached_contacts):
            self.add_contact(name, msg='Number already exists')
        elif number == '\\c':
            print('Cancelled')
            return
        
        email = input("enter email: ")
        
        # email validation
        if re.match(r'[\w-]+@\w+\.\w+', email) == None:
            self.add_contact(name, number, msg='Invalid email')
        elif any(c['email'].lower() == email.lower() for c in self.cached_contacts):
            self.add_contact(name, number, msg='Email already exists')
        elif email == '\\c':
            print('Cancelled')
            return
        
        self.cached_contacts.append(
            {
                'name': name,
                'number': number,
                'email': email
            }
        )
        self.save()
        
        print(f'{name} added successfully!')
        return

    def find_contact(self) -> list[dict]:
        name:str = input("Search a contact: ")
        res:list[dict] = []
        for c in self.cached_contacts:
            if name.lower() in c['name'].lower():
                res.append(c)
        return res

    def show_all(self, filtered_list=None) -> None:
        if filtered_list is None: filtered_list = self.cached_contacts
        self.clear_scr()
        if len(filtered_list) == 0:
            self.debug(filtered_list)
            self.debug(self.cached_contacts)
            print("No contacts available")
            return
        self.debug(filtered_list)
        print("All contacts: ")
        for i in range(len(filtered_list)):
            c = filtered_list[i]
            print('-'*25)
            print(f"idx:{i+1}\nName: {c['name']}\nPhone number: {c['number']}\nEmail: {c['email']}\n")
            print('-'*25)
        return

    def del_contact(self):
        results = self.find_contact()
        if len(results) > 1:
            self.debug(f"found multiple results {len(results)}")
            self.debug(results)
            show_all(results)
            c_index = int(input('Select one of the results: '))
            self.cached_contacts.remove(results[c_index - 1])
        else:
            self.cached_contacts.remove(results[0])
        self.save()
        return

    def clear_scr(self):
        os.system("cls") if os.name == 'nt' else os.system("clear")
        print('Contact Manager')

    def show_help(self) -> None:
        self.clear_scr()
        print('Commands: ')
        for key, action in zip(self.controls.keys(), [i['help'] for i in self.controls.values()]):
            print(f'{key} -> {action}')

    def sort_contacts(self):
        res = sorted(self.cached_contacts, key=lambda x: x['name'])
        for i in res:
            print(f"Name: {i['name']}")
            
    def stop(self) -> None:
        self.running = False
    
    def run(self) -> None:
        self.clear_scr()
        self.load()
        while self.running:
            cmd = input("> ")
            if cmd not in self.controls.keys() and all(cmd not in v['alias'] for v in self.controls.values()):
                print("wrong command use h for help")
            else:
                try:
                    self.controls[cmd]['fn']()
                except KeyError:
                    for v in self.controls.values():
                        if cmd in v['alias']:
                            v['fn']()
                            break
        self.clear_scr()
        print("Goodbye!")

if __name__ == "__main__":
    app = App()