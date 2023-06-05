A toy repository to learn how to make packages in python.

Install package simply by 

```
cd math_operations/
pip install .
cd ..
```

To install all recommended requirements : 

```
# navigate to package directory
cd math_operations
# using virtualenv 
pip install virtualenv
virtualenv pkg_env
# On Mac
source pkg_env/bin/activate
# On Windows Command Prompt
pkg_env\Scripts\activate.bat
#install all packages
cd ..
pip install -r requirements.txt
```