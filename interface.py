# !pip install flask
# importing flask library and necessary modules
from flask import Flask, render_template, request

# Loading model parameters from params.txt file generated in modeling.ipynb
lparams = []
with open('params.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        lparams.append(x)
lparams = [float(i) for i in lparams]

# Generating flask process
app = Flask(__name__)

# Defining main page route rendering the page on hosting server
@app.route("/")
def index():
    return render_template("index.html")

# Defining form subpage
@app.route("/form/", methods=['POST'])
def form():
    # Assigning parameters from inputs
    area_size = request.form.get("input_area")
    s_rooms	= request.form.get("input_rooms")
    s_floor	= request.form.get("input_floor")
    s_year = request.form.get("input_year")
    s_landlord_type = request.form.get("input_landlord")
    s_local_type = request.form.get("input_local_type")
    furnished = request.form.get("input_furnished")
    s_levels = request.form.get("input_levels")
    
    ## Converting input variables to binary lists corresponding with model parameters
    # Rooms variable
    if s_rooms == '1':
        l_rooms = [1,0,0,0]
    elif s_rooms == '2':
        l_rooms = [0,1,0,0]
    elif s_rooms == '3':
        l_rooms = [0,0,1,0]
    elif s_rooms == '4+':
        l_rooms = [0,0,0,1]
    # Floor variable
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
    # Year variable
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
    # Landlord type variable
    if s_landlord_type == 'osoba_prywatna':
        l_landlord_type = [0,1]
    elif s_landlord_type == 'firma':
        l_landlord_type = [1,0]
    # Local type variable
    if s_local_type == 'inne':
        l_local_type = [1,0,0]
    elif s_local_type == 'komercyjne':
        l_local_type = [0,1,0]
    elif s_local_type == 'mieszkalne':
        l_local_type = [0,0,1]
    # Furnished variable
    if furnished == 'nie':
        l_furnished = [1,0]
    elif furnished == 'tak':
        l_furnished = [0,1]
    # Levels variable
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
    # Combining generated binary lists in order correpsonding with model parameters order in params.txt
    multipliers = [1] + [area_size] + l_rooms + l_floor + l_landlord_type + l_local_type + l_furnished + l_levels
    # Multiplying converted input values by model parameters values from loaded params.txt file
    multiplied = [i1 * int(i2) for i1, i2 in zip(lparams, multipliers)]
    # Adding up the multiplied values to get the final result, rounding output to two decimal places
    result = round(sum(multiplied), 2)
    # Rendering result page from form.html and passing result variable to show on the web page
    return render_template("form.html", result=result)
