import json
import pickle
import numpy as np
__regions = None
__data_columns = None
__model = None

def get_estimatied_price(region,age, sex, bmi, children, smoker):
    try:
        reg_index = __data_columns.index(region.lower())
    except:
        reg_index=-1

    a = np.zeros(len(__data_columns))
    a[0] = age
    a[1] = sex
    a[2] = bmi
    a[3] = children
    a[4] = smoker
    if reg_index >= 0:
        a[reg_index] = 1
    return round(__model.predict([a])[0],2)

def get_region():
    return __regions

def load_save_artifacts():
    print("Loading save artifacts... start")
    global __data_columns
    global __regions

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __regions = __data_columns[5:]

    global __model
    with open("./artifacts/MC.pickle",'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")


if __name__ == '__main__':

    load_save_artifacts()
    print(get_region())
    print(get_estimatied_price('southwest',26,1,27,3,1))
    print(get_estimatied_price('southwest', 26, 1, 27, 3, 0))