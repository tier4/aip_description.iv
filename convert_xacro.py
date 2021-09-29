import argparse
import re
from pathlib import Path


def convert(data):
    new_data = data

    all_names = set(re.findall(r"calibration\['(\w+2\w+)'\]", data))

    for name in all_names:
        frame_from, frame_to = name.split('2', 1)
        new_data = re.sub(
            rf"calibration\['{name}'\]", rf"calibration['{frame_from}']['{frame_to}']", new_data
        )

    return new_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        data = f.read()
        new_data = convert(data)

    with open(args.input, 'w') as f:
        f.write(new_data)


if __name__ == '__main__':
    main()
