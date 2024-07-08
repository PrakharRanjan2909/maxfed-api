1. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows  `venv\Scripts\activate`
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```
API End Point 
1. POST /transform/chargecodes
2. POST /transform/instances
   
(http://127.0.0.1:8000/transform/chargecodes)
