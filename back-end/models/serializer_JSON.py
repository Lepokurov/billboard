import json


def serialize_JSON(billboard_element) -> json:
    """
    From class to json format
    :param billboard_element: Song or Artist or Genre or Year elem
    :return: json
    """
    #    I not sure if it's legal to do like that way.
    dict_elem: dict = billboard_element.__dict__
    return json.dumps(dict_elem)
