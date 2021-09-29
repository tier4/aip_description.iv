import argparse
from pathlib import Path
from typing import Dict

import ruamel.yaml
from ruamel.yaml.scalarfloat import ScalarFloat

yaml = ruamel.yaml.YAML()


def convert(data: Dict[str, Dict[str, ScalarFloat]]):
    new_data = {}
    for name, pose in data.items():
        frame_from, frame_to = name.split('2', 1)
        for column, value in pose.items():
            if not new_data.get(frame_from):
                new_data[frame_from] = {}

            if not new_data[frame_from].get(frame_to):
                new_data[frame_from][frame_to] = {}

            new_data[frame_from][frame_to][column] = value

    return new_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        data = yaml.load(f)
        new_data = convert(data)

    with open(args.input, 'w') as f:
        yaml.dump(new_data, f)


if __name__ == '__main__':
    main()
