import json


def inner_endpoint_value(request, view):
    """
    Обращается к <view> с помощью <request>.
    Если полученный словарь содержит всего один ключ, то он пропускается,
    и возвращается только значимая часть ответа.
    """
    return response_value(inner_request(request, view))


def inner_request(request, view):
    """
    Обращается к <view> с помощью <request>.
    Полученный результат возвращается в формате словаря.
    """
    return json.loads(view(request).content.decode())


def response_value(response):
    """
    Получает из словаря <response> значимую часть,
    удалив при наличии ключ, если он единственный.
    """
    keys = list(response.keys())
    if len(keys) == 1:
        return response[keys[0]]
    return response
