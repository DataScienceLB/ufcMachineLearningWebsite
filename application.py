from flask import Flask
from flask import render_template, request, redirect
from machine_learning import predict, loaded_model
# ----
# from plotly.offline import plot
# from plotly.graph_objs import Scatter
from flask import Markup
import plotly.graph_objects as go
# import plotly
# import json
# ----
import pandas as pd

application = app = Flask(__name__)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        try:
            req = request.form

            fighter1 = str(req["fighter1"]).lower()
            fighter2 = str(req["fighter2"]).lower()
            red = fighter1
            blue = fighter2
            # -----------------
            stats_df = pd.read_csv("df_fighters_clean_final.csv")

            rstats_query = stats_df.query(f'Name == "{red}"')
            rstrikes_landed_per_minute = rstats_query['SLpM:'].values[0]
            rstrike_accuracy = rstats_query['Str. Acc.:'].values[0]
            rstrikes_absorbed_per_minute = rstats_query['SApM:'].values[0]
            rstrike_defense = rstats_query['Str. Def:'].values[0]
            ravg_takedownds_p_15_mins = rstats_query['TD Avg.:'].values[0]
            rtakedown_accuracy = rstats_query['TD Acc.:'].values[0]
            rtakedown_defense = rstats_query['TD Def.:'].values[0]
            rsubmision_avg = rstats_query['Sub. Avg.:'].values[0]

            bstats_query = stats_df.query(f'Name == "{blue}"')
            bstrikes_landed_per_minute = bstats_query['SLpM:'].values[0]
            bstrike_accuracy = bstats_query['Str. Acc.:'].values[0]
            bstrikes_absorbed_per_minute = bstats_query['SApM:'].values[0]
            bstrike_defense = bstats_query['Str. Def:'].values[0]
            bavg_takedownds_p_15_mins = bstats_query['TD Avg.:'].values[0]
            btakedown_accuracy = bstats_query['TD Acc.:'].values[0]
            btakedown_defense = bstats_query['TD Def.:'].values[0]
            bsubmision_avg = bstats_query['Sub. Avg.:'].values[0]

            prediction = predict(loaded_model, red, blue)
            prediction2 = predict(loaded_model, blue, red)

            fighter1_avg = (prediction + (1 - prediction2)) / 2
            fighter2_avg = (prediction2 + (1 - prediction)) / 2

            prediction_f1 = int(round(fighter1_avg[0][0] * 100))
            prediction_f2 = int(round(fighter2_avg[0][0] * 100))

            tale_df = pd.read_csv("final_tale.csv")
            df_q_red = tale_df.query(f'Name == "{fighter1}"')

            r_weight_class = df_q_red["Weight Class"].values[0]
            r_weight = df_q_red["Weight:"].values[0]
            r_height = df_q_red["Height:"].values[0]
            r_reach = df_q_red["Reach:"].values[0]
            r_age = df_q_red["Age"].values[0]
            r_wins = df_q_red["Wins"].values[0]
            r_losses = df_q_red["Losses"].values[0]
            r_draws = df_q_red["Draws"].values[0]

            df_q_blue = tale_df.query(f'Name == "{fighter2}"')

            b_weight_class = df_q_blue["Weight Class"].values[0]
            b_weight = df_q_blue["Weight:"].values[0]
            b_height = df_q_blue["Height:"].values[0]
            b_reach = df_q_blue["Reach:"].values[0]
            b_age = df_q_blue["Age"].values[0]
            b_wins = df_q_blue["Wins"].values[0]
            b_losses = df_q_blue["Losses"].values[0]
            b_draws = df_q_blue["Draws"].values[0]

            return render_template("main_page.html",
                                   rstrikes_landed_per_minute=rstrikes_landed_per_minute, rstrike_accuracy=rstrike_accuracy,
                                   rstrikes_absorbed_per_minute=rstrikes_absorbed_per_minute,
                                   rstrike_defense=rstrike_defense, ravg_takedownds_p_15_mins=ravg_takedownds_p_15_mins ,
                                   rtakedown_accuracy=rtakedown_accuracy, rtakedown_defense=rtakedown_defense,
                                   rsubmision_avg=rsubmision_avg,

                                   bstrikes_landed_per_minute=bstrikes_landed_per_minute,
                                   bstrike_accuracy=bstrike_accuracy,
                                   bstrikes_absorbed_per_minute=bstrikes_absorbed_per_minute,
                                   bstrike_defense=bstrike_defense, bavg_takedownds_p_15_mins=bavg_takedownds_p_15_mins,
                                   btakedown_accuracy=btakedown_accuracy, btakedown_defense=btakedown_defense,
                                   bsubmision_avg=bsubmision_avg,

                                   red=prediction_f1, blue=prediction_f2,
                                   red_name=fighter1, blue_name=fighter2,

                                   r_weight_class=r_weight_class, r_age=r_age, r_height=r_height,
                                   r_weight=r_weight, r_reach=r_reach, r_wins=r_wins, r_losses=r_losses, r_draws=r_draws,

                                   b_weight_class=b_weight_class, b_age=b_age, b_height=b_height,
                                   b_weight=b_weight, b_reach=b_reach, b_wins=b_wins, b_losses=b_losses, b_draws=b_draws)
        except (KeyError, IndexError) as e:
            not_found = True
            return render_template("main_page.html", not_found=not_found)
    return render_template("main_page.html")


if __name__ == '__main__':
    application.run()
