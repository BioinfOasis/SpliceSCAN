import pandas as pd
import csv
import sys

def encoding(input, output):
    filePath = input
    file = pd.read_csv(filePath)
    # print(file['hit'])
    # print(len(file['hit'][0]))
    # print(len(file['hit']))
    with open(output, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([input])
        for i in range(len(file['hit'])):
            for j in range(602):
                if file['hit'][i][j] == 'A':
                    writer.writerow([1, 0, 0, 0])
                elif file['hit'][i][j] == 'C':
                    writer.writerow([0, 1, 0, 0])
                elif file['hit'][i][j] == 'G':
                    writer.writerow([0, 0, 1, 0])
                elif file['hit'][i][j] == 'T':
                    writer.writerow([0, 0, 0, 1])

if __name__ == '__main__':
    parameter_dict = {}
    for user_input in sys.argv[1:]:
        if "=" not in user_input:  #
            continue
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        parameter_dict[varname] = varvalue

    if "input" in parameter_dict:
        filepath = parameter_dict["input"]
    else:
        print("Please input parameters input")
        sys.exit(0)

    if "output" in parameter_dict:
        outputfile = parameter_dict["output"]
    else:
        print("Please input parameters output")
        sys.exit(0)
    encoding(filepath, outputfile)