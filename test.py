import os

# app_string = "it-trm,it-co"

app_string = os.getenv("MTMS")
app_list = app_string.split(',')

print(app_list)

no_of_apps = len(app_list)

print(no_of_apps)