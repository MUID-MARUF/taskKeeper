#Task Keeper

> A liteweight, fast & reliable task manager backend project which can be used for both mobile & web platforms.

## Features

- Feature 1: Organize messy todo tasks in a simple and effective way.
- Feature 2: Can be implemented in multiple platforms (ex: Android, IOS, MacOS, Linux, Windows and many more).
- Feature 3: REST API for easy and robust implementation.
- Feature 4: Uses JWT token for secured authentication.
- Feature 5: Can be used in both local or cloud database systems.

## Project Structure

---- root/
|---- api/
| |---- migrations/
| |---- **init**.py
| |---- admin.py
| |---- app.py
| |---- models.py
| |---- serializers.py
| |---- tests.py
| |---- urls.py
|---- taskManager/
| |---- **init**.py
| |---- asgi.py
| |---- settings.py
| |---- urls.py
| |---- wsgi.py
---- manage.py
---- pyproject.toml
---- readme.md
---- uv.lock

## API Endpoints Methods

1. root / fetch all tasks ("api/") -> GET
2. login ("api/login/") -> GET
3. refresh token ("api/refresh") -> GET
4. register new user ("api/register/") -> POST
5. create a new task ("api/create/") -> POST
6. Update task ("api/updte/<uuid:pk>/") -> PUT
7. Delete an exixting task ("api/delete/<uuid:pk>/") -> DELETE

## Prerequisites and Implementation

- Install UV [pip install uv]
- Clone the repository
- Create & activate a virtual environment using uv [uv venv] & [.venv/bin/activate]
- Configure Database technology and deployment configs in taskManager/settings.py
- Migrate the database using [uv run python manage.py makemigrations && migrate]
- run the project using [uv run python manage.py runserver]
- Wallah! You're done!

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/XYZ`)
3. Commit your Changes (`git commit -m 'Add XYZ'`)
4. Push to the Branch (`git push origin feature/XYZ`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- Muid Hasan Maruf - muidmarufa2@gmail.com
