## Setup Instructions

### Python Environment
```bash
python -m venv .venv
```

Activate the virtual environment:
- **Windows:** `./.venv/Scripts/activate`
- **macOS/Linux:** `./.venv/bin/activate`

### Install Dependencies
```bash
pip install -r requirements.txt
npm i
```

### Run the Application
```bash
flask --app main run
```

### Build Tailwind CSS
```bash
npx @tailwindcss/cli -i ./static/style.css -o ./static/output.css --watch
```