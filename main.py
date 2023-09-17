import json

import Gen_num
import Moooooon_ALG


def read_json(variant: str) -> dict:
    result = {
        "hash": '',
        "bins": [],
        "last_num": '',
        "hash_format": ''
    }
    with open("parametrs.json", "r") as file:
        data = json.load(file)
        result["hash"] = data[variant]["hash"]
        result["last_num"] = data[variant]["last_numbers"]
        for i in range(len(data[variant]["bins"])):
            result["bins"].append(data[variant]["bins"][i])
        result["hash_format"] = data[variant]["hash_format"]
    print(result)
    return result


if __name__ == "__main__":
    Moooooon_ALG.luna('2200700417413837')
    data = read_json("15")
    Gen_num.check_hash(data["bins"][1], 41741, data["last_num"], data["hash"], data["hash_format"])


