
from ..api_number import api_number
from .low_level.message import MetadataRequest, iRODSMessage

def data_avu(conn,op,/,path,avu,**opt):
    message_body = MetadataRequest(
        op, "-d", path, *avu, **opt
    )

    request = iRODSMessage(
        "RODS_API_REQ",
        msg=message_body, int_info=api_number["MOD_AVU_METADATA_AN"]
    )
    conn.send(request)
    response = conn.recv()
