import tensorflow as tf
import os
import numpy as np
import pandas as pd
import random
import sys


def predict(input, output, model_path, way=1):
    test_file = input
    if way == 1:
        test_sample = pd.read_csv(test_file, header=None, skiprows=1)
    else:
        test_sample = pd.read_csv(test_file, header=None)
    num = 602
    test_predict = []
    itera = []
    for x in range(0, len(test_sample) + 1 - num, num):
        itera.append(x)
    # Get samples by index
    for x in itera:
        test_predict.append(test_sample.iloc[x:x + num, ])

    test_predict = np.array(test_predict)
    print("Dimensions before modification: ",test_predict.shape)
    test_predict = np.expand_dims(test_predict,axis=3)
    print("After modifying the dimensions: ",test_predict.shape)

    model = tf.keras.models.load_model("./models/" + model_path)

    result = model.predict(test_predict)
    print("result:",result)
    print(type(result))
    if way == 1:
        with open(test_file, 'r', encoding='UTF8', newline='') as f:
            SplicePath = f.readline().strip()
        SplicePd = pd.read_csv(SplicePath)
        SplicePd['result'] = result[:, 1]
        SplicePd.to_csv(output)
        pred = tf.argmax(result, axis=1)
        print("pred:",pred)

    if way == 0:
        np.savetxt(output, result, delimiter=',')
        pred = tf.argmax(result, axis=1)
        print("pred:",pred)
        print(type(pred))


if __name__ == '__main__':
    parameter_dict = {}
    for user_input in sys.argv[1:]:
        if "=" not in user_input:  #
            continue
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        parameter_dict[varname] = varvalue

    way = 0
    model_path = ''
    if "organism" in parameter_dict:
        filepath = parameter_dict["organism"]
        if filepath == 'H_sapiens':
            model_path += "H_sapiens"
        elif filepath == 'D_melanogaster':
            model_path += "D_melanogaster"
        elif filepath == 'A_thaliana':
            model_path += "A_thaliana"
        elif filepath == 'C_elegans':
            model_path += "C_elegans"
        elif filepath == 'O_sativa_japonica':
            model_path += "O_sativa_japonica"
        else:
            print("Please input the correct parameters organism")
            sys.exit(0)
    else:
        print("Please input parameters organism")
        sys.exit(0)

    if "type" in parameter_dict:
        filepath = parameter_dict["type"]
        if filepath == 'donor':
            model_path += "_donor.h5"
        elif filepath == 'acceptor':
            model_path += "_acceptor.h5"
        else:
            print("Please input the correct parameters type")
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

    if "way" in parameter_dict:
        way = parameter_dict["way"]
        predict(filepath, outputfile, model_path, 0)
    else:
        predict(filepath, outputfile, model_path)