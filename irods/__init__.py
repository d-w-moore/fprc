import sys
import logging
import os

# Magic Numbers
MAX_PASSWORD_LENGTH = 50
MAX_SQL_ATTR = 50
MAX_PATH_ALLOWED = 1024
MAX_NAME_LEN = MAX_PATH_ALLOWED + 64
LONG_NAME_LEN = 256
RESPONSE_LEN = 16
CHALLENGE_LEN = 64
MAX_SQL_ROWS = 256
DEFAULT_CONNECTION_TIMEOUT = 120
# https://stackoverflow.com/questions/45704243/value-of-c-pytime-t-in-python
MAXIMUM_CONNECTION_TIMEOUT = 9223372036

#AUTH_SCHEME_KEY = "a_scheme"
#AUTH_USER_KEY = "a_user"
#AUTH_PWD_KEY = "a_pw"
#AUTH_TTL_KEY = "a_ttl"

NATIVE_AUTH_SCHEME = "native"



