from lxml import etree


def init(string):
    return etree.fromstring(string)


def first(tree, tags, attributes=None, value=None, absolute=False):
    q = every(tree, tags, attributes, value, absolute)
    return q[0]


def first_or_none(tree, tags, attributes=None, value=None, absolute=False):
    q = every(tree, tags, attributes, value, absolute)
    if q:
        return q[0]
    return None


def every(tree, tags, attributes=None, value=None, absolute=False):
    """
    Finds all nodes in <tree> with <tag>
    and any of <attributes> equal to <value> (optional).
    """
    total = []
    if absolute:
        prefix = '//'
    else:
        prefix = ''
    for tag in tags:
        if attributes:
            for attribute in attributes:
                if value is None:
                    q = '%s{%s}%s[@%s]' % (
                        prefix, '', tag, attribute
                    )
                else:
                    q = '%s{%s}%s[@%s="%s"]' % (
                        prefix, '', tag, attribute, value
                    )
                total += tree.findall(q)
        else:
            total += tree.findall('%s{%s}%s' % (
                prefix, '', tag))
    return total