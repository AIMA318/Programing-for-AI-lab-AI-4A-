from datetime import datetime

# Import will be done in app.py to avoid circular imports
# This file will be imported after db is initialized

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
    
    def __repr__(self):
        return f'<Recipe {self.title}>'

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
    
    def __repr__(self):
        return f'<Ingredient {self.name}>'
