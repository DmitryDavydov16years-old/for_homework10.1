from src.masks import masking_account, masking_card
from src.widget import changes_date_line, masking_card_or_account, replacing_email_addresses

card = input()
print(masking_card(card))

bill = input()
print(masking_account(bill))

card_or_bill = input()
print(masking_card_or_account(card_or_bill))

get_time = input()
print(changes_date_line(get_time))

line_of_text = input()
print(replacing_email_addresses(line_of_text))
