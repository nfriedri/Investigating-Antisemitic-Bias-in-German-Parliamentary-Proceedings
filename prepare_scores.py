import os
import environment as env

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# new_Path = os.path.join(os.path.curdir, "fu_scores")
new_Path = env.HFLP_SCORES_ANTISEM_DIR
# new_Path = os.path.join(os.path.curdir, "evaluation", "t_test")


def plot_all_lines(data, statistic, title):


    data_list = []
    for d in data:
        if d["method"] == statistic:
            data_list.append(d)
    df = pd.DataFrame(data_list)
    sns.set_theme()

    g = sns.catplot(
        data=df, kind="bar",
        x="slice", y="score1", hue="dimension",
        alpha=.6, height=6, palette="hls"
    )

    g.despine(left=True)
    g.set_axis_labels("", statistic)
    g.legend.set_title("View")
    g.legend.loc = "upper right"



    plt.savefig(f'{title}.pdf')


def prepare_antisem_scores():
    files = os.listdir(env.HFLP_SCORES_ANTISEM_DIR)
    print(files)
    for file in files:
        if '.npy' in file:
            files.remove(file)
    print(files)

    scores = []

    for file in files:
        score = {}
        with open(os.path.join(env.HFLP_SCORES_ANTISEM_DIR, file), "r") as f:
            data = f.readlines()
            """
            value_1 = float(data[0].rsplit(":")[1].rsplit(",")[0])
            print(value_1)
            """
            value_1 = float(data[18].rsplit(":")[1].rsplit(",")[0])
            # value_2 = float(data[20].rsplit(":")[1].rsplit(",")[0])
            # value_3 = float(data[22].rsplit(":")[1].rsplit(",")[0])
            # value_4 = float(data[24].rsplit(":")[1].rsplit(",")[0])
            # value_mean = (value_1 + value_2 + value_3 + value_4) / 4
            
            filenames = file.replace(".txt", "").rsplit("_")
            slice = ""
            dimension = ""
            if filenames[0] == 'cdu' or filenames[0] == 'spd' or filenames[0] == 'kaiserreich':
                slice = filenames[0] + filenames[1]
                if filenames[0] == 'kaiserreich':
                    slice = 'kr' + filenames[1]
                dimension = filenames[2]
            else:
                slice = filenames[0]
                dimension = filenames[1]
            
            # score = {"measure": "LP", "slice": slice, "dimension": dimension, "score": value_mean, "score1": value_1,
            #          "score2": value_2, "score3": value_3, "score4": value_4}
            score = {"measure": "LP", "slice": slice, "dimension": dimension, "score": value_1}
        scores.append(score)

    sentiment = []
    patriotic = []
    economic = []
    conspiratorial = []
    religious = []
    racism = []
    ethic = []

    for value in scores:
        if value["dimension"] == "sentiment":
            sentiment.append(value)
        if value["dimension"] == "patriotic":
            patriotic.append(value)
        if value["dimension"] == "economic":
            economic.append(value)
        if value["dimension"] == "conspiratorial":
            conspiratorial.append(value)
        if value["dimension"] == "religious":
            religious.append(value)
        if value["dimension"] == "racist":
            racism.append(value)
        if value["dimension"] == "ethic":
            ethic.append(value)
    """
    result = [sentiment[3], sentiment[4], sentiment[7], sentiment[0], sentiment[5], sentiment[1],
              sentiment[6], sentiment[2], patriotic[3], patriotic[4], patriotic[7], patriotic[0],
              patriotic[5], patriotic[1], patriotic[6], patriotic[2], economic[3], economic[4], economic[7],
              economic[0], economic[5], economic[1], economic[6], economic[2], conspiratorial[3],
              conspiratorial[4], conspiratorial[7], conspiratorial[0], conspiratorial[5],
              conspiratorial[1], conspiratorial[6], conspiratorial[2], religious[3], religious[4], religious[7],
              religious[0], religious[5], religious[1], religious[6], religious[2], racism[3], racism[4],
              racism[7], racism[0], racism[5], racism[1], racism[6], racism[2], ethic[3], ethic[4], ethic[7],
              ethic[0], ethic[5], ethic[1], ethic[6], ethic[2]]

    return result
    """   
    print()

    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[8]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[2]) + ",")
    print()

    print(str(patriotic[3]) + ",")
    print(str(patriotic[4]) + ",")
    print(str(patriotic[8]) + ",")
    print(str(patriotic[5]) + ",")
    print(str(patriotic[0]) + ",")
    print(str(patriotic[6]) + ",")
    print(str(patriotic[1]) + ",")
    print(str(patriotic[7]) + ",")
    print(str(patriotic[2]) + ",")
    print()

    print(str(economic[3]) + ",")
    print(str(economic[4]) + ",")
    print(str(economic[8]) + ",")
    print(str(economic[5]) + ",")
    print(str(economic[0]) + ",")
    print(str(economic[6]) + ",")
    print(str(economic[1]) + ",")
    print(str(economic[7]) + ",")
    print(str(economic[2]) + ",")
    print()

    print(str(conspiratorial[3]) + ",")
    print(str(conspiratorial[4]) + ",")
    print(str(conspiratorial[8]) + ",")
    print(str(conspiratorial[5]) + ",")
    print(str(conspiratorial[0]) + ",")
    print(str(conspiratorial[6]) + ",")
    print(str(conspiratorial[1]) + ",")
    print(str(conspiratorial[7]) + ",")
    print(str(conspiratorial[2]) + ",")
    print()

    print(str(religious[3]) + ",")
    print(str(religious[4]) + ",")
    print(str(religious[8]) + ",")
    print(str(religious[5]) + ",")
    print(str(religious[0]) + ",")
    print(str(religious[6]) + ",")
    print(str(religious[1]) + ",")
    print(str(religious[7]) + ",")
    print(str(religious[2]) + ",")
    print()

    print(str(racism[3]) + ",")
    print(str(racism[4]) + ",")
    print(str(racism[8]) + ",")
    print(str(racism[5]) + ",")
    print(str(racism[0]) + ",")
    print(str(racism[6]) + ",")
    print(str(racism[1]) + ",")
    print(str(racism[7]) + ",")
    print(str(racism[2]) + ",")
    print()

    print(str(ethic[3]) + ",")
    print(str(ethic[4]) + ",")
    print(str(ethic[8]) + ",")
    print(str(ethic[5]) + ",")
    print(str(ethic[0]) + ",")
    print(str(ethic[6]) + ",")
    print(str(ethic[1]) + ",")
    print(str(ethic[7]) + ",")
    print(str(ethic[2]) + ",")
    print()

    result = [sentiment[3], sentiment[4], sentiment[8], sentiment[5], sentiment[0], sentiment[6], sentiment[1],
              sentiment[7], sentiment[2], patriotic[3], patriotic[4], patriotic[8], patriotic[5], patriotic[0],
              patriotic[6], patriotic[1], patriotic[7], patriotic[2], economic[3], economic[4], economic[8],
              economic[5], economic[0], economic[6], economic[1], economic[7], economic[2], conspiratorial[3],
              conspiratorial[4], conspiratorial[8], conspiratorial[5], conspiratorial[0], conspiratorial[6],
              conspiratorial[1], conspiratorial[7], conspiratorial[2], racism[3], racism[4],
              racism[8], racism[5], racism[0], racism[6], racism[1], racism[7], racism[2], religious[3], religious[4], religious[8],
              religious[5], religious[0], religious[6], religious[1], religious[7], religious[2],  ethic[3], ethic[4], ethic[8],
              ethic[5], ethic[0], ethic[6], ethic[1], ethic[7], ethic[2]]

    return result

def prepare_anticom_scores():
    files = os.listdir(env.HFLP_SCORES_ANTICOM_DIR)
    print(files)
    for file in files:
        if '.npy' in file:
            files.remove(file)
    print(files)

    scores = []

    for file in files:
        score = {}
        with open(os.path.join(env.HFLP_SCORES_ANTICOM_DIR, file), "r") as f:
            data = f.readlines()
            """
            value_1 = float(data[0].rsplit(":")[1].rsplit(",")[0])
            print(value_1)
            """
            value_1 = float(data[10].rsplit(":")[1].rsplit(",")[0])
            
            filenames = file.replace(".txt", "").rsplit("_")
            slice = ""
            dimension = ""
            if filenames[0] == 'cdu' or filenames[0] == 'spd' or filenames[0] == 'kaiserreich':
                slice = filenames[0] + filenames[1]
                if filenames[0] == 'kaiserreich':
                    slice = 'kr' + filenames[1]
                dimension = filenames[2]
            else:
                slice = filenames[0]
                dimension = filenames[1]
            
            score = {"method": "HFLP", "slice": slice, "dimension": dimension, "score1": value_1}
        scores.append(score)

    sentiment = []
    political = []
    propaganda = []

    for value in scores:
        if value["dimension"] == "sentiment":
            sentiment.append(value)
        if value["dimension"] == "political":
            political.append(value)
        if value["dimension"] == "propaganda":
            propaganda.append(value)
        
    """
    # Without NS slice
    result = [sentiment[3], sentiment[4], sentiment[7], sentiment[0], sentiment[5], sentiment[1],
              sentiment[6], sentiment[2], political[3], political[4], political[7], political[0],
              political[5], political[1], political[6], political[2], propaganda[3], propaganda[4], propaganda[7],
              propaganda[0], propaganda[5], propaganda[1], propaganda[6], propaganda[2]]

    return result
    """
    # With all Slices
    print()
    print(str(sentiment[3]) + ",")
    print(str(sentiment[4]) + ",")
    print(str(sentiment[8]) + ",")
    print(str(sentiment[5]) + ",")
    print(str(sentiment[0]) + ",")
    print(str(sentiment[6]) + ",")
    print(str(sentiment[1]) + ",")
    print(str(sentiment[7]) + ",")
    print(str(sentiment[2]) + ",")
    print()

    print(str(political[3]) + ",")
    print(str(political[4]) + ",")
    print(str(political[8]) + ",")
    print(str(political[5]) + ",")
    print(str(political[0]) + ",")
    print(str(political[6]) + ",")
    print(str(political[1]) + ",")
    print(str(political[7]) + ",")
    print(str(political[2]) + ",")
    print()

    print(str(propaganda[3]) + ",")
    print(str(propaganda[4]) + ",")
    print(str(propaganda[8]) + ",")
    print(str(propaganda[5]) + ",")
    print(str(propaganda[0]) + ",")
    print(str(propaganda[6]) + ",")
    print(str(propaganda[1]) + ",")
    print(str(propaganda[7]) + ",")
    print(str(propaganda[2]) + ",")
    print()

    

    result = [sentiment[3], sentiment[4], sentiment[8], sentiment[5], sentiment[0], sentiment[6], sentiment[1],
              sentiment[7], sentiment[2], political[3], political[4], political[8], political[5], political[0],
              political[6], political[1], political[7], political[2], propaganda[3], propaganda[4], propaganda[8],
              propaganda[5], propaganda[0], propaganda[6], propaganda[1], propaganda[7], propaganda[2]]

    return result


if env.AREA == "antisem":
    data = prepare_antisem_scores()
    plot_all_lines(data, "HFLP", "result_antisem")
else:
    data = prepare_anticom_scores()
    plot_all_lines(data, "HFLP", "result_anticom")

