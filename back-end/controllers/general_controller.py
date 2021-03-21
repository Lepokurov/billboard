from content_create import create_content
from factory import Factory

factory = Factory()


def get_start(page, step):
    start = step * (page - 1)
    return start


def get_elem_list(element, type_, value_, page, step):
    content = create_content('list', type_, value_)
    start = get_start(page, step)
    elem = element(start, step)
    factory(elem, content)
    return elem


def get_elem_solo(element, id_elem):
    elem = element(id_elem)
    factory(elem, {'page': 'solo'})
    return elem


def get_elem_count(element, type_, value_):
    content = create_content('count', type_, value_)
    elem = element(0)
    factory(elem, content)
    return elem.count
