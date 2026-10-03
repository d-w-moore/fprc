from os.path import abspath, dirname, join
import sys
import uuid

from irods.client.data import (
    data_open,
    data_close,
    data_unlink,
    O_CREAT,
    O_WRONLY
)
from irods.client.connection import Connection
from irods.client.metadata import data_avu
from irods.client.account import iRODSAccount
#from irods.client.query import Query
#from irods.client.query.models import DataObject,Collection
#from irods.client.query.column import Like

PATH = '/tempZone/home/rods/abc.dat-' + uuid.uuid1().hex

account = iRODSAccount(
    'localhost',
    1247,
    'rods',
    'tempZone',
    password='rods'
)

conn = Connection( account )

def test_data_and_metadata_create():
    desc = None
    try:
        desc = data_open(conn, PATH, O_WRONLY|O_CREAT)
        #input('->')
        data_close(conn, desc)
        data_avu(conn, "add", PATH, ("aa","bb",))
    finally:
        if desc:
            data_unlink(conn, PATH, force=True)
