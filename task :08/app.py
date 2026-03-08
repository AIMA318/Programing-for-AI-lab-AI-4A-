from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)

# Create database tables
with app.app_context():
    db.create_all()

# Define models directly in app.py to avoid import issues
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    prep_time = db.Column(db.String(50))
    cook_time = db.Column(db.String(50))
    servings = db.Column(db.Integer, default=1)
    difficulty = db.Column(db.String(20), default='Easy')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with ingredients
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'instructions': self.instructions,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'servings': self.servings,
            'difficulty': self.difficulty,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients]
        }

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(50))
    unit = db.Column(db.String(50))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'recipe_id': self.recipe_id
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = Recipe(
        title=data['title'],
        description=data['description'],
        instructions=data['instructions'],
        prep_time=data.get('prep_time', ''),
        cook_time=data.get('cook_time', ''),
        servings=data.get('servings', 1),
        difficulty=data.get('difficulty', 'Easy')
    )
    
    # Add ingredients
    for ingredient_data in data.get('ingredients', []):
        ingredient = Ingredient(
            name=ingredient_data['name'],
            quantity=ingredient_data.get('quantity', ''),
            unit=ingredient_data.get('unit', '')
        )
        recipe.ingredients.append(ingredient)
    
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.to_dict()), 201

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict())

@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.get_json()
    
    recipe.title = data.get('title', recipe.title)
    recipe.description = data.get('description', recipe.description)
    recipe.instructions = data.get('instructions', recipe.instructions)
    recipe.prep_time = data.get('prep_time', recipe.prep_time)
    recipe.cook_time = data.get('cook_time', recipe.cook_time)
    recipe.servings = data.get('servings', recipe.servings)
    recipe.difficulty = data.get('difficulty', recipe.difficulty)
    
    # Update ingredients
    if 'ingredients' in data:
        # Remove existing ingredients
        recipe.ingredients.clear()
        
        # Add new ingredients
        for ingredient_data in data['ingredients']:
            ingredient = Ingredient(
                name=ingredient_data['name'],
                quantity=ingredient_data.get('quantity', ''),
                unit=ingredient_data.get('unit', '')
            )
            recipe.ingredients.append(ingredient)
    
    db.session.commit()
    return jsonify(recipe.to_dict())

@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return '', 204

@app.route('/api/recipes/search', methods=['GET'])
def search_recipes():
    query = request.args.get('q', '').lower()
    difficulty = request.args.get('difficulty', '')
    
    recipes_query = Recipe.query
    
    if query:
        recipes_query = recipes_query.filter(
            (Recipe.title.ilike(f'%{query}%')) |
            (Recipe.description.ilike(f'%{query}%')) |
            (Recipe.instructions.ilike(f'%{query}%'))
        )
    
    if difficulty:
        recipes_query = recipes_query.filter(Recipe.difficulty == difficulty)
    
    recipes = recipes_query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

if __name__ == '__main__':
    app.run(debug=True)
