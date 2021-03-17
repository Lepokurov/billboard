from BillbordElement import BillboardElement


def create_list_general(sql_data, BillboardElement):
    list_ = []
    for sql_line in sql_data:
        genre = BillboardElement(sql_line[0], sql_line[1], sql_line[2])
        list_.append(genre)
    return list_
