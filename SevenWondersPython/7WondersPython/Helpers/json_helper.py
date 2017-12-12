from flask import json
import datetime
import decimal

def json_types_handler(self, x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    if isinstance(x, decimal.Decimal):
        return str(x)
    raise TypeError("Unknown type")