#!/usr/bin/python
from pcap_analysis import PcapHandler

if __name__ == "__main__":
	a = PcapHandler()
	data = a.createDataFromPcapfile('1C887950FC57-1478761795-00008-data.pcap')
	sql  = a.createSQL(data)
	a.wr2db(sql)
