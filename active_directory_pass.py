"""
Based on :
https://stackoverflow.com/questions/30586604/correct-encoding-for-unicodepwd-in-active-directory
https://ldapwiki.com/wiki/Passwords%20Using%20LDIF
"""

import base64

ENCODING = 'utf-16le'


def unicode_pwd(password: str):
    _pass_encoded = password.encode(ENCODING)
    _pass_coded = base64.b64encode(_pass_encoded)
    print(f'{password} -> {_pass_encoded} -> {_pass_coded}')
    return _pass_coded


def deunicode_pwd(password_c):
    _pass_decoded = base64.b64decode(password_c)
    _pass = _pass_decoded.decode(ENCODING)
    print(f'{password_c} -> {_pass_decoded} -> {_pass}')
    return _pass


def test_pass(password):
    cp = unicode_pwd(password)
    assert password == deunicode_pwd(cp)


if __name__ == '__main__':
    test_pass('"newPassword"')
    test_pass('"dasdj#W$RWEKLRJ$"')
