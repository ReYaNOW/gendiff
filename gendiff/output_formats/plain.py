def stringify_value(value) -> str:
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case dict():
            return '[complex value]'
        case _:
            if not isinstance(value, int):
                return f"'{value}'"
            return f'{value}'


def render_plain(diff: dict) -> str:
    def iter_plain(diff: dict, curr_prop_path: str = '') -> list:
        result = []
        for key, v_info in diff.items():
            type_ = v_info['type']
            value = v_info['value']
            property_name = f'{curr_prop_path}{key}'

            match type_:
                case 'nested':
                    result.extend(render_nested(value, property_name))

                case 'added':
                    result.append(render_added(value, property_name))

                case 'deleted':
                    result.append(render_deleted(property_name))

                case 'changed':
                    result.append(render_changed(value, v_info, property_name))

        return result

    def render_nested(value, property_name: str) -> list:
        return iter_plain(value, f'{property_name}.')

    def render_added(value, property_name: str) -> str:
        val = stringify_value(value)
        return f"Property '{property_name}' was added with value: {val}"

    def render_deleted(property_name):
        return f"Property '{property_name}' was removed"

    def render_changed(value, v_info: dict, property_name: str) -> str:
        old_val = stringify_value(value)
        new_val = stringify_value(v_info['new_value'])
        return (
            f"Property '{property_name}' was updated. "
            f"From {old_val} to {new_val}"
        )

    return '\n'.join(iter_plain(diff))
