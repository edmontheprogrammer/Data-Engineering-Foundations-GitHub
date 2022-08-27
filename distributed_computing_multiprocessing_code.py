# multiprocessing

from multiprocessing import Pool


def athlete_avg_age(grouped_data):
    year, group = grouped_data
    return pd.DataFrame({"Age": group["Age"].mean()}, index=[year])


with Pool(4) as p:
    average_age = p.map(athlete_avg_age, df.groupby("Year"))
