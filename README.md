# Mini Blog 🚀
   A full-featured, responsive blogging platform built with **Django** and **PostgreSQL**. This project allows users to share their stories, engage with readers through comments, and receive automated
      notifications.
      
  ## ✨ Features
  
   **User Authentication:** Secure registration, login, and logout functionality.
   **Blog Management:** Registered users can create and publish their own blog posts.
   **Commenting System:** Interactive comments section on every post to foster engagement.
   **Smart Search:** Quickly find articles by title using the integrated search functionality.
   **Email Notifications:** Automatic alerts (via terminal console) when a post receives a new comment.
   **Responsive Design:** A clean, modern UI built with **Bootstrap 5** that works seamlessly on mobile, tablet, and desktop.
   **PostgreSQL Integration:** Uses a robust relational database for scalable data management.
   
   ## 🛠️ Tech Stack
   
   **Backend:** [Django](https://www.djangoproject.com/) (Python)
   **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/)
   **Database:** [PostgreSQL](https://www.postgresql.org/)
   **Environment:** Python Virtual Environment (venv)
   
   ## 🚀 Getting Started
   
   ### Prerequisites
   
   Python 3.10+
   PostgreSQL installed and running
    `pip` (Python package manager)
   
   ### Installation & Setup
   
   1. **Clone the repository:**
     git clone https://github.com/yourusername/mini-blog.git
     cd mini-blog
   
   2. **Set up the Virtual Environment:**
     python -m venv venv
  On Windows:
     venv\Scripts\activate
  On macOS/Linux:
     source venv/bin/activate
   
   4. **Database Configuration:**
      - Create a PostgreSQL database named `blog_db`.
      - Update the `DATABASES` section in `blog_project/settings.py` with your PostgreSQL credentials (`USER` and `PASSWORD`).
    
  **Apply Migrations:**
     python manage.py migrate
   
  **Create a Superuser (Admin):**
     python manage.py createsuperuser
   
   **Run the Server:**
     python manage.py runserver

  Visit the app at `http://127.0.0.1:8000/home/`.
    
  ## 📂 Project Structure
    
   `blog/`: Contains the core logic, models (Post, Comment), and templates.
     `blog_project/`: Project-level settings and URL configurations.
     `templates/`: HTML files styled with Bootstrap 5.
    
  ## 📧 Email Notifications
   Currently, `EMAIL_BACKEND` is set to `console`. When a new comment is posted, the notification content will be printed to your terminal. To use a real email service (like Gmail), update the SMTP
      settings in `settings.py`.
