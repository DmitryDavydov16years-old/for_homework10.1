from src.masks import masking_account, masking_card


def masking_card_or_account(card_or_account: str) -> str:
    """
    Функция переиспользует ранее написанные функции и возвращает исходную строку с замаскированным номером карты/счета.
    """
    split_card_or_account = card_or_account.split(" ")
    if split_card_or_account[0] != "Счет":
        return f'{" ".join(split_card_or_account[:-1])} {masking_card(split_card_or_account[-1])}'
    return f"Счет {masking_account(split_card_or_account[-1])}"


def changes_date_line(date: str) -> str:
    """
    Принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    split_date = date.split("T")[0].split("-")
    return f"{split_date[2]}.{split_date[1]}.{split_date[0]}"
