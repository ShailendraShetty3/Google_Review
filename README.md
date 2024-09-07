
### Installation process and running of the server

Create a folder to keep the project and virtual environment(considered best practice not necessarily followed but prefered) and move to the same directory.

Use `git clone https://github.com/ShailendraShetty3/Google_Review.git` command to install it in the local system.

After installation move to the project directory

Use `py -m venv myVirtualenv` to create virtual environment in windows.
If you are a Linux or MacOS user use `python -m venv myVirtualenv` to create virtual environment.

use `cd myVirtualenv` to move to the virtual environment

Activate virtual environment by `Scripts\activate`

If your virtual environment is activated you can see `(myVirtualenv)` in your terminal
Note use Command Prompt and don't use windows powershell. You have to customize it before using windows powershell for activating environment.

Now come out of virtual environment folder and move to your project forlder which is `Google_Review`
Note virtual environment has to be still activated.

Now use `pip install -r requirements.txt` to install all the dependencies required for the project.

Create the PostgreSQL database with name `integration` and user `shetty` if you want to change the configuration of the database connection go to `settings.py` and change the configuration of `DATABASES` section.

Use `python manage.py makemigrations` to to to configure the database for changes.

Use `python manage.py migrate` to apply the migrations to the database.

Use `python manage.py runserver 8000` to run the server in the port `8000` you can change it by changing the port number.

If you are running the server in `8000` port you can see API documentation swagger in `Your_IP_Address/8000/swagger/`

