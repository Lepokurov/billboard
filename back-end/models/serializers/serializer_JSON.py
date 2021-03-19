import json


def serialize_JSON(billboard_element) -> json:
    """
    From class to json format
    :param billboard_element: Song or Artist or Genre or Year elem
    :return: json
    """
    #    I not sure if it's legal to do like that way.
    return json.dumps(billboard_element.__dict__)
