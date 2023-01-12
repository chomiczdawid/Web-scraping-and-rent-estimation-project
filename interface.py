#!pip install flask
from flask import Flask, render_template, request

# Załadowanie listy z parametrami modelu
lparams = []
with open('params.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        lparams.append(x)
lparams = [float(i) for i in lparams]

# Wygenerowanie strony głównej html za pomocą Flaska
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form/", methods=['POST'])
def form():
    area_size = request.form.get("input_area")
    s_rooms	= request.form.get("input_rooms")
    s_floor	= request.form.get("input_floor")
    s_year = request.form.get("input_year")
    s_landlord_type = request.form.get("input_landlord")
    s_local_type = request.form.get("input_local_type")
    furnished = request.form.get("input_furnished")
    s_levels = request.form.get("input_levels")
    
    if s_rooms == '1':
        l_rooms = [1,0,0,0]
    elif s_rooms == '2':
        l_rooms = [0,1,0,0]
    elif s_rooms == '3':
        l_rooms = [0,0,1,0]
    elif s_rooms == '4+':
        l_rooms = [0,0,0,1]

    if s_floor == '1':
        l_floor = [1,0,0,0,0,0,0]
    elif s_floor == '2':
        l_floor = [0,1,0,0,0,0,0]
    elif s_floor == '3':
        l_floor = [0,0,1,0,0,0,0]
    elif s_floor == '4':
        l_floor = [0,0,0,1,0,0,0]
    elif s_floor == '5-10':
        l_floor = [0,0,0,0,1,0,0]
    elif s_floor == '<=0':
        l_floor = [0,0,0,0,0,1,0]
    elif s_floor == '>10':
        l_floor = [0,0,0,0,0,0,1]

    if s_year == '1990-2005':
        l_year = [1,0,0,0,0]
    elif s_year == '2005-2015':
        l_year = [0,1,0,0,0]
    elif s_year == '2015-2020':
        l_year = [0,0,1,0,0]
    elif s_year == '<1990':
        l_year = [0,0,0,1,0]
    elif s_year == '>=2020':
        l_year = [0,0,0,0,1]

    if s_landlord_type == 'osoba_prywatna':
        l_landlord_type = [0,1]
    elif s_landlord_type == 'firma':
        l_landlord_type = [1,0]

    if s_local_type == 'inne':
        l_local_type = [1,0,0]
    elif s_local_type == 'komercyjne':
        l_local_type = [0,1,0]
    elif s_local_type == 'mieszkalne':
        l_local_type = [0,0,1]

    if furnished == 'nie':
        l_furnished = [1,0]
    elif furnished == 'tak':
        l_furnished = [0,1]

    if s_levels == '3':
        l_levels = [1,0,0,0,0]
    elif s_levels == '4':
        l_levels = [0,1,0,0,0]
    elif s_levels == '5':
        l_levels = [0,0,1,0,0]
    elif s_levels == '<=2':
        l_levels = [0,0,0,1,0]
    elif s_levels == '>6':
        l_levels = [0,0,0,0,1]
    
    multipliers = [1] + [area_size] + l_rooms + l_floor + l_landlord_type + l_local_type + l_furnished + l_levels
    multiplied = [i1 * int(i2) for i1, i2 in zip(lparams, multipliers)]
    result = round(sum(multiplied), 2)
    return render_template("form.html", result=result)