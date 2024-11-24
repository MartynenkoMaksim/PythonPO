import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    total_sum = sum(item.get('score') * item.get('weight') for item in json_data)
    return (f"{total_sum:.3f}")

print(task())
