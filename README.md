# System Events Backend API

This Flask application serves as the backend API for the Faker Event Generator and Monitor web application. It provides endpoints for generating fake system events, monitoring them, and handling the saving of event files.

## Dependencies

- Flask: A micro web framework for Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).

## API Endpoints

1. API endpoints can be added and removed as per need as of now all are 'GET' Types.
2. The user can opt to select the number of events by endpoint parameters
3. ```savelog``` Parameter can be used to dynamically opt in or out from saving log.


## Running the Backend

To run the backend server, follow these steps:

1. Navigate to the root directory.
2. Install the required Python dependencies using pip:
3. ```pip install flask```
4. ```pip install flask-cors```
5. execute `python server.py`
6. This will start the Flask server on `http://localhost:5000`.

## Additional Notes

- Customize the logic within the Flask endpoints according to your requirements.
- Ensure that the frontend application is configured to make requests to the correct backend endpoints.
- For production deployment, consider deploying the Flask application on a production server like Gunicorn or uWSGI behind a reverse proxy like Nginx.

