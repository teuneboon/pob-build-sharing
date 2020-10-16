This is just a proof of concept to test how much load we can handle without optimization.

# Development
To run the example(which currently uses an SQLite database), you probably want to make a virtualenv and then run:

1. `pip install -r requirements.txt`
2. `uvicorn main:app --reload`

This starts a local development server running at `http://localhost:8000`


# TODO

If we're out of PoC status we'd need:

- Better organized folder structure
- Proper security measures
- Maybe design some landing page if you go to the site in a browser
- Maybe switch to setup.py instead of requirements.txt
- Linting + other CI stuff
