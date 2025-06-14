# 📝 Flask Notes Web App

A simple and secure note-taking web application built with **Flask**, allowing users to **register, log in**, and **create or delete notes**. Designed with scalability and clean code structure in mind.

---

## 🚀 Features

- 🔐 User Authentication (Sign Up & Log In)  
- 🗒️ Create and Delete Notes  
- 📁 SQLite Database Integration  
- 🖼️ Bootstrap for Styling  
- 🌐 RESTful API with JavaScript `fetch` for deleting notes  
- 🔒 Secret Key stored securely via environment variables  

---

## 📁 Project Structure

```
├── instance/  
│   └── database.db             # SQLite database  
├── website/  
│   ├── static/                 # Static files (JS, CSS)  
│   │   └── index.js  
│   ├── templates/              # HTML templates  
│   │   ├── base.html  
│   │   ├── home.html  
│   │   ├── login.html  
│   │   └── sign_up.html  
│   ├── __init__.py             # App factory  
│   ├── auth.py                 # Authentication routes  
│   ├── views.py                # Main views  
│   └── models.py               # SQLAlchemy models  
├── .env                        # Secret environment variables (NOT pushed)  
├── .gitignore  
├── main.py                     # App entry point  
└── README.md
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-notes-app.git
cd flask-notes-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Activate the virtual environment:
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File for Secrets

```bash
touch .env
```

Add this to your `.env` file:

```ini
SECRET_KEY=your-secret-key
```

> ✅ Make sure you never share this file or upload it to GitHub.

---

## ▶️ Run the App Locally

```bash
python main.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Deployment on Render

### Steps:

1. Push your project to GitHub.
2. Go to [https://render.com](https://render.com) and create a **Web Service**.
3. Connect your GitHub repository.
4. Set the following:
   - **Build Command**: (leave blank or use `pip install -r requirements.txt`)
   - **Start Command**: `gunicorn main:app`
   - **Environment Variables**:
     ```env
     SECRET_KEY=your-secret-key
     ```

5. Click **Deploy**. Your app is now online!

---

## 🛠️ Tech Stack

- Python 3.x  
- Flask  
- Jinja2 Templates  
- SQLite + SQLAlchemy  
- Bootstrap 4/5  
- JavaScript (Fetch API)

---

## 🙋‍♂️ Author

**Joshua Darrah**  
📧 Email: darrahjoshua551@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/joshuadarrah)

---

## 📜 License

MIT License – Use, modify, and share freely.

---

## 📌 To-Do

- [ ] Add edit note functionality  
- [ ] Add user profile page  
- [ ] Add dark mode toggle  
