# 🌍 Nomad Nest

**Global Cost of Living Calculator App (In Development)**  
**Author:** [Brice A. Nelson](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/) • [devbybrice.com](https://www.devbybrice.com)

---

## 🧭 Overview

**Nomad Nest** is a full-stack **Flask application** designed to calculate and compare the **cost of living (COL)** across global cities.  
The app integrates real-world datasets and APIs to provide structured cost indices, rent trends, and purchasing power insights for digital nomads, remote workers, and travelers planning relocations.

This project is under **active development** and will serve as both a **backend architecture demo** and a **data-driven web application**.

---

## ⚙️ Current Features (MVP Stage)

- 🌐 Flask backend with modular blueprints (`/routes`, `/models`, `/utils`)  
- 🧮 Cost-of-Living data ingestion and parsing via pre-downloaded datasets  
- 🧱 SQL-backed data model for countries, states/provinces, and cities  
- 🧰 REST API endpoints (in progress) for accessing COL data  
- 💾 Database migrations using Flask-Migrate  
- 🧪 Preliminary tests for model validation and API responses  

---

## 🧩 Planned Features

- 📊 Dynamic frontend interface for COL comparisons  
- 🌍 Hierarchical location selection:  
  - Select **Country → State/Province → City**  
  - Dynamically filter cities based on selections  
- 💱 Currency conversion and standardization  
- 🔍 Integration with real-time APIs (e.g., Open Exchange Rates or Numbeo)  
- 💾 User profiles for saving and revisiting comparisons  
- 🔐 Authentication with Flask-Login  
- ☁️ Deployment on AWS (App Runner + RDS PostgreSQL + S3 for static assets)

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Python 3, Flask |
| **Database** | PostgreSQL + SQLAlchemy ORM |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Templating** | Jinja2 |
| **Testing** | Pytest / Unittest |
| **Version Control** | Git + GitHub |
| **Deployment (Planned)** | AWS RDS, App Runner or Elastic Beanstalk |
| **Data Sources** | Country/state/city datasets and COL indices |

---

## 🚀 Getting Started (Dev Mode)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Brice-Financial-Projects/Nomad-Nest.git
cd Nomad-Nest
```

--- 

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Flask app

```bash
python run.py
```

The app will be available at:

```cpp
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```graphql
Nomad-Nest/
│
├── app/
│   ├── config/         # App configuration files
│   ├── data/           # Static datasets (COL indices, city data)
│   ├── models/         # SQLAlchemy models for countries/cities
│   ├── routes/         # Flask blueprints (API endpoints)
│   ├── static/         # CSS, JS, and images
│   ├── templates/      # HTML templates (Jinja2)
│   ├── tests/          # Unit and integration tests
│   ├── utils/          # Helper modules (data loaders, validators)
│   ├── __init__.py     # App factory
│   └── extensions.py   # Initialize Flask extensions
│
├── migrations/         # Alembic database migrations
├── requirements.txt    # Project dependencies
├── run.py              # App entry point
└── structure.md        # Documentation of folder layout
```

---

## 🧠 Lessons Learned (In Progress)

- Building scalable Flask apps using the application factory pattern  
- Structuring multi-module projects for maintainability  
- Managing hierarchical data models for global datasets  
- Planning database migrations and schema design early  
- Designing APIs to serve structured, queryable economic data  
- Integrating static data ingestion workflows for reproducibility  

---

## 🌱 Future Enhancements

- Integrate **machine learning** models for COL prediction  
- Implement caching with **Redis** for repeated city queries  
- Add analytics dashboards for visual comparisons (Plotly / Chart.js)  
- Deploy a REST API microservice version (FastAPI or Flask-RESTX)  
- Add localization and language support  
- Integrate external exchange rate APIs for real-time conversions  
- Develop an authentication system with JWT or Flask-Login  

---

## 🪪 License & Author

This project is open source under the **MIT License** — free to use, modify, and distribute.

**Author:** Brice A. Nelson  
🌐 [devbybrice.com](https://www.devbybrice.com)  
💼 [LinkedIn](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/)

---

> _“Data meets wanderlust — empowering global citizens to compare, plan, and thrive anywhere on Earth.”_ 🌎
