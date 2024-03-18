import string


RUS_LETTER_MAPPING = {
    'а': 'Alfa',
    'б': 'Bravo',
    'в': 'Victor',
    'г': 'Golf',
    'д': 'Delta',
    'е': 'Echo',
    'ж': 'Zulu Hotel',
    'з': 'Zulu',
    'и': 'India',
    'й': 'India',
    'к': 'Kilo',
    'л': 'Lima',
    'м': 'Mike',
    'н': 'November',
    'о': 'Oscar',
    'п': 'Papa',
    'р': 'Romeo',
    'с': 'Sierra',
    'т': 'Tango',
    'у': 'Uniform',
    'ф': 'Foxtrot',
    'х': 'X-ray',
    'ц': 'Tango Sierra',
    'ч': 'Charlie Hotel',
    'ш': 'Sierra Hotel',
    'щ': 'Sierra Charlie Hotel',
    'ы': 'Yankee',
    'ъ': '',
    'ь': '',
    'э': 'Echo',
    'ю': 'Yankee Uniform',
    'я': 'Yankee Alfa',
}


ICAO_CODE_WORDS = [
    'Alfa',
    'Bravo',
    'Charlie',
    'Delta',
    'Echo',
    'Foxtrot',
    'Golf',
    'Hotel',
    'India',
    'Juliett',
    'Kilo',
    'Lima',
    'Mike',
    'November',
    'Oscar',
    'Papa',
    'Quebec',
    'Romeo',
    'Sierra',
    'Tango',
    'Uniform',
    'Victor',
    'Whiskey',
    'X-ray',
    'Yankee',
    'Zulu',
]

ENG_LETTER_MAPPING = dict(zip(string.ascii_lowercase, ICAO_CODE_WORDS))


async def map_letter(ch: str, mapping_dict: dict) -> str:
    if ch.lower() not in mapping_dict.keys():
        return ch
    else:
        return mapping_dict[ch.lower()]


async def make_letter_mapping(ch: str, lang_mode: str) -> str:
    """
    :param lang_mode: 'ru' or 'en' mode
    :param ch: symbol to convert
    :return: converted symbol
    """
    match lang_mode:
        case "ru":
            return await map_letter(ch=ch, mapping_dict=RUS_LETTER_MAPPING)
        case "en":
            return await map_letter(ch=ch, mapping_dict=ENG_LETTER_MAPPING)


async def compile_mil_massage(message_text: str, lang_mode: str) -> str:
    """
    :param lang_mode: 'ru' or 'en' mode
    :param message_text: text received from user in bot
    :return: Make military alphabetical message --> "Hi" -> "Hotel India"
    """
    res_list = [await make_letter_mapping(ch, lang_mode) for ch in message_text if ch != ' ']
    militarized_message = ' '.join(res_list).replace(' ,', ',')
    print(militarized_message)
    return militarized_message
