#!/bin/bash
# Quick Start Script for JobPilot IQ X

echo "🚀 JobPilot IQ X - Quick Start"
echo "=============================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Found: Python $python_version"
echo ""

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate

echo "✓ Installing dependencies..."
pip install -q -r requirements.txt

echo "✓ Initializing database..."
python3 -c "from src.utils.database import Database; Database(); print('  Database initialized')"

echo ""
echo "✓ Setup complete!"
echo ""
echo "🚀 Starting JobPilot IQ X..."
echo "════════════════════════════"
echo ""
echo "Access the app at: http://localhost:8501"
echo ""

streamlit run app.py
