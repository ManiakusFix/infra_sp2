from django.utils import timezone
import re

from django.core.exceptions import ValidationError

MINYEAR = 1945


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть <me>.'),
            params={'value': value},
        )
    if re.search(r'^[\w.@+-]{1,150}$', value) is None:
        raise ValidationError(
            ('Не допустимые символы в нике.'),
            params={'value': value},
        )


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            ('Год %(value)s больше текущего!'),
            params={'value': value},
        )

    if value < MINYEAR:
        raise ValidationError(
            ('%(value)s - некорректное значение года! (должно быть'
                f' больше {MINYEAR} г.)'),
            params={'value': value},
        )
