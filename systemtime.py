import datetime
import struct

def systemtime_16_le(bytes16):
    """
    typedef struct _SYSTEMTIME {
        WORD wYear;
        WORD wMonth;
        WORD wDayOfWeek;
        WORD wDay;
        WORD wHour;
        WORD wMinute;
        WORD wSecond;
        WORD wMilliseconds;
    } SYSTEMTIME, *PSYSTEMTIME, *LPSYSTEMTIME;
    """
    n = struct.unpack('<8H', bytes16)
    d = datetime.datetime(n[0], n[1], n[3], n[4], n[5], n[6], n[7] * 1000)
    return d.isoformat()

