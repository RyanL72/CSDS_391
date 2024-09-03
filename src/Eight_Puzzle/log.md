python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1

deactivate 
pip install -r requirements
pip freeze > requirements.txt

pip install sphinx
sphinx-quickstart

go to config.py and import os, import sys, and sys.path.insert(0, os.path.abspath('../../src'))

go to index.rst
.. toctree::
   :maxdepth=2
   :caption: Contents:

   Eight_Puzzle


 
sphinx-apidoc -o documentation/source/ src/  
.\make.bat html

------

sphinx-apidoc -o C:\Users\Ryan\CSDS_391\Eight_Puzzle\documentation\source 
C:\Users\Ryan\CSDS_391\Eight_Puzzle\documentation\make.bat html

pip install sphinx-autobuild
sphinx-autobuild . ..

>>> from Eight_Puzzle import Eight_Puzzle
