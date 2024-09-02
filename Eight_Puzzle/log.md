python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1

deactivate 
pip freeze > requirements.txt

pip install sphinx
sphinx-quickstart

go to config.py and import os, import sys, and sys.path.insert(0, os.path.abspath(r'C:\Users\Ryan\CSDS_391\Eight_Puzzle\src'))

go to index.rst file and add modules under Contents

in documentation directory  
sphinx-apidoc -o . ..
./make.bat html

------

sphinx-apidoc -o C:\Users\Ryan\CSDS_391\Eight_Puzzle\documentation\source 
C:\Users\Ryan\CSDS_391\Eight_Puzzle\documentation\make.bat html

pip install sphinx-autobuild
sphinx-autobuild . ..