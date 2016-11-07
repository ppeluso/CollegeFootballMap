
# coding: utf-8

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import sys
sys.path.append('/Users/peterpeluso/desktop/CollegeFootballMap/CFB')


app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/fullmap')
def fullmap():
    from update import data_array 
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:75%;"
            "width:100%;"
            "top:75%;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers= data_array,
        # maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template('example.html', fullmap=fullmap)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)