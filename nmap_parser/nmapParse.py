''' This module deals with the nmap parsing operations. The operations like checking for the IP address, open ports are done. '''
''' Dependency modules for the tool to run are 
	- openpyxl
	- pandas
'''
import sys
import re
import fileHandler
import pandas as pd

# Global list for exporting to excel
lst_hosts = []
lst_ports = []
lst_protocol = []
lst_state = []
lst_service = []
lst_reason = []
lst_version = []
lst_sr_no = []
sr_no_cnt = 0

def parseNmapContents(inputFile, formatFlag, outputFile):
	''' The function extracts the contents of the nmap output for specific host. The nmap result file is used for parsing.
		- inputFile path of the nmap result file to be used for parsing. 
		- Format Flag to check if the version regex is to be applied. Values can be 1 [For reason], 2 [For version]. Defaults to 1
		- OutputFile where the excel sheet is to be stored on the file system after parsing. Defaults to current location
	'''
	result = fileHandler.fileRead(inputFile)
	#print('File Contents are:', result)
	getIpAddresses(result, formatFlag, outputFile)
	re.purge()

def getPortDetails(str_port, ip, formatFlag, outputFile):
	'''This function  extracts the contents of substring between the IPs for open port details. ''' 
	print('formatFlag = ', formatFlag)	
	ports_With_reason = "(?P<ports>[\d]+)\/(?P<protocol>tcp|udp)\s+(?P<state>open|filtered)\s+(?P<service>[\w\S]*)\s+(?P<reason>.*)"
	ports_With_version = "(?P<ports>[\d]+)\/(?P<protocol>tcp|udp)\s+(?P<state>open|filtered)\s+(?P<service>\S*(?!\n)\S)(?:\n|(?P<version>.*))"
	ports_With_both = "(?P<ports>[\d]+)\/(?P<protocol>tcp|udp)\s+(?P<state>open|filtered)\s+(?P<service>[\w\S]*)\s+(?P<reason>\S*\s+\S+\s+\S*(?=\w)\w)(?:\n|(?P<version>.*))"
	#ports_With_version = #"(?P<ports>[\d]+)\/(?P<protocol>tcp|udp)\s+(?P<state>open|filtered)\s+(?P<service>[\w\S]*)\s+(?P<reason>[\w\S]*\s+[\w\S]+\s+[\w\S]*\s*)(?P<version>[\w\S]*)"
	
	str_ports = None
	if formatFlag == '1':
		str_ports = ports_With_reason
	if formatFlag == '2':
		str_ports = ports_With_version
	if formatFlag == '3':
		str_ports = ports_With_both
		
	print('Regex selected is :- ', str_ports)	
	#pattern_ports_reasons = re.compile(ports_With_reason, re.MULTILINE)
	pattern_ports_reasons = re.compile(str_ports, re.MULTILINE)
	
	ports = pattern_ports_reasons.finditer(str_port)
	host_cnt = 0
	for port in ports:
		if host_cnt==0:
			global sr_no_cnt
			lst_hosts.append(ip)
			host_cnt = host_cnt + 1
			sr_no_cnt = sr_no_cnt + 1
			lst_sr_no.append(sr_no_cnt)
		else:
			lst_hosts.append("")
			lst_sr_no.append("")
			
		lst_ports.append(port.group("ports"))
		lst_protocol.append(port.group("protocol"))
		lst_state.append(port.group("state"))
		lst_service.append(port.group("service"))
		#lst_reason.append(port.group("reason"))
		
		if formatFlag == '1': #Flag value of 1 is for Reason
			lst_reason.append(port.group("reason"))
			
		if formatFlag == '2': #Flag value of 2 is for Version
			lst_version.append(port.group("version"))
		
		if formatFlag == '3': #Flag value of 3 is for Version and Reason both
			lst_reason.append(port.group("reason"))
			lst_version.append(port.group("version"))
		
	# Export to excel now
	if formatFlag == '1': # Flag value of 1 is for handling 'Reason' field of nmap output.
		df = pd.DataFrame({'Sr. No': lst_sr_no, 'Host': lst_hosts, 'Ports': lst_ports, 'Protocol': lst_protocol, 'State': lst_state, 'Service': lst_service, 'Reason': lst_reason})
	if formatFlag == '2': # only version infor but no reason info in output
		df = pd.DataFrame({'Sr. No': lst_sr_no, 'Host': lst_hosts, 'Ports': lst_ports, 'Protocol': lst_protocol, 'State': lst_state, 'Service': lst_service, 'Version': lst_version})
	if formatFlag == '3':
		df = pd.DataFrame({'Sr. No': lst_sr_no, 'Host': lst_hosts, 'Ports': lst_ports, 'Protocol': lst_protocol, 'State': lst_state, 'Service': lst_service, 'Reason': lst_reason, 'Version': lst_version})
	
	print('output file to be used in creating the sheet is :- ', outputFile)	
	df.to_excel(outputFile, sheet_name='sheet1', index=False)	
	#df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

	

def getIpAddresses(str, formatFlag, outputFile):
	'''The function extracts the IP addresses from the nmap result file. Returns the index at which IP address is found in the result string'''
	#print('getIpAddresses():- The nmap result text is as follows.------------------>')
	#print(str)
	#Check for the pattern 'Nmap scan report for ' with   captured group name. Check if the named group is captured and put condition to get the IP address pattern referring to the older pattern only for the ip address. 
	ip_txt = "(Nmap scan report for .*)"
	#ip_txt = "([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}(?=\)*))"
	ip_pattern = re.compile(ip_txt, re.MULTILINE)
	itr = ip_pattern.finditer(str)
	
	cnt = 0
	start_pos = 0
	end_pos = 0
	prev = 0
	substr = ''
	ip = ''
	ip_final = ''
	addr_str = ''
	host_pattern_str = "(?P<IP>[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})"
		
	for match in itr:
		if cnt==0: # first iteration and we need the to skip the match.start() index
			prev = match.end()
			cnt = cnt + 1
			host_ip = re.compile(host_pattern_str)
			addr_str = match.group()
			ip = host_ip.search(addr_str)
		else:
			ip_final = ip
			start_pos = prev
			end_pos = match.start()
			substr = str[start_pos:end_pos]
			prev = match.end()
			#import pdb
			#pdb.set_trace()
			getPortDetails(substr, ip_final.group(), formatFlag, outputFile)
			host_ip = re.compile(host_pattern_str)
			addr_str = match.group()
			ip = host_ip.search(addr_str)
		
	# Follow the above steps to process the last host open ports which are not addressed in the above iteration.
	str_final = str[end_pos:]
	#host_ip_final = re.compile(host_pattern_str)
	ip_final = ip
	getPortDetails(str_final, ip_final.group(), formatFlag, outputFile)
	
	re.purge()	

if __name__ == "__main__":
	print('Nmap parsing module')
	
	if(len(sys.argv) < 4):
		print("Three arguments needed for the script [1. nmap output text file 2.Flag Value 3.Name of the parsed file you want].")
		sys.exit(1)
	else:
		inputFile = sys.argv[1]
		formatFlag = sys.argv[2] 
		outputFile = sys.argv[3]
			
		print('Arg 1 = ', inputFile)
		print('Arg 2 = ', formatFlag)
		print('Arg 3 =', outputFile)
			
		outputFile = outputFile + '.xlsx'
		print('Ouput File name is :- ', outputFile)
		
		parseNmapContents(inputFile, formatFlag, outputFile)
	
