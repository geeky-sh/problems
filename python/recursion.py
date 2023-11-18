

complex_json = {
    'a': {'b': {"c": 'd'}},
    'x': [{'y': 'z'}]
}



def access(variable, access):
    if isinstance(variable, list):
        return variable[int(access)]
    elif isinstance(variable, dict):
        return variable[access]

def _get_value(variable, accessors):
    if not accessors or variable is None:
        return variable
    first = accessors[0]
    remaining = accessors[1:]
    return _get_value(access(variable, first), remaining)


def get_value(variable, accessor):
    return _get_value(variable, accessor.split("."))


def get_value(variable, accessor):
    accessors = accessor.split(".")
    for ac in accessors:
        if isinstance(variable, list):
            variable = variable[int(ac)]
        elif isinstance(variable, dict):
            variable = variable[ac]
    return variable



get_value(complex_json, 'a.b')
get_value(complex_json, 'a.b.c')
get_value(complex_json, 'x.0.y')