from logging import getLogger
import argparse
import json
from services.build_graph import graph

logger = getLogger()


def load_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Specify a file name', required=False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    filename = args.file
    data = load_json_file('data/big.json')

    graph_data = graph(data)
    print(graph_data.model_dump_json())
