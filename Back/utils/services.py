import json
import os.path
import re
import traceback
from datetime import datetime
from functools import reduce

from django.conf import settings
from django.utils.timezone import now as django_now

from pytz import timezone


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def load_json(path, local=True):
    if local:
        path = full_path(path)
    with open(path, encoding='utf-8') as f:
        return load_attr(load_json, path, lambda: json.loads(read_file(path)))


def read_file(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def full_path(path_tail, check_existance=True):
    """ Возвращает полный путь к файлу лежащему в проекте. """
    path = os.path.join(settings.BASE_DIR, path_tail)
    if check_existance and not os.path.isfile(path):
        raise FileNotFoundError
    return path


def load_attr(obj, attribute, func):
    if not hasattr(obj, attribute):
        setattr(obj, attribute, func())
    return getattr(obj, attribute)


def process_error(exc, prefix=None):
    pretext = prefix + '\n' if prefix else ''
    error_text = (
        f'{pretext}Произошла ошибка {type(exc).__name__}: {exc}'
    )
    trace_path = full_path('tmp/traceback.txt', check_existance=False)
    trace = traceback.format_exc()
    with open(trace_path, 'w') as f:
        f.write(str(trace))
    with open(trace_path, 'rb') as f:
        tg_log(error_text, f)


def separate_thousands(number):
    return '{:,}'.format(number).replace(',', ' ')


def clean_html(text):
    return re.sub(r'<.*?>', '', text)


def callback_data(update, skip_left=0, skip_right=0):
    data = update.callback_query.data
    target = '_'.join(data.split('_')[skip_left:])
    return target


def now():
    return django_now()


def unpack_dict(target, keys, soft=False, pop=False):
    if soft:
        if pop:
            return [target.pop(k, None) for k in keys]
        else:
            return [target.get(k) for k in keys]
    else:
        if pop:
            return [target.pop(k) for k in keys]
        else:
            return [target[k] for k in keys]


def pick_dict(target, keys):
    values = unpack_dict(target, keys)
    items = zip(keys, values)
    return dict(items)


def strptime_one_of(date_string, formats, localize=True):
    dt = None
    for f in formats:
        try:
            dt = datetime.strptime(date_string, f)
        except ValueError:
            continue
    if dt is not None:
        dt = localize_dt(dt)
    return dt


def localize_dt(naive_dt):
    tz = timezone(settings.TIME_ZONE)
    try:
        return tz.localize(naive_dt)
    except OverflowError as e:
        localized = naive_dt.replace(tzinfo=tz)
        return localized


def deep_get(target, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, target)


def date_to_dict(date):
    return {
        'year': date.year,
        'month': date.month,
        'day': date.day,
    }
