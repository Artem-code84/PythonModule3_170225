class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {
            "Diamonds": '\u2666',
            "Hearts": "\u2665",
            "Spades": '\u2660',
            "Clubs": '\u2663'
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)

cards_str = []
for card in cards:
    cards_str.append(card.to_str())

print(", ".join(cards_str))

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
