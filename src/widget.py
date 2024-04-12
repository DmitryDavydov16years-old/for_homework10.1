from src.masks import masking_account, masking_card


def masking_card_or_account(time: str) -> str:
    """ "
    Функция переиспользует ранее написанные функции и возвращает исходную строку с замаскированным номером карты/счета.
    """
    redact_time = time.split(" ")
    if redact_time[0] != "Счет":
        return f'{" ".join(redact_time[:-1])} {masking_card(redact_time[-1])}'
    return f"Счет {masking_account(redact_time[-1])}"


def changes_date_line(time: str) -> str:
    """
    Принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    redact_time = time.split("T")[0].split("-")
    return f"{redact_time[2]}.{redact_time[1]}.{redact_time[0]}"


def replacing_email_addresses(line_with_text: str) -> str:
    """
    Фунция принимает строку текста, содержащую одно или несколько предложений,
    и заменяет все email-адреса на маскированные версии
    """
    split_line_with_text = line_with_text.split(" ")
    for word in split_line_with_text:
        if "@" in word:
            split_word = word.split("@")
            part_of_word = split_word[0]
            len_part_of_word = len(part_of_word)
            list_part_of_word = list(part_of_word)
            hidden_characters = "X" * (len_part_of_word - 3)
            immutable_part = "".join(list_part_of_word[:3])
            number_of_item = split_line_with_text.index(word)
            split_line_with_text[number_of_item] = f"{immutable_part}{hidden_characters}@{split_word[1]}"
    return " ".join(split_line_with_text)
