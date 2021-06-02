import os
import argparse

"""Directory variables for simpler & faster central changes"""

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
ENVIRONMENT_FILE = os.path.join(ROOT_DIR, "environment.txt")

# Change area between antisem & anticom
AREA = str(open(ENVIRONMENT_FILE, "r").read())

MODULES_DIR = os.path.join(ROOT_DIR, "modules")
MODELS_DIR = os.path.join(ROOT_DIR, "models")
DATA_DIR = os.path.join(ROOT_DIR, "data")

VECTOR_ANTISEM_DIR = os.path.join(MODELS_DIR, "vectors", "antisemitism")
VECTOR_ANTICOM_DIR = os.path.join(MODELS_DIR, "vectors", "anticommunism")
VOCAB_ANTISEM_DIR = os.path.join(MODELS_DIR, "vocab", "antisemitism")
VOCAB_ANTICOM_DIR = os.path.join(MODELS_DIR, "vocab", "anticommunism")

SPECIFICATION_FILES = os.path.join(DATA_DIR, "specifications")
SPEC_ANTISEM_FILES = os.path.join(SPECIFICATION_FILES, "antisemitism")
SPEC_ANTICOM_FILES = os.path.join(SPECIFICATION_FILES, "anticommunism")

HFLP_DIR = os.path.join(ROOT_DIR, "hflp")
HFLP_SCORES_ANTISEM_DIR = os.path.join(HFLP_DIR, "hflp_scores", "antisem")
HFLP_SCORES_ANTICOM_DIR = os.path.join(HFLP_DIR, "hflp_scores", "anticom")
PPMI_ANTISEM_DIR = os.path.join(HFLP_DIR, "ppmi", "antisem")
PPMI_ANTICOM_DIR = os.path.join(HFLP_DIR, "ppmi", "anticom")

ECT_OUTPUTS = os.path.join(ROOT_DIR, "evaluation", "ect")
WEAT_OUTPUTS = os.path.join(ROOT_DIR, "evaluation", "weat")
BAT_OUTPUTS = os.path.join(ROOT_DIR, "evaluation", "bat")
KMEANS_OUTPUTS = os.path.join(ROOT_DIR, "evaluation", "kmeans")
SIMLEX_OUTPUTS = os.path.join(ROOT_DIR, "evaluation", "simlex")


def set_area(area_value):
    with open(ENVIRONMENT_FILE, "w") as f:
        f.write(area_value)
        f.close()
    AREA = area_value
    print("_________________________________")
    print("AREA has been set to: " + AREA)
    print("_________________________________")


def main():
    parser = argparse.ArgumentParser(description="Change area")
    parser.add_argument("--area", type=str, help="antisem | anticom", required=True)

    if parser.parse_args().area == "antisem":
        set_area(parser.parse_args().area)
    if parser.parse_args().area == "anticom":
        set_area(parser.parse_args().area)



if __name__ == "__main__":
    main()


