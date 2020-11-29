from passgen.transformer import transform


def test_transform_delimiter():
    assert 'a b c' == transform(list('abc'))
    assert 'a b c' == transform(list('abc'), delimiter=' ')
    assert 'a.b.c' == transform(list('abc'), delimiter='.')
    assert 'a.b.c' == transform(tuple('abc'), delimiter='.')
