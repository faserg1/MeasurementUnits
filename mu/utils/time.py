#!/usr/bin/env python3

from datetime import datetime

def get_utc_seconds(date):
    epoch = datetime.utcfromtimestamp(0)
    return (date - epoch).total_seconds()
