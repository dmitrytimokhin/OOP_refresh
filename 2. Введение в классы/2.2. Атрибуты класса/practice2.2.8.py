# Реализуйте функцию is_obj_has_attr, которая принимает любой объект в качестве первого аргумента и название атрибута в качестве второго
#
# Функция is_obj_has_attr должна возвращать True, если в объекте имеется атрибут с указанным названием, либо вернуть False.
#
# Ваша задача написать только определение функции is_obj_has_attr

def is_obj_has_attr(attr: object,name: str):
    """

    :type name: object
    :type attr: object
    :param attr: 
    :param name: 
    :return: 
    """
    return hasattr(attr, name)
