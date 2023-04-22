import csv
import argparse

parser = argparse.ArgumentParser(description='Process a CSV file of hosts and ports.')
parser.add_argument('filename', type=str, help='the name of the CSV file')
args = parser.parse_args()

with open(args.filename) as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    # Create a dictionary to store the hosts, ports, and plugin output for each name
    names_dict = {}

    # Loop through each row and add the host, port, and plugin output to the dictionary for the corresponding name
    for row in reader:
        host = row[0]
        protocol = row[1]
        port = row[2]
        name = row[3]
        plugin_output = row[4]

        if name not in names_dict:
            names_dict[name] = []
        names_dict[name].append((host, port, plugin_output))

    # Print the list of hosts, ports, and plugin output for each name
    for name, hosts_ports_plugins in names_dict.items():
        print(f"{name}:")
        for host, port, plugin_output in hosts_ports_plugins:
            print(f" {host}:{port} - {plugin_output}")
