from django import template
import re

register = template.Library()

# Список нецензурных слов
BAD_WORDS = ['редиска']


def censor_word(word):
    # Заменяем буквы в слове на символ '*'
    return '*' * len(word)


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр 'censor' применим только к строковым переменным.")

    # Создаем шаблон для поиска нецензурных слов
    pattern = r'\b(' + '|'.join(BAD_WORDS) + r')\b'

    # Функция замены с использованием re.sub
    def replace(match):
        word = match.group(0)
        return censor_word(word)

    # Заменяем нецензурные слова в строке и возвращаем результат
    return re.sub(pattern, replace, value, flags=re.IGNORECASE)