# Recipe Book - Cooking App

A dynamic Flask-based web application for managing and sharing recipes. Features a modern, responsive frontend with full CRUD operations for recipes and ingredients.

## Features

- **Recipe Management**: Create, read, update, and delete recipes
- **Ingredient Tracking**: Add and manage ingredients for each recipe
- **Search & Filter**: Search recipes by title, description, or instructions; filter by difficulty level
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS
- **Dynamic Frontend**: Interactive UI with modal dialogs and real-time updates
- **Database Storage**: SQLite database for persistent data storage

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS
- **Icons**: Font Awesome
- **API**: RESTful API endpoints

## Installation

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database with sample data**:
   ```bash
   python add_sample_data.py
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## API Endpoints

### Recipes
- `GET /api/recipes` - Get all recipes
- `GET /api/recipes/<id>` - Get a specific recipe
- `POST /api/recipes` - Create a new recipe
- `PUT /api/recipes/<id>` - Update a recipe
- `DELETE /api/recipes/<id>` - Delete a recipe
- `GET /api/recipes/search` - Search recipes (with query parameters `q` and `difficulty`)

### Recipe Data Structure
```json
{
  "title": "Recipe Title",
  "description": "Recipe description",
  "instructions": "Step-by-step instructions",
  "prep_time": "15 mins",
  "cook_time": "30 mins",
  "servings": 4,
  "difficulty": "Easy|Medium|Hard",
  "ingredients": [
    {
      "name": "Ingredient name",
      "quantity": "1",
      "unit": "cup"
    }
  ]
}
```

## Project Structure

```
task 8/
├── app.py                 # Main Flask application
├── models.py              # Database models (Recipe, Ingredient)
├── requirements.txt       # Python dependencies
├── add_sample_data.py     # Script to populate database with sample recipes
├── templates/
│   └── index.html        # Main frontend template
├── recipes.db            # SQLite database (created automatically)
└── README.md            # This file
```

## Usage

1. **View Recipes**: Browse all recipe cards on the main page
2. **Search**: Use the search bar to find recipes by keywords
3. **Filter**: Filter recipes by difficulty level (Easy, Medium, Hard)
4. **View Details**: Click on any recipe card to see full details including ingredients and instructions
5. **Add Recipe**: Click "Add Recipe" button to create a new recipe
6. **Edit Recipe**: Click the edit icon on any recipe card to modify it
7. **Delete Recipe**: Click the trash icon to remove a recipe

## Sample Recipes

The application comes pre-loaded with 5 sample recipes:
- Classic Spaghetti Carbonara
- Chicken Stir Fry
- Chocolate Chip Cookies
- Greek Salad
- Beef Tacos

## Database Schema

### Recipe Model
- `id`: Primary key
- `title`: Recipe title (required)
- `description`: Recipe description (required)
- `instructions`: Cooking instructions (required)
- `prep_time`: Preparation time
- `cook_time`: Cooking time
- `servings`: Number of servings
- `difficulty`: Difficulty level (Easy, Medium, Hard)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Ingredient Model
- `id`: Primary key
- `name`: Ingredient name (required)
- `quantity`: Quantity amount
- `unit`: Unit of measurement
- `recipe_id`: Foreign key to Recipe

## Customization

- **Styling**: Modify the CSS in `templates/index.html` or adjust Tailwind classes
- **Database**: The app uses SQLite by default but can be configured for other databases
- **Features**: Add new API endpoints in `app.py` and corresponding frontend functionality

## Troubleshooting

1. **Database not found**: Run `python add_sample_data.py` to create and populate the database
2. **Port already in use**: The app runs on port 5000 by default. You can change this in `app.py`
3. **Dependencies error**: Ensure all requirements are installed with `pip install -r requirements.txt`

## License

This project is open source and available under the MIT License.
