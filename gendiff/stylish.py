def check_val(value):
    match value:
        case None:
            return " null"
        case bool():
            return f" {str(value).lower()}"
        case "":
            return ""
        case _:
            return f" {value}"


def keep_dict_add(result, value, depth=1, replace="    "):
    if not isinstance(value, dict):
        return f"{check_val(value)}"
    for k, v in value.items():
        if isinstance(v, dict):
            result.append(f"{replace*depth}{k}: " + "{")
            keep_dict_add(result, v, depth + 1)
            result.append(f"{replace*depth}" + "}")
            continue
        result.append(f"{replace*depth}{k}:{keep_dict_add(result, v, depth)}")


def simple_add(result, key, value, intend, depth, operation):
    match operation:
        case " ":
            result.append(f"{intend*depth}{key}:{check_val(value)}")
        case "-":
            result.append(f"{(intend*depth)[:-2]}- {key}:{check_val(value)}")
        case "+":
            result.append(f"{(intend*depth)[:-2]}+ {key}:{check_val(value)}")


def stylish(result, diff, intend="    "):
    for item in diff:
        depth = item["depth"]
        key = item['key']
        match item["type"]:
            case "dict":
                result.append(f"{intend * depth}{key}: " + "{")
                stylish(result, item["value"])
                result.append(f"{intend * depth}" + "}")
            case "keep":
                simple_add(
                    result,
                    key,
                    item["value"],
                    intend,
                    depth,
                    operation=" ",
                )
            case "add":
                simple_add(
                    result,
                    key,
                    item["value"],
                    intend,
                    depth,
                    operation="+",
                )
            case "delete":
                simple_add(
                    result,
                    key,
                    item["value"],
                    intend,
                    depth,
                    operation="-",
                )
            case "change":
                if isinstance(item["old_value"], dict):
                    result.append(f"{(intend*depth)[:-2]}- {key}: " + "{")
                    keep_dict_add(result, item["old_value"], depth + 1)
                    result.append(f"{(intend*depth)}" + "}")
                else:
                    simple_add(
                        result,
                        key,
                        item["old_value"],
                        intend,
                        depth,
                        operation="-",
                    )
                if isinstance(item["new_value"], dict):
                    result.append(f"{(intend*depth)[:-2]}- {key}: " + "{")
                    keep_dict_add(result, item["new_value"], depth + 1)
                    result.append(f"{(intend*depth)}" + "}")
                else:
                    simple_add(
                        result,
                        key,
                        item["new_value"],
                        intend,
                        depth,
                        operation="+",
                    )
            case "dict_delete":
                result.append(f"{(intend*depth)[:-2]}- {key}: " + "{")
                keep_dict_add(result, item["value"], depth + 1)
                result.append(f"{(intend*depth)}" + "}")
            case "dict_add":
                result.append(f"{(intend*depth)[:-2]}+ {key}: " + "{")
                keep_dict_add(result, item["value"], depth + 1)
                result.append(f"{(intend*depth)}" + "}")
    return result


def out_stylish(diff: list) -> str:
    result = ["{"]
    stylish(result, diff)
    result.append("}")
    return "\n".join(result)
