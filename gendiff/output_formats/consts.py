from collections import namedtuple

# if you want to add new_format, add new name in _FORMAT_VALUES and that's it
_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices', map(str.upper, _FORMAT_VALUES))(
    *_FORMAT_VALUES
)

INDENT = '    '
