import csv
import argparse

parser = argparse.ArgumentParser(description='Process a CSV file of hosts and ports.')
parser.add_argument('filename', type=str, help='the name of the CSV file')
args = parser.parse_args()

ports_by_host = {}

with open(args.filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        host = row['Host']
        port = row['Port']
        if host not in ports_by_host:
            ports_by_host[host] = set()
        ports_by_host[host].add(port)

for host, ports in ports_by_host.items():
    print(f"{host} -p {','.join(ports)}")