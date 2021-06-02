import os
import sys
sys.path.append('./..')
import environment as env


def print_antisem_dict():
    path = f'{env.HFLP_SCORES_ANTISEM_DIR}_10'
    files = os.listdir(path)
    print(files)
    scores = []
    print()
    for file in files:
        if file.split('_')[0] == "weimar":
            slice = file.split('_')[0]
            dimension = file.split('_')[1].replace('.txt', '')
        elif file.split('_')[0] == "ns":
            slice = file.split('_')[0]
            dimension = file.split('_')[1].replace('.txt', '')
        else:
            slice = file.split('_')[0] + file.split('_')[1]
            dimension = file.split('_')[2].replace('.txt', '')
        if '.txt' in file:
            # print(file)
            with open(f'{path}/{file}', 'r') as f:
                data = f.readlines()
                score_1 = float(data[18].split(',')[0].split(':')[1])
                score_2 = float(data[20].split(',')[0].split(':')[1])
                score_3 = float(data[22].split(',')[0].split(':')[1])
                score_4 = float(data[24].split(',')[0].split(':')[1])
                result = {"method": "PPMI", "slice": slice, "dimension": dimension, "score_1": score_1,
                          "score_2": score_2,
                          "score_3": score_3, "score4": score_4}
                scores.append(result)
                f.close()

    # for score in scores:
    #     print(score)

    sentiment = []
    patriotism = []
    economy = []
    conspiracy = []
    religion = []
    racism = []
    ethics = []

    for score in scores:
        if score["dimension"] == "sentiment":
            sentiment.append(score)
        if score["dimension"] == "patriotic":
            patriotism.append(score)
        if score["dimension"] == "economic":
            economy.append(score)
        if score["dimension"] == "conspiratorial":
            conspiracy.append(score)
        if score["dimension"] == "religious":
            religion.append(score)
        if score["dimension"] == "racist":
            racism.append(score)
        if score["dimension"] == "ethic":
            ethics.append(score)
    """
    for score in sentiment:
        print(score)
    print()
    for score in patriotism:
        print(score)
    print()
    for score in economy:
        print(score)
    print()
    for score in conspiracy:
        print(score)
    print()
    for score in religion:
        print(score)
    print()
    for score in racism:
        print(score)
    print()
    for score in ethics:
        print(score)
    print()

"""
    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[8]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[2]) + ",")
    print('\n')
    print(str(patriotism[3]) + ",")
    print(str(patriotism[4]) + ",")
    print(str(patriotism[8]) + ",")
    print(str(patriotism[5]) + ",")
    print(str(patriotism[0]) + ",")
    print(str(patriotism[6]) + ",")
    print(str(patriotism[1]) + ",")
    print(str(patriotism[7]) + ",")
    print(str(patriotism[2]) + ",")
    print('\n')
    print(str(economy[3]) + ",")
    print(str(economy[4]) + ",")
    print(str(economy[8]) + ",")
    print(str(economy[5]) + ",")
    print(str(economy[0]) + ",")
    print(str(economy[6]) + ",")
    print(str(economy[1]) + ",")
    print(str(economy[7]) + ",")
    print(str(economy[2]) + ",")
    print('\n')
    print(str(conspiracy[3]) + ",")
    print(str(conspiracy[4]) + ",")
    print(str(conspiracy[8]) + ",")
    print(str(conspiracy[5]) + ",")
    print(str(conspiracy[0]) + ",")
    print(str(conspiracy[6]) + ",")
    print(str(conspiracy[1]) + ",")
    print(str(conspiracy[7]) + ",")
    print(str(conspiracy[2]) + ",")
    print('\n')
    print(str(religion[3]) + ",")
    print(str(religion[4]) + ",")
    print(str(religion[8]) + ",")
    print(str(religion[5]) + ",")
    print(str(religion[0]) + ",")
    print(str(religion[6]) + ",")
    print(str(religion[1]) + ",")
    print(str(religion[7]) + ",")
    print(str(religion[2]) + ",")
    print('\n')
    print(str(racism[3]) + ",")
    print(str(racism[4]) + ",")
    print(str(racism[8]) + ",")
    print(str(racism[5]) + ",")
    print(str(racism[0]) + ",")
    print(str(racism[6]) + ",")
    print(str(racism[1]) + ",")
    print(str(racism[7]) + ",")
    print(str(racism[2]) + ",")
    print('\n')
    print(str(ethics[3]) + ",")
    print(str(ethics[4]) + ",")
    print(str(ethics[8]) + ",")
    print(str(ethics[5]) + ",")
    print(str(ethics[0]) + ",")
    print(str(ethics[6]) + ",")
    print(str(ethics[1]) + ",")
    print(str(ethics[7]) + ",")
    print(str(ethics[2]) + ",")

def print_anticom_dict():
    path = f'{env.HFLP_SCORES_ANTICOM_DIR}_10'
    files = os.listdir(path)
    print(files)
    scores = []
    print()
    for file in files:
        if file.split('_')[0] == "weimar":
            slice = file.split('_')[0]
            dimension = file.split('_')[1].replace('.txt', '')
        elif file.split('_')[0] == "ns":
            slice = file.split('_')[0]
            dimension = file.split('_')[1].replace('.txt', '')
        else:
            slice = file.split('_')[0] + file.split('_')[1]
            dimension = file.split('_')[2].replace('.txt', '')
        if '.txt' in file:
            # print(file)
            with open(f'{path}/{file}', 'r') as f:
                data = f.readlines()
                score_1 = float(data[10].split(',')[0].split(':')[1])
                result = {"method": "PPMI", "slice": slice, "dimension": dimension, "score_1": score_1}
                scores.append(result)
                f.close()

    sentiment = []
    political = []
    propaganda = []

    for score in scores:
        if score["dimension"] == "sentiment":
            sentiment.append(score)
        if score["dimension"] == "political":
            political.append(score)
        if score["dimension"] == "propaganda":
            propaganda.append(score)

    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[8]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[2]) + ",")
    print('\n')
    print(str(political[3]) + ",")
    print(str(political[4]) + ",")
    print(str(political[8]) + ",")
    print(str(political[5]) + ",")
    print(str(political[0]) + ",")
    print(str(political[6]) + ",")
    print(str(political[1]) + ",")
    print(str(political[7]) + ",")
    print(str(political[2]) + ",")
    print('\n')
    print(str(propaganda[3]) + ",")
    print(str(propaganda[4]) + ",")
    print(str(propaganda[8]) + ",")
    print(str(propaganda[5]) + ",")
    print(str(propaganda[0]) + ",")
    print(str(propaganda[6]) + ",")
    print(str(propaganda[1]) + ",")
    print(str(propaganda[7]) + ",")
    print(str(propaganda[2]) + ",")


# print_anticom_dict()
print_antisem_dict()
