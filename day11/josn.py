import json


def dumps_json():
    p_dict = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }
    json_str = json.dumps(p_dict)
    print(json_str)


def dump_json():
    p_dict = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }
    with open('data.json', mode='w') as f:
        json.dump(p_dict, f)


def load_json():
    with open('data.json', 'r', encoding='utf8') as f:
        p_dict = json.load(f)
    print(p_dict)


def loads_json():
    json_str = '{"name": "骆昊","age": 38,"qq": 957658,"friends": ["王大锤", "白元芳"],"cars": [{"brand": "BYD", "max_speed": 180},{"brand": "Audi", "max_speed": 280},{"brand": "Benz", "max_speed": 320}]}'
    p_dict = json.loads(json_str)
    print(p_dict)


def main():
    dumps_json()
    dump_json()
    load_json()
    loads_json()


if __name__ == '__main__':
    main()
