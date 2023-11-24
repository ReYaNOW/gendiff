from collections import namedtuple


_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices', map(str.upper, _FORMAT_VALUES))(
    *_FORMAT_VALUES
)
