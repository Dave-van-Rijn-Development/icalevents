class Encoding:
    ENCODE_ENCODING = 'utf-8'
    DECODE_ENCODING = 'ascii'


_encoding = Encoding()


def get_encoding():
    return _encoding


def set_encoding(*, encode_encoding: str = None, decode_encoding: str = None):
    encoding = get_encoding()
    if encode_encoding:
        encoding.ENCODE_ENCODING = encode_encoding
    if decode_encoding:
        encoding.DECODE_ENCODING = decode_encoding
