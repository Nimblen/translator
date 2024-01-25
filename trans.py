from translate import Translator


def translate(text, from_lang="en", to_lang="ru") -> str:
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(text)
    if compare(text, translation):
        translator = Translator(from_lang=to_lang, to_lang=from_lang)
        translation = translator.translate(text)
        return translation

    return translation


def compare(user_input, output) -> bool:
    """
    This function compares the input text with the output text and returns a boolean value indicating if the input text is present in the output text.

    Args:
        user_input (str): The input text to be compared.
        output (str): The output text in which the input text is to be searched.

    Returns:
        bool: A boolean value indicating if the input text is present in the output text.

    """
    if user_input[1:2] in output:
        return True
    return False
