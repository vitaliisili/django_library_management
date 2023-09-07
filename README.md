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

Step 6: Create a new database migrations
```bash
python -m manage makemigrations
```
Alternative: `make makemigrations`


Step 7: Apply migration to a database
```bash
python -m manage migrate
```
Alternative: `make migrate`

Step 8: Create a superuser for logging into the admin panel
```bash
python -m manage createsuperuser
```
Alternative: `make createsuperuser`

Step 9: Run application
```bash
python -m manage runserver
```
Alternative: `make runserver`

Step 10: In browser open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### *Enjoy!*


## Contributing

Thank you for your interest in contributing to our project! We welcome contributions from the community and appreciate your time and effort. Before you get started, please take a moment to read through the guidelines below:

### Getting Started

1. Fork the repository and clone it to your local machine.
2. Install any necessary dependencies by following the instructions in the project's documentation.
3. Create a new branch for your contributions: `git checkout -b your-branch-name`.
4. Make your desired changes or additions to the codebase.
5. Test your changes thoroughly to ensure they do not introduce any new issues.
6. Commit your changes with a descriptive commit message: `git commit -m "Add your message here"`.
7. Push your changes to your forked repository: `git push origin your-branch-name`.
8. Submit a pull request to the main repository, clearly explaining the purpose and details of your contribution.

### Code Guidelines

- Follow the coding style and conventions used in the project.
- Write clear and concise code with meaningful comments where necessary.
- Ensure your code is properly formatted and indented.

### Communication

If you have any questions, concerns, or need assistance, please don't hesitate to reach out to us.
We appreciate your contributions and look forward to working with you!


Thank you for your interest in `Django Library Management`! We hope you find it valuable and enjoy using it. 

![tree.png](docs%2Fimages%2Ftree.png)