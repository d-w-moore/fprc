from os.path import abspath, dirname, join
import sys

from irods.client.data import (data_open, data_close, O_CREAT, O_WRONLY)
from irods.client.connection import Connection
from irods.client.metadata import data_avu
from irods.client.account import iRODSAccount
#from irods.client.query import Query
#from irods.client.query.models import DataObject,Collection
#from irods.client.query.column import Like

PATH = '/tempZone/home/rods/abc.dat'

account = iRODSAccount(
    'localhost',
    1247,
    'rods',
    'tempZone',
    password='rods'
)

conn = Connection( account )

def test_data_and_metadata_create():
    desc = data_open(conn, PATH, O_WRONLY|O_CREAT)
    data_close(conn, desc)
    data_avu(conn, "add", PATH, ("aa","bb",))
    # TODO: unlink the data object.
