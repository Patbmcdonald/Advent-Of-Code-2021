import pathlib

PATH = pathlib.Path(__file__).parent.absolute()


def read_lines(datapath):
    with open(f"{PATH}/data/{datapath}") as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


def read_file_to_list(datapath, strip=True):
    file = open(f"{PATH}/data/{datapath}")
    file_list = file.readlines()
    if strip:
        return [line.strip() for line in file_list]
    return file_list


def convert_str_to_int_list(thisList) -> list[int]:
    return [int(i) for i in thisList]

def convert_int_list_to_int(integers: list[int]) -> int:
    return int("".join([str(integer) for integer in integers]))

def convert_int_list_to_str(integers: list[int]) -> str:
    return "".join([str(integer) for integer in integers])
    