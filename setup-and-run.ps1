python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --no-cache-dir -r requirements.txt
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload