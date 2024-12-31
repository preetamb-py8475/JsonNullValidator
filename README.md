# JSON Null Validator

> Programming Language: Python 3.10.5

> IDE: PyCharm Community Edition 2024.3.1.1

> REST API Framework: Flask 3.1.0

> REST API Client: Postman (one can also use Python `requests` library)

> VCS: Git

---

## Steps to run (in Windows 10 64-bit):
1. Install Python 3.10.5 in your local machine.
2. Install Git.
3. Install Postman.
4. Clone the GitHub repository -- `git clone https://github.com/preetamb-py8475/JsonNullValidator.git`.
5. Change directory to the project folder -- `cd JsonNullValidator`.
6. Create virtual environment -- `python -m venv .venv`.
7. Activate the virtual environment -- `.venv\Scripts\activate`.
8. Install requirements.txt -- `pip install -r requirements.txt` -or- Install Flask -- `pip install Flask`.
9. Run 'app.py' -- `python app.py` (This is run the development server in your local machine).
10. Open Postman & test the following 3 REST API calls:
  1. Valid JSON:
        * Input:
        > HTTP Method - `POST`

        > URL - `http://127.0.0.1:5000/validate`
        
        > Payload (Body > raw) - `valid.json`

        * Expected Output:
        > `{ "status": "success" }`

  2. Invalid JSON:
        * Input:
        > HTTP Method - `POST`
        
        > URL - `http://127.0.0.1:5000/validate`
        
        > Payload (Body > raw) - `invalid.json`

        * Expected Output:
        > `{ "invalid_fields": ["user.age", "user.address.city", "order.items[1].price"], "status": "error" }`

  3. [BONUS] Optional NULL Check:
        * Input:
        > HTTP Method - `POST`
        
        > URL - `http://127.0.0.1:5000/validate?optional_fields=user.age,user.address.city`
        
        > Payload (Body > raw) - `invalid.json`

        * Expected Output:
        > `{ "invalid_fields": ["order.items[1].price"], "status": "error" }`
