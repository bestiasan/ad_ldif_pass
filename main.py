import base64

ENCODING = 'utf-16le'


def code_pass(password: str):
    _pass_encoded = password.encode(ENCODING)
    _pass_coded = base64.b64encode(_pass_encoded)
    print(f'{password} -> {_pass_encoded} -> {_pass_coded}')
    return _pass_coded


def decode_pass(password_c):
    _pass_decoded = base64.b64decode(password_c)
    _pass = _pass_decoded.decode(ENCODING)
    print(f'{password_c} -> {_pass_decoded} -> {_pass}')
    return _pass


def test_pass(password):

    cp = code_pass(password)
    assert password == decode_pass(cp)


test_pass('"newPassword"')
test_pass('dasdj#W$RWEKLRJ$')

pass
