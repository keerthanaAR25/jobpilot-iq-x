# 🔧 Dependency Installation & Troubleshooting Guide

## ✅ Current Status

All dependencies have been successfully installed and verified:

```
✓ streamlit
✓ streamlit_extras  
✓ pandas
✓ numpy
✓ plotly
✓ PyPDF2
✓ pydantic
✓ dotenv
✓ requests
✓ openai
✓ json5
✓ sqlalchemy
✓ sqlite3
✓ typing-extensions

14/14 ✓ All dependencies installed successfully!
```

---

## 🚀 Running the Application

### Method 1: Using Batch Script (Easiest)
```bash
# Windows only - runs verification and starts app
verify_setup.bat
```

### Method 2: Manual Command
```bash
# Activate virtual environment
venv\Scripts\activate.bat

# Run application
streamlit run app.py
```

Application opens at: **http://localhost:8501**

---

## 🔍 Verify Dependencies Anytime

```bash
# Activate venv first
venv\Scripts\activate.bat

# Run verification
python verify_imports.py
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: "ModuleNotFoundError: No module named 'plotly'"
**Cause**: Virtual environment not activated or dependencies not installed

**Solution**:
```bash
# Activate the virtual environment
venv\Scripts\activate.bat

# Install/reinstall all dependencies
pip install -r requirements.txt

# Verify
python verify_imports.py
```

### Issue 2: "ModuleNotFoundError: No module named 'PyPDF2'"
**Cause**: Same as above

**Solution**: Same as Issue 1

### Issue 3: "ModuleNotFoundError: No module named 'streamlit'"
**Cause**: Virtual environment not activated

**Solution**:
```bash
# IMPORTANT: Must activate venv first!
venv\Scripts\activate.bat

# Then verify
python verify_imports.py
```

### Issue 4: "File is being used by another process"
**Cause**: Streamlit or another Python process still running

**Solution**:
```bash
# Option 1: Close VS Code terminal and reopen
# Option 2: Kill Python processes
taskkill /F /IM python.exe

# Then try again
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Issue 5: Permission Denied Errors
**Cause**: Antivirus or file locking

**Solution**:
```bash
# Try installing with no-cache
pip install --no-cache-dir -r requirements.txt

# If still fails, use wheels only
pip install --only-binary :all: -r requirements.txt
```

---

## 📋 Dependency List & Versions

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | Latest | Web UI framework |
| plotly | Latest | Interactive charts |
| pandas | Latest | Data processing |
| numpy | Latest | Numerical computing |
| pypdf2 | Latest | PDF resume parsing |
| pydantic | Latest | Data validation |
| python-dotenv | Latest | Environment variables |
| requests | Latest | HTTP requests |
| openai | Latest | OpenAI API integration |
| sqlalchemy | Latest | Database ORM |
| json5 | Latest | JSON parsing |
| streamlit-extras | Latest | Streamlit extensions |

---

## 🔄 Fresh Installation (Nuclear Option)

If nothing works, do a complete fresh install:

```bash
# 1. Remove old virtual environment
rmdir /s /q venv

# 2. Create new virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate.bat

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install requirements
pip install -r requirements.txt

# 6. Verify
python verify_imports.py
```

---

## ✅ Verification Checklist

- [ ] Virtual environment created (`venv` folder exists)
- [ ] Virtual environment activated (prompt shows `(venv)`)
- [ ] `verify_imports.py` returns all 14/14 ✓
- [ ] Can run `streamlit run app.py`
- [ ] Application opens at http://localhost:8501
- [ ] All 10 features load without errors
- [ ] Resume upload works
- [ ] Charts render properly

---

## 📞 Quick Reference Commands

```bash
# Show current environment
python --version
pip --version

# List installed packages
pip list

# Check specific package
pip show streamlit

# Install single package
pip install streamlit

# Reinstall all packages
pip install --force-reinstall -r requirements.txt

# Update pip
python -m pip install --upgrade pip

# Activate venv (Windows)
venv\Scripts\activate.bat

# Deactivate venv
deactivate
```

---

## 🎯 Next Steps

1. ✅ **Verify Setup**: Run `python verify_imports.py`
2. ✅ **Start Application**: Run `streamlit run app.py`
3. ✅ **Open in Browser**: Navigate to `http://localhost:8501`
4. ✅ **Test All Features**: Click through all 10 pages
5. ✅ **Deploy**: Follow SETUP_INSTRUCTIONS.md for deployment

---

## 📊 Current Environment

- **Python**: 3.14+
- **Virtual Environment**: `venv/`
- **Dependencies**: 14 core packages installed
- **Status**: ✅ Production Ready

---

## 💡 Pro Tips

1. **Always activate venv first** before running any Python commands
2. **Use `verify_imports.py`** to troubleshoot missing packages
3. **Keep requirements.txt updated** after adding new packages
4. **Create new venv** if experiencing persistent issues
5. **Use `--no-cache-dir`** flag if installation fails

---

**Last Updated**: June 12, 2026  
**Status**: ✅ All Dependencies Verified & Working
