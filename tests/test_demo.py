from src.masks import masc_of_bill, masc_of_card
from src.widget import masks_of_cards, give_data

card = input()
print(masc_of_card(card))

bill = input()
print(masc_of_bill(bill))

card_or_bill = input()
print(masks_of_cards(card_or_bill))

get_time = input()
print(give_data(get_time))
