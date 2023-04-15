# Dockerize-DRF-Cinema

**Installing using GitHub**
Clone the repository:
git clone https://github.com/Zoriana-Dvulit/Dockerize-DRF-Cinema.git

Install the necessary packages:
$ pip install -r requirements.txt

**_Run with Docker_**
1. Build the Docker image:
docker build -t cinema-app .

2. Run the Docker container:
docker run -p 8000:8000 cinema-app
The API will now be available at http://localhost:8000/.

Note: If you make any changes to the code, you will need to rebuild the Docker image before running the container again.

Alternatively, you can also run the API locally without Docker by following these steps:

Run locally

1. Create a virtual environment:
python -m venv venv
2. Activate the virtual environment:
source venv/bin/activate
3. Install the necessary packages:
pip install -r requirements.txt
4. Migrate the database:
python manage.py migrate
5. Run the development server:
python manage.py runserver
The API will now be available at http://localhost:8000/.