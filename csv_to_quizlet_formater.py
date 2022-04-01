pinyin = []
chinese = []
english = []

def extract_new_data(pin, chi, eng):
    f = open("lesson 1.csv", 'r', encoding='utf-8')
    for line in f.readlines():
        splitted = line.split(",")
        pin.append(splitted[0])
        chi.append(splitted[1])
        eng.append(splitted[2][0:-1])
    return pin, chi, eng

def write_data_exel(pin, chi, eng):
    with open('chinese_excel.csv', 'w', newline='', encoding='utf-8') as f:
        for i in range(0, len(pin)):
            f.write("{},{},{}\n".format(pin[i], chi[i], eng[i]))

def write_data_easy(pin, chi, eng):
    with open('chinese_easy.csv', 'w', newline='', encoding='utf-8') as f:
        for i in range(0, len(pin)):
            f.write("{} ({}),{}\n".format(pin[i], chi[i], eng[i]))

def write_data_hard(pin, chi, eng):
    with open('chinese_hard.csv', 'w', newline='', encoding='utf-8') as f:
        for i in range(0, len(pin)):
            f.write("{},{} ({})\n".format(chi[i], eng[i], pin[i]))


if "__main__" == __name__:
    extract_new_data(pinyin, chinese, english)
    write_data_exel(pinyin, chinese, english)
    write_data_easy(pinyin, chinese, english)
    write_data_hard(pinyin, chinese, english)
