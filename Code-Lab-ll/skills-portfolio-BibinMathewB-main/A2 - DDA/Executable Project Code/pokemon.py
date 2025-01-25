import requests
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class Pokemon:
    def __init__(self, name, Types, Abilities, Sprite):
        self.name = name
        self.types = Types
        self.abilities = Abilities
        self.sprite = Sprite

class Pokedex:
    def __init__(self):
        self.pokemon_data = {}
        self.pokemon_list = []

    def fetch_pokemon(self, name):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code == 200:
            data = response.json()
            Types = [t['type']['name'] for t in data['types']]
            Abilities = [a['ability']['name'] for a in data['abilities']]
            Sprite = data['sprites']['front_default']
            self.pokemon_data[name] = Pokemon(name, Types, Abilities, Sprite)
            return self.pokemon_data[name]
        else:
            return None

    def fetch_all_pokemon(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")  # Using the api given
        if response.status_code == 200:
            data = response.json()
            self.pokemon_list = [pokemon['name'] for pokemon in data['results']]
            return self.pokemon_list
        else:
            return []

class UserInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokédex")
        self.master.geometry("400x500")
        self.master.configure(bg="black")

        self.pokedex = Pokedex()
        self.pokedex.fetch_all_pokemon()

        # making the title of the app
        self.title_label = tk.Label(master, text="Pokédex", font=("Helvetica", 24, "bold"), bg="black", fg="white")
        self.title_label.pack(pady=10)

        # a dropdown selection for all the pokemons
        self.pokemon_combobox = ttk.Combobox(master, values=self.pokedex.pokemon_list, font=("Sans Serif", 14), width=20)
        self.pokemon_combobox.pack(pady=10)

        # Making the capture button
        self.fetch_button = tk.Button(master, text="Capture", command=self.fetch_pokemon_info, font=("Sans Serif", 12), bg="#007bff", fg="white")
        self.fetch_button.pack(pady=10)

        # the capture solution
        self.result_frame = tk.Frame(master, bg="black")
        self.result_frame.pack(pady=20)

        self.result_label = tk.Label(self.result_frame, text="", wraplength=350, justify="center", font=("Sans Serif", 12), bg="black", fg="white")
        self.result_label.pack(pady=10)

        self.pokemon_image = tk.Label(self.result_frame, bg="black")
        self.pokemon_image.pack(pady=10)

    def fetch_pokemon_info(self):
        name = self.pokemon_combobox.get()
        if name:
            pokemon = self.pokedex.fetch_pokemon(name)
            if pokemon:
                types = ', '.join(pokemon.types)
                abilities = ', '.join(pokemon.abilities)
                self.result_label.config(text=f"Name: {pokemon.name.capitalize()}\nTypes: {types}\nAbilities: {abilities}")
                self.display_pokemon_image(pokemon.sprite)
            else:
                messagebox.showerror("Error", "Pokémon not found!")
        else:
            messagebox.showwarning("Warning", "Please select a Pokémon.")

    def display_pokemon_image(self, sprite_url):
        try:
            image_response = requests.get(sprite_url)
            image_data = Image.open(requests.get(sprite_url, stream=True).raw)
            image_data = image_data.resize((100, 100), Image.ANTIALIAS)  # Resize image
            self.pokemon_image.image = ImageTk.PhotoImage(image_data)
            self.pokemon_image.config(image=self.pokemon_image.image)
        except Exception as e:
            self.pokemon_image.config(image="")
            print(f"Error loading image: {e}")

# running the main app
if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()