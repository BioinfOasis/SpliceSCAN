import csv
import sys


def readSplitFasta(input, output, way):
    splitFile = open(output, 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(splitFile)
    csv_writer.writerow(['sequence', 'position', 'hit', 'result'])
    with open(input, 'r') as reads:
        if way == 1:
            while True:
                sequence = reads.readline().rstrip()
                read = reads.readline().rstrip()
                if len(sequence) > 0:
                    length = len(read)
                    if length >= 602:
                        for i in range(300, length):
                            if read[i] == 'G' and read[i + 1] == 'T' and (length - i) >= 301:
                                csv_writer.writerow([sequence, i, read[i - 300: i + 302]])
                else:
                    break
        elif way == 0:
            while True:
                sequence = reads.readline().rstrip()
                read = reads.readline().rstrip()
                if len(sequence) > 0:
                    length = len(read)
                    if length >= 602:
                        for i in range(300, length):
                            if read[i] == 'A' and read[i + 1] == 'G' and (length - i) >= 301:
                                csv_writer.writerow([sequence, i, read[i - 300: i + 302]])
                else:
                    break
    splitFile.close()


if __name__ == '__main__':
    parameter_dict = {}
    for user_input in sys.argv[1:]:
        if "=" not in user_input:  #
            continue
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        parameter_dict[varname] = varvalue

    way = 0
    if "type" in parameter_dict:
        filepath = parameter_dict["type"]
        if filepath == 'donor':
            way = 1
        elif filepath == 'accepter':
            way = 0
        else:
            sys.exit(0)
    else:
        print("Please input parameters type")
        sys.exit(0)

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
    readSplitFasta(filepath, outputfile, way)
