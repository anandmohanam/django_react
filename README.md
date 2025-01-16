# Django REST Framework and React.js Sample Project

## Folder Structure
```
├── db.sqlite3
├── manage.py
├── run.bat
├── api
├── base
├── env
├── myapp
└── mysite
```

## API Features
- **GET**: Retrieve data from the server.
- **DELETE**: Remove data from the server.
- **POST**: Send data to the server.

## Installation Process
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the username, email, and password.

## Running the Project
### Option 1: Using `run.bat`
- Simply double-click on the `run.bat` file to start the project.

### Option 2: Using Command Line
1. Navigate to the project directory:
   ```bash
   cd </path>
   ```
2. Start the Django server:
   ```bash
   python manage.py runserver
   ```
3. Navigate to the `myapp` directory:
   ```bash
   cd myapp
   ```
4. Start the React.js app:
   ```bash
   npm start
   ```

