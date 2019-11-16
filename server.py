from flask import (
    Flask,
    render_template
)
import connexion

# The columns from the dataset will be the the columsn in the database

# ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description', 'Earthy', 'Sweet', 'Citrus',
#        'Flowery', 'Violet', 'Diesel', 'Spicy/Herbal', 'Sage', 'Woody', 'Apricot', 'Grapefruit',
#        'Orange', 'Pungent', 'Grape', 'Pine', 'Skunk', 'None', 'Berry', 'Pepper', 'Menthol', 'Blue',
#        'Cheese', 'Chemical', 'Mango', 'Lemon', 'Peach', 'Vanilla', 'Nutty', 'Chestnut', 'Tea',
#        'Tobacco', 'Tropical', 'Strawberry', 'Blueberry', 'Mint', 'Apple', 'Honey', 'Lavender',
#        'Lime', 'Coffee', 'Ammonia', 'Minty', 'Tree', 'Fruit', 'Butter', 'Pineapple', 'Tar', 'Rose',
#        'Plum', 'Pear', 'Creative', 'Energetic', 'Tingly', 'Euphoric', 'Relaxed', 'Aroused',
#        'Happy', 'Uplifted', 'Hungry', 'Talkative', 'Giggly', 'Focused', 'Sleepy', 'Dry', 'Mouth']




app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)