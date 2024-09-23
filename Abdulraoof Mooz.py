# إعداد الطالب : عبد الرؤوف عابد علي موز 

import random
from PIL import Image, ImageTk
import tkinter as tk

class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image_file_path = f'images/{rank}_of_{suit}.png'  # Ensure this matches your directory structure

    def __repr__(self):
        return f'{self.rank} of {self.suit}'
    
    def load_image(self):
        try:
            image = Image.open(self.image_file_path)
            return image
        except IOError:
            print(f"Image not found for {self}: {self.image_file_path}")
            return None

class CardDeck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [PlayingCard(suit, rank) for suit in suits for rank in ranks]
        self.shuffle_deck()
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print('No cards left in the deck!')
            return None
    
class Gamer:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
    
    def draw_from_deck(self, deck, count=1):
        for _ in range(count):
            card = deck.draw_card()
            if card:
                self.cards_in_hand.append(card)
    
    def get_hand(self):
        return self.cards_in_hand

class CardGameInterface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Card Drawing Game")
        
        self.deck = CardDeck()
        self.player_one = Gamer("Gamer One")
        self.player_two = Gamer("Gamer Two")
        
        self.player_one_frame = tk.Frame(main_window)
        self.player_one_frame.pack(side="left", padx=20, pady=20)
        
        self.player_two_frame = tk.Frame(main_window)
        self.player_two_frame.pack(side="right", padx=20, pady=20)
        
        self.draw_button = tk.Button(main_window, text="Draw New Cards", command=self.draw_and_display)
        self.draw_button.pack(pady=20)
        
    def draw_and_display(self):
        self.player_one.draw_from_deck(self.deck, 5)
        self.player_two.draw_from_deck(self.deck, 5)
        
        self.display_hand(self.player_one, self.player_one_frame)
        self.display_hand(self.player_two, self.player_two_frame)
        
    def display_hand(self, gamer, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
        tk.Label(frame, text=f"{gamer.name}'s Cards:").pack()
        
        for card in gamer.get_hand():
            img = card.load_image()
            if img:
                img = img.resize((90, 140))  # Resize image to fit within the frame
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(frame, image=photo)
                label.image = photo  # Keep a reference to avoid garbage collection
                label.pack(side="left", padx=5)

# Run the game
main_window = tk.Tk()
game_interface = CardGameInterface(main_window)
main_window.mainloop()
