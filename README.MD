# Sum of numbers API

Exercise started: `8:40`, ended: `9:25`

First prepare virtual environment of your choice and install requirements.

Production:

    pip install -r requirements.txt

Development:

    pip install -r dev-requirements.txt

To run the program use:

    uvicorn main:app --reload

and then access endpoint in the browser:

    http://localhost:8000/total

Custom port `5000`:

    uvicorn main:app --port 5000 --reload

    http://localhost:5000/total

To execute unit tests run:

    python -m unittest

or

    pytest tests
