from app import app, db, Recipe, Ingredient

def add_sample_recipes():
    with app.app_context():
        # Clear existing data
        Recipe.query.delete()
        db.session.commit()
        
        # Sample recipes
        sample_recipes = [
            {
                'title': 'Classic Spaghetti Carbonara',
                'description': 'A traditional Italian pasta dish with eggs, cheese, and pancetta',
                'instructions': '''1. Cook spaghetti according to package directions.
2. While pasta cooks, fry pancetta until crispy.
3. In a bowl, whisk eggs with grated Parmesan cheese.
4. Drain pasta, reserving 1 cup pasta water.
5. Add hot pasta to pancetta, remove from heat.
6. Quickly stir in egg mixture, adding pasta water as needed.
7. Season with black pepper and serve immediately.''',
                'prep_time': '10 mins',
                'cook_time': '20 mins',
                'servings': 4,
                'difficulty': 'Medium',
                'ingredients': [
                    {'name': 'Spaghetti', 'quantity': '400', 'unit': 'grams'},
                    {'name': 'Pancetta', 'quantity': '200', 'unit': 'grams'},
                    {'name': 'Eggs', 'quantity': '4', 'unit': 'large'},
                    {'name': 'Parmesan cheese', 'quantity': '100', 'unit': 'grams'},
                    {'name': 'Black pepper', 'quantity': '2', 'unit': 'teaspoons'}
                ]
            },
            {
                'title': 'Chicken Stir Fry',
                'description': 'Quick and healthy Asian-inspired stir fry with vegetables',
                'instructions': '''1. Cut chicken into bite-sized pieces.
2. Heat oil in a large wok or skillet over high heat.
3. Cook chicken until golden, about 5-6 minutes.
4. Add vegetables and stir fry for 3-4 minutes.
5. Mix soy sauce, garlic, and honey in a small bowl.
6. Pour sauce over chicken and vegetables.
7. Cook for 2 more minutes until sauce thickens.
8. Serve over rice or noodles.''',
                'prep_time': '15 mins',
                'cook_time': '15 mins',
                'servings': 4,
                'difficulty': 'Easy',
                'ingredients': [
                    {'name': 'Chicken breast', 'quantity': '500', 'unit': 'grams'},
                    {'name': 'Mixed vegetables', 'quantity': '300', 'unit': 'grams'},
                    {'name': 'Soy sauce', 'quantity': '3', 'unit': 'tablespoons'},
                    {'name': 'Garlic', 'quantity': '3', 'unit': 'cloves'},
                    {'name': 'Honey', 'quantity': '1', 'unit': 'tablespoon'},
                    {'name': 'Vegetable oil', 'quantity': '2', 'unit': 'tablespoons'}
                ]
            },
            {
                'title': 'Chocolate Chip Cookies',
                'description': 'Classic homemade chocolate chip cookies that are soft and chewy',
                'instructions': '''1. Preheat oven to 375°F (190°C).
2. Cream together butter and sugars until fluffy.
3. Beat in eggs and vanilla extract.
4. Mix in flour, baking soda, and salt.
5. Fold in chocolate chips.
6. Drop rounded tablespoons onto baking sheets.
7. Bake for 9-11 minutes until golden brown.
8. Cool on baking sheet for 2 minutes before transferring.''',
                'prep_time': '20 mins',
                'cook_time': '12 mins',
                'servings': 24,
                'difficulty': 'Easy',
                'ingredients': [
                    {'name': 'Butter', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Brown sugar', 'quantity': '3/4', 'unit': 'cup'},
                    {'name': 'White sugar', 'quantity': '1/4', 'unit': 'cup'},
                    {'name': 'Eggs', 'quantity': '2', 'unit': 'large'},
                    {'name': 'Vanilla extract', 'quantity': '2', 'unit': 'teaspoons'},
                    {'name': 'All-purpose flour', 'quantity': '2.25', 'unit': 'cups'},
                    {'name': 'Baking soda', 'quantity': '1', 'unit': 'teaspoon'},
                    {'name': 'Salt', 'quantity': '1', 'unit': 'teaspoon'},
                    {'name': 'Chocolate chips', 'quantity': '2', 'unit': 'cups'}
                ]
            },
            {
                'title': 'Greek Salad',
                'description': 'Fresh and healthy Mediterranean salad with feta cheese',
                'instructions': '''1. Cut cucumbers into bite-sized pieces.
2. Halve cherry tomatoes.
3. Thinly slice red onion.
4. Crumble feta cheese.
5. Combine all vegetables in a large bowl.
6. Drizzle with olive oil and lemon juice.
7. Season with oregano, salt, and pepper.
8. Toss gently and serve immediately.''',
                'prep_time': '15 mins',
                'cook_time': '0 mins',
                'servings': 6,
                'difficulty': 'Easy',
                'ingredients': [
                    {'name': 'Cucumber', 'quantity': '2', 'unit': 'large'},
                    {'name': 'Cherry tomatoes', 'quantity': '400', 'unit': 'grams'},
                    {'name': 'Red onion', 'quantity': '1', 'unit': 'medium'},
                    {'name': 'Feta cheese', 'quantity': '200', 'unit': 'grams'},
                    {'name': 'Kalamata olives', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Olive oil', 'quantity': '3', 'unit': 'tablespoons'},
                    {'name': 'Lemon juice', 'quantity': '2', 'unit': 'tablespoons'},
                    {'name': 'Dried oregano', 'quantity': '1', 'unit': 'teaspoon'}
                ]
            },
            {
                'title': 'Beef Tacos',
                'description': 'Mexican-style tacos with seasoned ground beef and fresh toppings',
                'instructions': '''1. Brown ground beef in a large skillet.
2. Add taco seasoning and water, simmer until thickened.
3. Warm taco shells according to package directions.
4. Fill shells with beef mixture.
5. Top with lettuce, tomatoes, and cheese.
6. Add sour cream and salsa as desired.
7. Serve with lime wedges.''',
                'prep_time': '10 mins',
                'cook_time': '15 mins',
                'servings': 6,
                'difficulty': 'Easy',
                'ingredients': [
                    {'name': 'Ground beef', 'quantity': '1', 'unit': 'pound'},
                    {'name': 'Taco seasoning', 'quantity': '1', 'unit': 'packet'},
                    {'name': 'Taco shells', 'quantity': '12', 'unit': 'hard'},
                    {'name': 'Lettuce', 'quantity': '1', 'unit': 'head'},
                    {'name': 'Tomatoes', 'quantity': '2', 'unit': 'medium'},
                    {'name': 'Cheddar cheese', 'quantity': '200', 'unit': 'grams'},
                    {'name': 'Sour cream', 'quantity': '1', 'unit': 'cup'},
                    {'name': 'Salsa', 'quantity': '1', 'unit': 'jar'}
                ]
            }
        ]
        
        # Add recipes to database
        for recipe_data in sample_recipes:
            recipe = Recipe(
                title=recipe_data['title'],
                description=recipe_data['description'],
                instructions=recipe_data['instructions'],
                prep_time=recipe_data['prep_time'],
                cook_time=recipe_data['cook_time'],
                servings=recipe_data['servings'],
                difficulty=recipe_data['difficulty']
            )
            
            for ingredient_data in recipe_data['ingredients']:
                ingredient = Ingredient(
                    name=ingredient_data['name'],
                    quantity=ingredient_data['quantity'],
                    unit=ingredient_data['unit']
                )
                recipe.ingredients.append(ingredient)
            
            db.session.add(recipe)
        
        db.session.commit()
        print(f"Added {len(sample_recipes)} sample recipes to the database!")

if __name__ == '__main__':
    add_sample_recipes()
