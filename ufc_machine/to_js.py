import pandas as pd
import plotly.graph_objects as go
import json

df = pd.read_csv("df_fighters_clean_final.csv")
df = df.sort_values(by='Name')
print(df[df["Name"].str.startswith("g")])
# stats_query = df.query(f'Name == "{"jorge masvidal"}"')
# name = stats_query['Name'].values[0]
# strikes_landed_per_minute = stats_query['SLpM:'].values[0]
# strike_accuracy = stats_query['Str. Acc.:'].values[0]
# strikes_absorbed_per_minute = stats_query['SApM:'].values[0]
# strike_defense = stats_query['Str. Def:'].values[0]
# avg_takedownds_p_15_mins = stats_query['TD Avg.:'].values[0]
# takedown_accuracy = stats_query['TD Acc.:'].values[0]
# takedown_defense = stats_query['TD Def.:'].values[0]
# submision_avg = stats_query['Sub. Avg.:'].values[0]
#
# stats = [strikes_landed_per_minute, strike_accuracy, strikes_absorbed_per_minute, strike_defense,
#          avg_takedownds_p_15_mins, takedown_accuracy, takedown_defense, submision_avg]
# y = ["Submission_Avg_p_15_mins", "Strike_Accuracy", "Strikes_Absorbed", "Strike_Defense", "Avg_Takedowns_per_15min",
#      "Takedown_Acc", "Takedown_Defense", "Strikes_Landed_per_minute" ]
# x = [submision_avg, strike_accuracy, strikes_absorbed_per_minute, strike_defense, avg_takedownds_p_15_mins,
#      takedown_accuracy, takedown_defense,  strikes_landed_per_minute ]
# fig = go.Figure(data=[go.Bar(x=x, y=y,)])
# fig.update_traces(marker_color='red', marker_line_color='black',marker_line_width=4, opacity=.6, orientation='h')
# fig.show()

# trace = go.Bar(
#         x = x,
#         y = y
#     )
# data = [trace]

# df_json = df.Name.to_json(orient='records')
# json.dumps(df.values.tolist())
# print(json.dumps(df.Name.values.tolist()))
# print(df_json)

# df[['SLpM:', 'Str. Acc.:', 'SApM:', 'Str. Def:', 'TD Avg.:', 'TD Acc.:', 'TD Def.:', 'Sub. Avg.:']]
