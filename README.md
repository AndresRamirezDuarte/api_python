# API

## Set Up

1. create virtual environment

    ```
    python -m venv venv
    ```

    ```
    .\env\Scripts\activate
    ```

2. Install requirements

    ```
    pip install requirements.txt
    ```

3. Start the server development with:

    ```
   python -m app
    ```
   
4. Start the server waitress 

    ```
    waitress-serve --port=5000 --call "app:create_app"
    ```
 

## CONFIG
  
Set environment in run_app.bat 

  -TESTING, PRODUCTION, DEVELOPMENT  
