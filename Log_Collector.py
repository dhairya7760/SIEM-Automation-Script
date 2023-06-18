import win32evtlog
import csv
from io import StringIO
import pandas as pd
import win32evtlog
import win32evtlogutil
import win32security
import win32con
import winerror
import time
import re
import string
import sys
import traceback
import hashlib

def system():
	h = win32evtlog.OpenEventLog(None, "System")

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print("\n Number of records : ",len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = "Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name"
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ";" + records[i].SourceName + ";" + records[i].TimeWritten.Format() + ";" + str(records[i].EventID) + ";" + str(records[i].RecordNumber) + ";" + str(records[i].EventType) + ";" + str(records[i].EventCategory) + ";" + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
		df.to_csv('System_Log.csv',header=None,index=False)

def security():
	h = win32evtlog.OpenEventLog(None, "Security")

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print("\n Number of records : ",len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = "Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name"
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ";" + records[i].SourceName + ";" + records[i].TimeWritten.Format() + ";" + str(records[i].EventID) + ";" + str(records[i].RecordNumber) + ";" + str(records[i].EventType) + ";" + str(records[i].EventCategory) + ";" + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
		df.to_csv('Security_Log.csv',header=None,index=False)

def application():
	h = win32evtlog.OpenEventLog(None, "Application")

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print("\n Number of records : ",len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = "Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name"
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ";" + records[i].SourceName + ";" + records[i].TimeWritten.Format() + ";" + str(records[i].EventID) + ";" + str(records[i].RecordNumber) + ";" + str(records[i].EventType) + ";" + str(records[i].EventCategory) + ";" + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
		df.to_csv('Application_Log.csv',header=None,index=False)

print("\n System Logs ")
system()
print("\n Security Logs ")
security()
print("\n Application Logs ")
application()