from ...api_number import api_number
from ..low_level.message import (
    FileOpenRequest,
    FileSeekResponse,
    iRODSMessage,
    OpenedDataObjRequest,
    StringStringMap,
)

O_RDONLY = 0
O_WRONLY = 1
O_RDWR = 2
O_APPEND = 1024
O_CREAT = 64
O_EXCL = 128
O_TRUNC = 512

# TODO: This is suspect, since we don't know that iRODS and Linux agree on the value.
from os import SEEK_SET

def data_open(conn, /, path, flags=O_RDONLY, **options):
    message_body = FileOpenRequest(
        objPath=path,
        createMode=0o644,
        openFlags=flags,
        offset=0,
        dataSize=-1,
        numThreads=1,
        oprType=0,
        KeyValPair_PI=StringStringMap(options),
    )
    message = iRODSMessage("RODS_API_REQ", msg=message_body, int_info=api_number["DATA_OBJ_CREATE_AN"])
    conn.send(message)
    response = conn.recv()
    return response.int_info

def data_seek(conn, /, desc, offset, whence=SEEK_SET):
    message_body = OpenedDataObjRequest(
        l1descInx=desc,
        len=0,
        whence=whence,
        oprType=0,
        offset=offset,
        bytesWritten=0,
        KeyValPair_PI=StringStringMap(),
    )
    message = iRODSMessage("RODS_API_REQ", msg=message_body, int_info=api_number["DATA_OBJ_LSEEK_AN"])

    conn.send(message)
    response = conn.recv()
    offset = response.get_main_message(FileSeekResponse).offset
    return offset

def data_read(conn, /, desc, size=-1, buffer=None):
    if size < 0:
        size = len(buffer)
    elif buffer is not None:
        size = min(size, len(buffer))
    message_body = OpenedDataObjRequest(
        l1descInx=desc,
        len=size,
        whence=0,
        oprType=0,
        offset=0,
        bytesWritten=0,
        KeyValPair_PI=StringStringMap(),
    )
    message = iRODSMessage("RODS_API_REQ", msg=message_body, int_info=api_number["DATA_OBJ_READ_AN"])
    conn.send(message)
    if buffer is None:
        response = conn.recv()
    else:
        response = conn.recv_into(buffer)
    return response.bs

def data_write(conn, /, desc, string):
    message_body = OpenedDataObjRequest(
        l1descInx=desc,
        len=len(string),
        whence=0,
        oprType=0,
        offset=0,
        bytesWritten=0,
        KeyValPair_PI=StringStringMap(),
    )
    message = iRODSMessage(
        "RODS_API_REQ",
        msg=message_body,
        bs=string,
        int_info=api_number["DATA_OBJ_WRITE_AN"],
    )
    conn.send(message)
    response = conn.recv()
    return response.int_info

def data_close(conn, /, desc, **options):
    message_body = OpenedDataObjRequest(
        l1descInx=desc,
        len=0,
        whence=0,
        oprType=0,
        offset=0,
        bytesWritten=0,
        KeyValPair_PI=StringStringMap(options),
    )
    message = iRODSMessage("RODS_API_REQ", msg=message_body, int_info=api_number["DATA_OBJ_CLOSE_AN"])
    conn.send(message)
    conn.recv()
