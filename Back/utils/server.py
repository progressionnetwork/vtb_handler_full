import json

from django.http import JsonResponse


class Serializer:

    def serialize(self, target):
        if not hasattr(self, 'Model'):
            raise NotImplementedError(f'Model attribute wasn\'t set for {type(self).__name__}.')
        if self.Model != type(target):
            raise ValueError(f'Wrong serializer {type(self).__name__} for target {type(target).__name__}.')

    def serialize(self, target):
        result = {}
        simple_fields = [
            'id',
        ]
        result.update({f: getattr(target, f) for f in simple_fields})

        return result


def parse_request_data(request):
    data = {k: v for k, v in request.GET.items()}
    try:
        data.update(json.loads(request.body))
    except Exception as e:
        print('parse_request_data', e)
    finally:
        data.update({k: v for k, v in request.POST.items()})
    return data


def check_missing_field(body, fields):
    """
    Проверка наличия обязательных полей <fields> в <body> запроса.
    Возвращает недостающий ключ или None.
    """
    for field in fields:
        if field not in body:
            return field


def check_one_of_exists(body, fields):
    """
    Проверка наличия одного из обязательных полей <fields> в <body> запроса.
    Возвращает первый встреченый ключ или None.
    """
    for field in fields:
        if field in body:
            return field


def invalid_field_value(field):
    """
    Ответ сервера в случае некорректного значения поля <field> в запросе.
    """
    return response(
        400, 'Некорректное значение "{}"'.format(field)
    )


def required_field_missing(field):
    """
    Ответ сервера в случае отсутствия обязательного поля <field> в запросе.
    """
    return response(
        400, 'Отсутствует обязательное поле "{}"'.format(field)
    )


def response(code, message=None, data=None):
    """
    Ответ сервера с кодом <code> в формате:
    {
        'status': bool (<code> == 200),
        ? 'message': str (<message>),
        ? 'data': (<data>),
    }
    """
    body = {'status': code == 200}
    if message is not None:
        body['message'] = message
    if data is not None:
        body['data'] = data
    return JsonResponse(body, status=code)
