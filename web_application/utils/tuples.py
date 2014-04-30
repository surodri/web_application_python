def to_dict(tuple,keys):
    dict = {}
    for index, key in enumerate(keys):
        dict[key] = tuple[index]
        return dict
