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
                    result.append(f"Property '{property_name}' was removed")

                case 'changed':
                    result.append(render_changed(value, v_info, property_name))

        return result

    def render_nested(val, property_name):
        return iter_plain(val, f'{property_name}.')

    def render_added(value, property_name):
        val = stringify_value(value)
        return f"Property '{property_name}' was added " f"with value: {val}"

    def render_changed(value, v_info, property_name):
        old_val = stringify_value(value)
        new_val = stringify_value(v_info['new_value'])
        return (
            f"Property '{property_name}' was updated. "
            f"From {old_val} to {new_val}"
        )

    return '\n'.join(iter_plain(diff))
