import pandas as pd
import os
import sys
sys.path.append('./..')
import environment as env

DIMENSIONS_SEM = ['sentiment', 'patriotism', 'economic', 'conspiratorial', 'religious', 'racist', 'ethic']
DIMENSIONS_COM = ["sentiment", "political", "propaganda"]

ECT_DIR = ""
WEAT_DIR = ""
DIMENSIONS = []


def prepare_ect_scores():
    dirs = os.listdir(ECT_DIR)
    # print(dirs)
    scores = []
    data = []
    for file in dirs:
        ect_path = ECT_DIR + '/' + file
        scores.append(pd.read_csv(ect_path))
    counter = 0
    for file in dirs:
        for dimension in DIMENSIONS:
            result = float(scores[counter][dimension][1])
            print(result)
            specification = dimension
            title = file.replace("_score.csv", "")
            # specification = "antisemitism_" + dimension
            data.append({"slice": title, "specification": specification, "measure": "ECT", "score": result})
        counter += 1
    return data



def prepare_weat_scores():
    dirs = os.listdir(WEAT_DIR)
    # print(dirs)
    scores = []
    for file in dirs:
        titles = file.split("_")
        # print(titles)
        specification = titles[1]
        measure = "WEAT"
        slice = ""
        if titles[2] == 'weimar.txt':
            slice = titles[2]
        else:
            slice = titles[2] + titles[3]
        slice = slice.replace('.txt', '') 
        file_path = WEAT_DIR + '/' + file
        file_data = open(file_path, "r")
        data = file_data.readlines()
        significance = True
        if "False" in data[0]:
            significance = False
        result_data = data[1].split(',')
        effect_size = float(result_data[1])

        scores.append({"slice": slice, "specification": specification, "measure": measure, "score": effect_size,
                       "significance": significance})
    return scores


def print_scores_anticom(scores):
    
    sentiment = []
    political = []
    propaganda = []

    for score in scores:
        if score["specification"] == "sentiment":
            sentiment.append(score)
        if score["specification"] == "political":
            political.append(score)
        if score["specification"] == "propaganda":
            propaganda.append(score)

    print()
    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[2]) + ",")
    print('\n')
    print(str(political[3]) + ",")
    print(str(political[4]) + ",")
    print(str(political[7]) + ",")
    print(str(political[0]) + ",")
    print(str(political[5]) + ",")
    print(str(political[1]) + ",")
    print(str(political[6]) + ",")
    print(str(political[2]) + ",")
    print('\n')
    print(str(propaganda[3]) + ",")
    print(str(propaganda[4]) + ",")
    print(str(propaganda[7]) + ",")
    print(str(propaganda[0]) + ",")
    print(str(propaganda[5]) + ",")
    print(str(propaganda[1]) + ",")
    print(str(propaganda[6]) + ",")
    print(str(propaganda[2]) + ",")


def print_scores_antisem(scores):

    sentiment = []
    patriotism = []
    economy = []
    conspiracy = []
    religion = []
    racism = []
    ethics = []

    for score in scores:
        if score["specification"] == "sentiment":
            sentiment.append(score)
        if score["specification"] == "patriotism":
            patriotism.append(score)
        if score["specification"] == "economic":
            economy.append(score)
        if score["specification"] == "conspiratorial":
            conspiracy.append(score)
        if score["specification"] == "religious":
            religion.append(score)
        if score["specification"] == "racist":
            racism.append(score)
        if score["specification"] == "ethic":
            ethics.append(score)

    print()
    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[2]) + ",")
    print('\n')
    print(str(patriotism[3]) + ",")
    print(str(patriotism[4]) + ",")
    print(str(patriotism[7]) + ",")
    print(str(patriotism[0]) + ",")
    print(str(patriotism[5]) + ",")
    print(str(patriotism[1]) + ",")
    print(str(patriotism[6]) + ",")
    print(str(patriotism[2]) + ",")
    print('\n')
    print(str(economy[3]) + ",")
    print(str(economy[4]) + ",")
    print(str(economy[7]) + ",")
    print(str(economy[0]) + ",")
    print(str(economy[5]) + ",")
    print(str(economy[1]) + ",")
    print(str(economy[6]) + ",")
    print(str(economy[2]) + ",")
    print('\n')
    print(str(conspiracy[3]) + ",")
    print(str(conspiracy[4]) + ",")
    print(str(conspiracy[7]) + ",")
    print(str(conspiracy[0]) + ",")
    print(str(conspiracy[5]) + ",")
    print(str(conspiracy[1]) + ",")
    print(str(conspiracy[6]) + ",")
    print(str(conspiracy[2]) + ",")
    print('\n')
    print(str(religion[3]) + ",")
    print(str(religion[4]) + ",")
    print(str(religion[7]) + ",")
    print(str(religion[0]) + ",")
    print(str(religion[5]) + ",")
    print(str(religion[1]) + ",")
    print(str(religion[6]) + ",")
    print(str(religion[2]) + ",")
    print('\n')
    print(str(racism[3]) + ",")
    print(str(racism[4]) + ",")
    print(str(racism[7]) + ",")
    print(str(racism[0]) + ",")
    print(str(racism[5]) + ",")
    print(str(racism[1]) + ",")
    print(str(racism[6]) + ",")
    print(str(racism[2]) + ",")
    print('\n')
    print(str(ethics[3]) + ",")
    print(str(ethics[4]) + ",")
    print(str(ethics[7]) + ",")
    print(str(ethics[0]) + ",")
    print(str(ethics[5]) + ",")
    print(str(ethics[1]) + ",")
    print(str(ethics[6]) + ",")
    print(str(ethics[2]) + ",")



if env.AREA == "antisem":
    ECT_DIR = os.path.join(env.ECT_OUTPUTS, "antisem")
    WEAT_DIR = os.path.join(env.WEAT_OUTPUTS, "antisem")
    DIMENSIONS = DIMENSIONS_SEM
    weat_scores = prepare_weat_scores()
    ect_scores = prepare_ect_scores()
    print_scores_antisem(weat_scores)
    print_scores_antisem(ect_scores)

if env.AREA == "anticom":
    ECT_DIR = os.path.join(env.ECT_OUTPUTS, "anticom")
    WEAT_DIR = os.path.join(env.WEAT_OUTPUTS, "anticom")
    DIMENSIONS = DIMENSIONS_COM
    weat_scores = prepare_weat_scores()
    ect_scores = prepare_ect_scores()
    print_scores_anticom(weat_scores)
    print_scores_anticom(ect_scores)
