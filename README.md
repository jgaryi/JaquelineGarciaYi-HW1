# JaquelineGarciaYi-HW1
E115 Homework 1: Creating a Docker Container for Data Science

**Instructions**

**Write a Dockerfile** [3 points]

- Start with a base image, such as `3.11-slim-buster`
- Ensure we have an up to date baseline and install any OS dependencies
- Add a user app like we did in tutorials
- Set the working directory to /app
- Use `RUN` commands to install necessary packages. Consider using `pipenv` for Python package installations.
- Ensure you are running `pipenv sync` so that we can build and run your Dockerfile with all the python packages
- Set your entry point is set to `/bin/bash`
- Set your command to open up `pipenv shell`

**Write a Python Script** [0.5 points]

- Write a python script that uses `linear_model` from `sklearn` to predict the dependent variable.
- Use the `diabetes` data from the `datasets` module in `sklearn`.
- Make sure to print the predictions at the end.

**Submission Files** [0.5 points]

Your submission repo should have the following files:

```
   |-student-name-hw1
     |-Dockerfile
     |-Pipfile
     |-Pipfile.lock
     |-regression.py
     |-test.py
```

**Testing**
Create a file called `test.py` with the following content:

```
# Q1
import sys
version_info = sys.version_info
output = str(version_info.major) + "." + str(version_info.minor)
assert output == "3.11"

# Q2
from sklearn import datasets, linear_model
import numpy as np

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
assert True == True
```

You can test your work using the `test.py`. Just run `python test.py` and you should not receive any errors.

**Submission**

- Submit your zipped folder (`student-name-hw1`) with above code files to Canvas
