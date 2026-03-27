## 🔑 Setup

1. Get a Gemini API key from https://aistudio.google.com/apikey

2. Set it as environment variable:

**On Windows:**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**On Mac/Linux:**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

3. Run the script:
```bash
python med_translate.py
```
```

---

### **Step 3: Add to .gitignore**

**Create `.gitignore` file:**
```
# Environment variables
.env
*.env

# API keys
*api_key*
config.py

# Virtual environment
env/
venv/

# Python cache
__pycache__/
*.pyc