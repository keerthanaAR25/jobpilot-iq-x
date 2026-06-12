# 🚀 Setup & Deployment Instructions

## Table of Contents
1. [Quick Start (5 minutes)](#quick-start)
2. [Development Setup](#development-setup)
3. [Running the Application](#running-the-application)
4. [Production Deployment](#production-deployment)
5. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Prerequisites
- **Python 3.8 or higher**
- **Git** (for cloning repository)
- **pip** (Python package manager)

### Installation (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/[your-username]/jobpilot-iq-x.git
cd jobpilot-iq-x

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## Development Setup

### Step 1: System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8+
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 500MB free space

### Step 2: Clone Repository
```bash
git clone https://github.com/[your-username]/jobpilot-iq-x.git
cd jobpilot-iq-x
```

### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 5: Verify Installation
```bash
# Check Python version
python --version

# Check installed packages
pip list

# Verify key packages
python -c "import streamlit; import openai; import pandas; print('✓ All core packages installed')"
```

### Step 6: Configure Environment (Optional)
```bash
# Create .env file in project root
touch .env  # On Windows: type nul > .env

# Add your OpenAI API key (if needed)
echo OPENAI_API_KEY=your_api_key_here >> .env
```

---

## Running the Application

### Development Mode (Recommended for Testing)
```bash
# Ensure venv is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run with development settings
streamlit run app.py

# Optional: Run with dev options
streamlit run app.py --logger.level=debug
```

**Access**: http://localhost:8501

### Command Line Options
```bash
# Run with custom port
streamlit run app.py --server.port 8000

# Run without browser auto-open
streamlit run app.py --client.showErrorDetails=true

# Run in headless mode (server only)
streamlit run app.py --server.headless true
```

### File Structure for Reference
```
jobpilot-iq-x/
├── app.py                          # Main application entry
├── requirements.txt                # Python dependencies
├── config/
│   ├── __init__.py
│   └── config.py                   # Configuration settings
├── data/
│   ├── knowledge_base/             # Knowledge base JSON files
│   │   ├── companies.json
│   │   ├── roles.json
│   │   └── opportunities.json
│   └── uploads/                    # User uploads directory
├── src/
│   ├── modules/                    # Core business logic
│   │   ├── career_agents.py
│   │   ├── career_health.py
│   │   ├── foundry_iq.py           # Foundry IQ implementation
│   │   ├── interview_arena.py
│   │   └── resume_parser.py
│   ├── pages/                      # Streamlit pages
│   │   ├── dashboard.py
│   │   ├── resume_analyzer.py
│   │   ├── career_health.py
│   │   ├── career_twin.py
│   │   ├── company_readiness.py
│   │   ├── skill_gap_analyzer.py
│   │   ├── career_gps.py
│   │   ├── opportunity_radar.py
│   │   ├── interview_arena.py
│   │   ├── shortlist_analyzer.py
│   │   ├── action_plan.py
│   │   └── settings.py
│   └── utils/                      # Utility functions
│       ├── database.py
│       └── helpers.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   └── API.md
└── README.md
```

---

## Production Deployment

### Option 1: Streamlit Cloud (Recommended for Demo)

**Easiest deployment option for showing off your project!**

#### Prerequisites
- GitHub account with repository
- Streamlit Cloud account (free)

#### Steps
1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for production"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repository
   - Choose main branch and `app.py` as entry point
   - Click "Deploy"

3. **Share Your Link**
   - Your app will be live at: `https://jobpilot-iq-x-[username].streamlit.app`

#### Performance
- ✅ Fast deployment
- ✅ Free tier available
- ✅ Auto-scaling
- ✅ Custom domain support

---

### Option 2: Docker (Best for Enterprise)

#### Prerequisites
- Docker installed

#### Steps

1. **Create Dockerfile** (if not exists)
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore**
   ```
   venv
   __pycache__
   .git
   .gitignore
   .env
   ```

3. **Build and Run**
   ```bash
   # Build image
   docker build -t jobpilot-iq-x:latest .

   # Run container
   docker run -p 8501:8501 jobpilot-iq-x:latest

   # Run with volume mount for persistence
   docker run -p 8501:8501 -v $(pwd)/data:/app/data jobpilot-iq-x:latest
   ```

#### Push to Docker Hub
```bash
# Login to Docker Hub
docker login

# Tag image
docker tag jobpilot-iq-x:latest [username]/jobpilot-iq-x:latest

# Push
docker push [username]/jobpilot-iq-x:latest
```

---

### Option 3: AWS Deployment

#### Option 3a: AWS EC2
```bash
# 1. Launch EC2 instance (Ubuntu)
# 2. SSH into instance
ssh -i your-key.pem ec2-user@your-instance.com

# 3. Install dependencies
sudo yum update
sudo yum install python3 python3-pip git

# 4. Clone and setup
git clone https://github.com/[your-username]/jobpilot-iq-x.git
cd jobpilot-iq-x
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Run with screen (keeps running after logout)
screen -S jobpilot
streamlit run app.py --server.port 80 --server.address 0.0.0.0

# Access via: http://your-ec2-public-ip
```

#### Option 3b: AWS ECS (Containerized)
```bash
# Create ECR repository
aws ecr create-repository --repository-name jobpilot-iq-x

# Build and push to ECR
docker build -t jobpilot-iq-x:latest .
docker tag jobpilot-iq-x:latest [account].dkr.ecr.us-east-1.amazonaws.com/jobpilot-iq-x:latest
docker push [account].dkr.ecr.us-east-1.amazonaws.com/jobpilot-iq-x:latest

# Create ECS task definition and service (via AWS Console or AWS CLI)
```

---

### Option 4: Azure Deployment

```bash
# 1. Install Azure CLI
# See: https://docs.microsoft.com/cli/azure/install-azure-cli

# 2. Login to Azure
az login

# 3. Create resource group
az group create --name jobpilot-rg --location eastus

# 4. Create App Service
az appservice plan create \
  --name jobpilot-plan \
  --resource-group jobpilot-rg \
  --sku B1 \
  --is-linux

# 5. Create web app
az webapp create \
  --resource-group jobpilot-rg \
  --plan jobpilot-plan \
  --name jobpilot-iq-x \
  --runtime "PYTHON|3.9"

# 6. Deploy from GitHub
az webapp deployment github-actions add \
  --repo [your-username]/jobpilot-iq-x \
  --branch main \
  --resource-group jobpilot-rg \
  --name jobpilot-iq-x
```

---

### Option 5: Heroku Deployment

```bash
# 1. Install Heroku CLI
# See: https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create jobpilot-iq-x

# 4. Create Procfile (in project root)
echo "web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0" > Procfile

# 5. Deploy
git push heroku main

# 6. Access
heroku open
```

---

## Verification Checklist

After deployment, verify these features work:

### Core Features
- [ ] Resume upload and parsing works
- [ ] Career health score calculates correctly
- [ ] Career twin generates future profile
- [ ] Company readiness shows analysis
- [ ] Skill gap analyzer displays gaps
- [ ] Career GPS shows 30/60/90 plans
- [ ] Opportunity radar ranks opportunities
- [ ] Interview arena Q&A works
- [ ] Shortlist analyzer provides insights
- [ ] Action plan generates tasks

### Technical Verification
- [ ] No errors in console
- [ ] Database operations complete
- [ ] Charts render correctly
- [ ] Page navigation smooth
- [ ] Responsive on mobile
- [ ] Performance acceptable (< 2s load)

### Data Verification
- [ ] Knowledge base loaded
- [ ] Companies accessible
- [ ] Roles displayed
- [ ] Opportunities ranked
- [ ] User data persists

---

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'streamlit'

**Solution:**
```bash
# Ensure venv is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Reinstall requirements
pip install -r requirements.txt
```

### Issue: Port 8501 already in use

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill process on port 8501
# Windows:
netstat -ano | findstr :8501
taskkill /PID [PID] /F

# macOS/Linux:
lsof -ti :8501 | xargs kill -9
```

### Issue: Resume parsing fails

**Troubleshooting:**
- Ensure PDF is valid and readable
- Check file size < 10MB
- Verify PDF isn't encrypted
- Try uploading sample PDF from `data/samples/`

### Issue: Database errors

**Solution:**
```bash
# Reset database (WARNING: Loses user data)
rm -f jobpilot.db

# Or manually clear:
python -c "from src.utils.database import init_db; init_db()"
```

### Issue: Application runs slow

**Solutions:**
1. Clear browser cache: `Ctrl+Shift+Delete`
2. Restart Streamlit: Kill process and run again
3. Check system resources (RAM, CPU)
4. Clear `__pycache__` directories: `find . -type d -name __pycache__ -exec rm -r {} +`

### Issue: GitHub Copilot not available

**Note:** GitHub Copilot is used during development. If not available:
- The application still functions fully
- Code suggestions may be unavailable in IDE
- All features work as designed

### Issue: OpenAI API errors

**Check:**
1. API key is set correctly in `.env`
2. API key has valid balance/quota
3. Network connectivity is working
4. Rate limits aren't exceeded

---

## Performance Optimization

### Frontend Optimization
- Enable caching: `@st.cache_data`
- Use session state for user data
- Lazy load heavy components
- Minimize Plotly rendering

### Backend Optimization
- Cache knowledge base in memory
- Use indexed database queries
- Connection pooling for DB
- Async operations where possible

### Deployment Optimization
- Use CDN for static files
- Enable gzip compression
- Optimize Docker image size
- Use production-grade WSGI server if needed

---

## Monitoring & Maintenance

### Application Health
```bash
# Monitor logs (Streamlit Cloud)
# View in browser console and Streamlit logs

# Docker logs
docker logs [container-id] -f

# AWS CloudWatch
# Monitor EC2 metrics and logs
```

### Regular Maintenance
- [ ] Check logs for errors weekly
- [ ] Backup database monthly
- [ ] Update dependencies quarterly
- [ ] Review performance metrics monthly

---

## Support & Issues

### Getting Help
1. **Check Documentation**: `docs/` folder
2. **GitHub Issues**: Create issue in repository
3. **Troubleshooting**: See section above
4. **Hackathon Support**: Contact hackathon organizers

### Reporting Issues
Include:
- Error message and stack trace
- Steps to reproduce
- System information (OS, Python version)
- Environment details

---

## Next Steps

1. **Test locally** with `streamlit run app.py`
2. **Deploy to Streamlit Cloud** for easy demo
3. **Share link** with judges
4. **Monitor performance** after deployment
5. **Iterate based feedback**

---

## Deployment Comparison

| Platform | Setup Time | Cost | Scalability | Monitoring |
|----------|-----------|------|-------------|-----------|
| **Streamlit Cloud** | < 5 min | Free | Good | Excellent |
| **Docker** | 15 min | Varies | Excellent | Manual |
| **AWS** | 30 min | $5-50/mo | Excellent | Excellent |
| **Azure** | 30 min | $5-50/mo | Excellent | Excellent |
| **Heroku** | 10 min | $7-50/mo | Good | Excellent |

**Recommendation for Hackathon**: Use **Streamlit Cloud** for fastest, easiest demo!

---

## Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Cloud**: https://streamlit.io/cloud
- **Python Docs**: https://docs.python.org/3
- **Docker Docs**: https://docs.docker.com
- **AWS Docs**: https://docs.aws.amazon.com
- **Azure Docs**: https://docs.microsoft.com/azure

---

**Last Updated**: December 2024  
**Status**: Production Ready
