![Static Badge](https://img.shields.io/badge/Made_With-Python-blue?style=for-the-badge&logo=python&logoColor=brightgreen)
![Static Badge](https://img.shields.io/badge/Django-Template-blue?style=for-the-badge&logo=django&logoColor=brightgreen)
![Static Badge](https://img.shields.io/badge/Open-Source-blue?style=for-the-badge&logo=love&logoColor=brightgreen)
![Static Badge](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=brightgreen)
![Static Badge](https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge&logo=postgresql&logoColor=brightgreens)


# Django Library Management
![old_3_ratio_16_9.png](docs%2Fimages%2Fold_3_ratio_16_9.png)

## Description
Django Library Management is a comprehensive web-based application designed to streamline and automate library operations. 
It offers a robust solution for librarians and library staff to efficiently manage the library's resources, 
simplify the borrowing and returning process, and provide an intuitive catalog system for patrons.


## Key Features
1. User-Friendly Catalog System
- Easily add, update, and categorize books, journals, and other materials in the library's collection.
- Search and browse the catalog with advanced filtering options.
- View detailed information about each item, including author, publication date, and availability.
2. Patron Management
- Register new patrons and maintain their profiles.
- Keep track of borrowing history, due dates, and fines.
- Notify patrons of overdue materials and upcoming due dates via email or SMS.
3. Efficient Checkouts and Returns
- Streamline the checkout process using barcode scanning or manual entry.
- Generate receipts and due date reminders for borrowers.
- Simplify the return process and automatically update the item's availability status.
4. Administrative Dashboard
- Provide librarians with a centralized dashboard for managing library operations.
- Monitor real-time statistics, including inventory levels, patron activity, and fines.
- Customize access levels for library staff with role-based permissions.


## How To Start
Step 1: Clone the Repository
```bash
git clone https://github.com/vitaliisili/django_library_management.git
```

Step 2: Go to project folder, create a virtual environment and activate it
```bash
cd django_library_management
```
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```

Step 3: Install dependencies from `requirements.txt` file
```bash
pip install -r requirements.txt
```
Alternative: `make install`

Step 4: Create `.env` file in root directory
```bash
touch .env
```

Step 5: Add to `.env` database and django environments:
```dotenv
DB_NAME=example_database_name
DB_USER=database_user
DB_PASSWORD=strong_password
DB_HOST=database_host
DB_PORT=database_port
DJANGO_SECRET_KEY=strong_secret_key_min_32_chars
DJANGO_DEBUG=True
```
Example `.env` file:
```dotenv
DB_NAME=library_management
DB_USER=postgres
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=5432
DJANGO_SECRET_KEY=django-insecure-hj_gk3-=c%e_%yn#o4t4h350raetyse8)%9x3u_po^cfx&269!
DJANGO_DEBUG=True
```











Thank you for your interest in `Django Library Management`! We hope you find it valuable and enjoy using it. 