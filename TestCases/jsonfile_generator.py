import json
import argparse

'''
To use this program, enter command like:
python3 jsonfile_generator.py --HW_name ECE264-HW2 --case_num 5
'''


def get_args():
    parser = argparse.ArgumentParser("please add weights here")
    parser.add_argument("--HW_name", type=str, default="ECE264-HW1",
                        help="name of the homework")  # Get name of the homework from terminal
    parser.add_argument("--case_num", type=int, default=5,
                        help="total number of testcases")  # Get total number of testcases from terminal
    parser.add_argument("--mem_coef", type=float, default=0.01,
                        help="the weight for memory leak")  # Get weight of memory leak per byte from terminal
    parser.add_argument("--late-coef", type=float, default=0.01)  # Get penalty weight of late submission per hour
    # add more arguments here with similar format

    args = parser.parse_args()
    return args


def generate_json_file(params):
    name = params.HW_name
    test_params = {}  # Write the inner keys
    json_text = {'weights': []}  # Write the outer key
    case_num = params.case_num

    # if not given specific weight for each testcase, the weights will be equally distributed
    for i in range(case_num):
        test_params['test%d' % (i + 1)] = 1 / case_num

    '''
    to indicate weight for each testcase, write code like:
        test_params['test1'] = 0.1
        test_params['test2'] = 0.2
        ...
    '''

    test_params["mem_coef"] = params.mem_coef
    test_params["late_coef"] = params.late_coef
    for item in test_params:
        value = test_params[item]
        json_text['weights'].append({item: [value]}, )
    json_data = json.dumps(json_text, indent=4, separators=(',', ': '))  # Make Json file looks better
    filename = name + '.json'
    f = open(filename, 'w')
    f.write(json_data)
    f.close()


if __name__ == '__main__':
    params = get_args()
    generate_json_file(params)
