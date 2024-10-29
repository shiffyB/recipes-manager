from flask import Flask, request, jsonify

app = Flask(__name__)
recipes = {}  # Temporary storage

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.json
    recipe_id = len(recipes) + 1
    recipes[recipe_id] = data
    return jsonify({'id': recipe_id, 'status': 'Recipe added'})

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
