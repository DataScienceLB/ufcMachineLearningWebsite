from machine_learning import predict, loaded_model
import pandas as pd

df_fighters = pd.read_csv("df_fighters_clean_final.csv")
df_fighters.set_index("Name", inplace=True)
df_matches = pd.read_csv("training_model_clean.csv")

red = "jose masvidal"
blue = "nate diaz"

prediction = predict(loaded_model, red, blue)
print(prediction)