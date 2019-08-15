import os
import sys
from datetime import datetime

import altair as alt
import numpy as np
import pandas as pd


def get_values():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = file.read()

    data = [[float(y) for y in x.split()] for x in data.split('\n') if x]

    # print([list(t) for t in zip(*data)])
    packageloss, reponsetime, timestamp = zip(*data)
    return {'packageloss': np.array(packageloss),
            'responsetime': np.array(reponsetime),
            'timestamp': np.array([datetime.fromtimestamp(x) for x in timestamp])}


if __name__ == '__main__':
    df = pd.DataFrame(data=get_values())
    first_date = str(df.get('timestamp')[0])
    date_day = first_date.split()[0]
    start_hour = first_date.split()[1]
    end_hour = str(df.get('timestamp')[df.index[-1]]).split()[1]
    title = "Beehive Network ({})".format(date_day)
    chart_rt = alt.Chart(df, width=1000, height=500).mark_line().encode(
        x='timestamp:T',
        y='responsetime:Q',
        tooltip=['timestamp:T']
    ).properties(
        title="{} - {} - {} to {}".format(title, 'ResponseTime', start_hour, end_hour)
    ).configure_title(
        fontSize=20,
        font='Courier',
        anchor='start',
        color='gray'
    ).interactive()

    chart_pl = alt.Chart(df, width=1000, height=500).mark_line().encode(
        x='timestamp:T',
        y='packageloss:Q',
        tooltip=['timestamp:T']
    ).properties(
        title="{} - {} - {} to {}".format(title, 'PackageLoss', start_hour, end_hour),
    ).configure_title(
        fontSize=20,
        font='Courier',
        anchor='start',
        color='gray'
    ).interactive()

    basename = os.path.splitext(sys.argv[1])[0]
    chart_pl.save("{}_packageloss.html".format(basename))
    chart_rt.save("{}_responsetime.html".format(basename))
