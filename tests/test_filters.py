def test_splitstr(jinja):
    assert jinja.filters['splitstr']('abc\ndef') == ['abc', 'def']
