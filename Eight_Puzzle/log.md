python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1

deactivate 
pip freeze > requirements.txt

pip install sphinx
sphinx-quickstart
.\make.bat html
### this one works globally
sphinx-build -b html source/ build/html/ 