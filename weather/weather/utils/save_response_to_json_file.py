from enum import Enum
class InputType(Enum):
    RESP = 'resp'
    JSON = 'json'
    BYTES = 'bytes'
    DICT = 'dict'
    LIST = 'list'


def save_response_to_file(obj, input_type):
    match input_type:
        case 'resp':

    json_object = json.dumps(found_cityes, indent=4, ensure_ascii=False)

    with open("json_response.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)