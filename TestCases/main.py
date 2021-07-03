import json
import argparse


def get_args():
    parser = argparse.ArgumentParser("please add weights here")
    parser.add_argument("--HW_name", type=str, default="ECE264-HW1", help="name of the homework")
    parser.add_argument("--case_num", type=int, default=5, help="total number of testcases")
    parser.add_argument("--testcase", type=float, default=0.9, help="the weight for testcases")
    parser.add_argument("--mem_leak", type=float, default=0.1, help="the weight for memory leak")
    # add more arguments here with similar format

    args = parser.parse_args()
    return args


def generate_json_file(params):
    name=params.HW_name
    test_params = {"case_num": params.case_num,
                   "testcase": params.testcase,
                   "mem_leak": params.mem_leak}
    json_text = {'weights': []}
    for item in test_params:
        value = test_params[item]
        json_text['weights'].append({item: [value]}, )
    json_data = json.dumps(json_text, indent=4, separators=(',', ': '))
    filename = name+'.json'
    f = open(filename, 'w')
    f.write(json_data)
    f.close()


if __name__ == '__main__':
    params = get_args()
    generate_json_file(params)
