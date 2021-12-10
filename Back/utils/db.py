def index(model, index):
    return model.objects.get(id=index)


def get_or_create(model, **kwargs):
    existing = get_or_none(model, **kwargs)
    if existing is not None:
        return existing
    return create(model, **kwargs)


def create(model, **kwargs):
    return getattr(model.objects, 'create')(**kwargs)


def get_or_none(model, **kwargs):
    query = model.objects
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    if len(query) > 0:
        return query.get()


def get(model, **kwargs):
    query = model.objects
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    return query.get()


def first(model, **kwargs):
    query = model.objects
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    return query.all()[0]


def last(query):
    return query.order_by('-id').all()[0]


def first_or_none(model, **kwargs):
    query = model.objects
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    if query.exists():
        return query.all()[0]


def change(instance, **kwargs):
    for name, value in kwargs.items():
        setattr(instance, name, value)
    instance.save()


def query(model, **kwargs):
    query = model.objects
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    return list(query.all())


def qfilter(query, **kwargs):
    for name, value in kwargs.items():
        query = query.filter(**{name: value})
    return query
