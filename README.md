# The API Scrapper

A Python-based weather data scraper that fetches current weather information for major cities in Pakistan using the OpenWeatherMap API and stores the collected data in CSV format.

The application can be run locally using Python or containerized and executed using Docker.

## Features

* Fetches weather data from OpenWeatherMap API
* Retrieves weather information for:

  * Karachi
  * Lahore
  * Islamabad
  * Peshawar
  * Quetta
* Converts API responses into a Pandas DataFrame
* Saves the weather data as a CSV report
* Uses environment variables to protect the API key
* Dockerized for consistent execution across different machines

## Technologies Used

* Python
* Requests
* Pandas
* Python-dotenv
* Docker
* OpenWeatherMap API

## Project Structure

```text
The-API-Scrapper/
│
├── weather.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
├── README.md
│
└── output/
    └── weather_report_DD-MM-YYYY.csv
```

## Prerequisites

### For Local Execution

You need:

* Python 3.12 or later
* pip
* An OpenWeatherMap API key

### For Docker Execution

You need:

* Docker Desktop

Python does not need to be installed when running the application through Docker.

## Environment Variables

Create a `.env` file in the project root:

```env
api_key=YOUR_OPENWEATHERMAP_API_KEY
```

Replace `YOUR_OPENWEATHERMAP_API_KEY` with your actual API key.

> Do not commit the `.env` file to GitHub. The `.env` file is excluded using `.gitignore` and `.dockerignore`.

## Running Locally

Create and activate a virtual environment if desired:

```bash
python -m venv venv
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python weather.py
```

The generated report will be saved inside the `output` directory:

```text
output/weather_report_DD-MM-YYYY.csv
```

## Docker

### Build the Docker Image

From the project directory, run:

```bash
docker build -t weather-scraper .
```

Verify that the image was created:

```bash
docker images
```

You should see:

```text
weather-scraper
```

### Run the Docker Container

Run:

```powershell
docker run --rm --env-file .env -v "${PWD}\output:/app/output" weather-scraper
```

The command:

* Loads the API key from `.env`
* Starts the Docker container
* Executes `weather.py`
* Mounts the local `output` directory into the container
* Saves the generated CSV file to the host machine
* Automatically removes the container after execution

## Docker Architecture

The application follows this basic Docker workflow:

```text
weather.py
     │
     ├── requirements.txt
     │
     └── Dockerfile
             │
             ▼
       Docker Image
       weather-scraper
             │
             ▼
       Docker Container
             │
             ▼
       OpenWeatherMap API
             │
             ▼
       Weather Data
             │
             ▼
       output/*.csv
```

## Security

The OpenWeatherMap API key is stored in an environment variable rather than being hard-coded into the Python source code.

The `.env` file should never be committed to a public Git repository.

Recommended `.gitignore` entry:

```text
.env
__pycache__/
*.pyc
output/
```

## Author

Muhammad Asfar

