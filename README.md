# Clock CAPTCHA
A web-based CAPTCHA system using a draggable analog clock to verify human users. Built with Django, HTML, CSS, and JavaScript, it adds an interactive and visually challenging verification step for login forms.  

## Features
- Interactive Clock CAPTCHA: Users drag the hour and minute hands to match a target time.
- Distorted Time Display: The target time is displayed as a noisy, distorted image to prevent automated reading.
- Custom Validation: Only correct time entry enables the login button.
- Seamless UX: CAPTCHA popup overlays the login page and closes automatically on success.
- Redirection: Upon successful verification, users are redirected to a “Signed In” page.
- Refresh Option: Users can generate a new target time without reloading the page.

## Installation
1. Clone the repository
    git clone https://github.com/mhmistry/clock_captcha.git
    cd clock_captcha

2. Create a virtual environment (optional but recommended)
    python -m venv venv
    venv\Scripts\activate # Windows
    source venv/bin/activate # macOS/Linux

3. Install dependencies
    pip install django

4. Run the server
    python manage.py runserver

5. Open your browser and go to:
    http://127.0.0.1:8000/


## Usage
1. Enter a username and password.
2. Check the "I'm not a robot" box to open the CAPTCHA.
3. Drag the clock hands to match the distorted target time.
4. Click Submit to verify.
5. Upon success, you are redirected to the signed-in page.

## Folder Structure
clock_captcha/
├── captcha_app/
│ ├── templates/
│ │ ├── login.html
│ │ └── signed_in.html
│ ├── views.py
│ ├── urls.py
│ └── ...
├── captcha_project/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── manage.py
└── README.md

## Tech Stack
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default Django database)

## License
This project is open-source and free to use for educational purposes.

   

