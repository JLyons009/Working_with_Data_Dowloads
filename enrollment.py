import pandas as pd

contents = pd.read_csv('data/CRDC2013_14.csv')
contents["total_enrollment"] = contents["TOT_ENR_M"] + contents["TOT_ENR_F"]

cols = ["SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M", "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F", "SCH_ENR_TR_M", "SCH_ENR_TR_F"]

race_gen = {}

for col in cols:
    race_gen[col] = contents[col].sum()

all_enrollment = contents["total_enrollment"].sum()

race_gen_percent = {}

for key, value in race_gen.items():
    race_gen_percent[key] = value/all_enrollment

if __name__ == "__main__":
    for key, value in race_gen_percent.items():
        print(str(key) + ": " + str(value))