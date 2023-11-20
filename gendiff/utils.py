def stringify_value(value, format_name: str = 'stylish') -> str:
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case dict() if format_name == 'plain':
            return '[complex value]'
        case _:
            if format_name == 'plain' and not isinstance(value, int):
                return f"'{value}'"
            return f'{value}'
