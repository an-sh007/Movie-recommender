# 🎬 Movie Recommendation App

Welcome to the **Movie Recommendation App**! This is a simple web application built using **Django** and **MongoDB** that provides movie recommendations based on your preferences.

## 🚀 Features
- Display a list of movies with their genres and ratings.
- Provide personalized movie recommendations.
- Simple and clean user interface.

## 🛠️ Tech Stack
- **Backend:** Django
- **Database:** MongoDB using Djongo
- **Frontend:** HTML, CSS

## 📦 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-app.git
    ```

2. Navigate to the project folder:
    ```bash
    cd movie-recommendation-app
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    env\Scripts\activate  # For Windows
    source env/bin/activate  # For macOS/Linux
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure your MongoDB connection in `settings.py`.

6. Run migrations and start the server:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

7. Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 🧑‍💻 Contributing
Feel free to submit issues or pull requests! Contributions are welcome.

## 📜 License
This project is licensed under the **MIT License**.

---

🎉 Enjoy using the Movie Recommendation App!