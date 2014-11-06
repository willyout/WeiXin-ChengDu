# -*- coding: utf-8 -*-

def readfile():
    data = {}
    with open('../data/citycodes', 'r') as cityfile:
        # for line in cityfile.readlines():
        for line in cityfile:
            # print(type(line))
            city = line.decode('utf-8')
            if 'city_table' in city and 'VALUES' in city:
                citycode = city.strip().split(',')
                key = citycode[-2][1:-1]
                value = citycode[-1][1:-3]
                data[key] = value
    return data


def writefile():
    data = readfile()

    citycode = ''
    with open('../data/citycode', 'w+') as cityfile:
        for key, value in data.items():
            line = key + ' ' + value + '\n'
            citycode = citycode + line

        cityfile.write(citycode.encode('utf-8'))

if __name__ == '__main__':
    writefile()
