# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:


    with open(INPUT_FILENAME) as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w') as json_f:
        json.dump(data, json_f, indent=4)

    return json.dumps(data)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
