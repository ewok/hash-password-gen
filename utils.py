# -*- coding: utf-8 -*-
__author__ = 'ewok'

import hashlib


def generate_password(master_password, salt, method_scheme, size=None):
    generated_password = str(master_password) + str(salt)

    for method in method_scheme:
        if method == 'sha1sum':
            generated_password = hashlib.sha1(generated_password).hexdigest()
        elif method == 'md5sum':
            generated_password = hashlib.md5(generated_password).hexdigest()
        else:
            raise TypeError('Wrong method!')

    return generated_password[:int(size)] if size else generated_password

