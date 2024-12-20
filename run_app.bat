call env\Scripts\activate.bat
set MODE=DEVELOPMENT
call waitress-serve --port=5000 --call "app:create_app"
