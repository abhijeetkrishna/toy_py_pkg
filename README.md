A toy repository to learn how to make packages in python.

Install package simply by 

```
pip install .
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
pip install -r ../requirements.txt
```
## Acknowledgements

I learnt how to make a python package almost completely from [ChatGPT](https://chat.openai.com/). 

## To Do

* Use [pytest](https://docs.pytest.org/en/latest/) to run tests