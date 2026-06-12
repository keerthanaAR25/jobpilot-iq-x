# 🚀 Deployment Guide

## Deployment Options

### Option 1: Streamlit Cloud (Recommended for Quick Demo)

#### Prerequisites
- GitHub account with repository
- Streamlit account

#### Steps

1. **Push code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit: JobPilot IQ X"
git remote add origin https://github.com/yourusername/jobpilot-iq-x.git
git push -u origin main
```

2. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `jobpilot-iq-x`
   - Main file path: `app.py`
   - Click "Deploy"

3. **Configure environment**
   - Settings → Secrets → Add API keys if needed
   - Settings → Advanced settings for resource allocation

4. **Your app is live!**
   ```
   https://jobpilot-iq-x-yourname.streamlit.app
   ```

### Option 2: Docker Deployment

#### Prerequisites
- Docker installed
- Docker Hub account (for image registry)

#### Steps

1. **Create Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. **Create .dockerignore**
```
__pycache__
*.pyc
.git
.env
data/uploads
.streamlit/secrets.toml
```

3. **Build and run locally**
```bash
# Build image
docker build -t jobpilot-iq-x:latest .

# Run container
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  jobpilot-iq-x:latest

# Visit http://localhost:8501
```

4. **Push to Docker Hub**
```bash
# Tag image
docker tag jobpilot-iq-x:latest yourusername/jobpilot-iq-x:latest

# Login to Docker Hub
docker login

# Push image
docker push yourusername/jobpilot-iq-x:latest
```

5. **Deploy to cloud** (e.g., AWS ECS, Google Cloud Run, Azure Container Instances)

### Option 3: Heroku Deployment

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Steps

1. **Create Heroku app**
```bash
heroku create jobpilot-iq-x
```

2. **Create Procfile**
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

3. **Create setup.sh**
```bash
#!/bin/bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

4. **Create runtime.txt**
```
python-3.9.16
```

5. **Deploy**
```bash
git push heroku main
```

6. **Monitor logs**
```bash
heroku logs --tail
```

### Option 4: AWS Deployment

#### Using EC2

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance type: t3.small (minimum)
   - Security group: Allow 8501

2. **SSH into instance**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Setup application**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip python3-venv -y

# Clone repository
git clone https://github.com/yourusername/jobpilot-iq-x.git
cd jobpilot-iq-x

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

4. **Run with systemd service**

Create `/etc/systemd/system/jobpilot.service`:
```ini
[Unit]
Description=JobPilot IQ X Service
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/jobpilot-iq-x
Environment="PATH=/home/ubuntu/jobpilot-iq-x/venv/bin"
ExecStart=/home/ubuntu/jobpilot-iq-x/venv/bin/streamlit run app.py \
  --server.port=8501 \
  --server.address=0.0.0.0
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

5. **Enable and start service**
```bash
sudo systemctl daemon-reload
sudo systemctl enable jobpilot
sudo systemctl start jobpilot
```

6. **Setup reverse proxy (Nginx)**

Install Nginx:
```bash
sudo apt install nginx -y
```

Configure `/etc/nginx/sites-available/jobpilot`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/jobpilot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

7. **Setup SSL with Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

#### Using AWS Lightsail

1. Go to AWS Lightsail console
2. Click "Create instance"
3. Choose Ubuntu 22.04 LTS
4. Select plan (minimum: $3.50/month)
5. Follow steps 3-7 from EC2 section above

### Option 5: Google Cloud Run

#### Prerequisites
- Google Cloud Account
- gcloud CLI installed

#### Steps

1. **Create Dockerfile** (same as Docker section)

2. **Build and push to Google Container Registry**
```bash
# Set your GCP project
gcloud config set project YOUR_PROJECT_ID

# Build image
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/jobpilot-iq-x

# Or use Docker locally
docker tag jobpilot-iq-x:latest gcr.io/YOUR_PROJECT_ID/jobpilot-iq-x:latest
docker push gcr.io/YOUR_PROJECT_ID/jobpilot-iq-x:latest
```

3. **Deploy to Cloud Run**
```bash
gcloud run deploy jobpilot-iq-x \
  --image gcr.io/YOUR_PROJECT_ID/jobpilot-iq-x:latest \
  --platform managed \
  --region us-central1 \
  --memory 2Gi \
  --timeout 3600 \
  --allow-unauthenticated
```

4. **Get your URL**
```bash
gcloud run services describe jobpilot-iq-x --region us-central1
```

### Option 6: Azure App Service

#### Steps

1. **Create app service plan**
```bash
az group create --name jobpilot-rg --location eastus

az appservice plan create \
  --name jobpilot-plan \
  --resource-group jobpilot-rg \
  --sku B1 \
  --is-linux
```

2. **Create web app**
```bash
az webapp create \
  --resource-group jobpilot-rg \
  --plan jobpilot-plan \
  --name jobpilot-iq-x \
  --runtime "python|3.9"
```

3. **Deploy from GitHub**
```bash
az webapp deployment github-actions add \
  --resource-group jobpilot-rg \
  --name jobpilot-iq-x \
  --repo yourusername/jobpilot-iq-x \
  --branch main \
  --runtime python:3.9 \
  --build-provider github-actions
```

## Production Checklist

- [ ] Environment variables configured
- [ ] Database backups scheduled
- [ ] Logging setup complete
- [ ] Error monitoring (Sentry/DataDog)
- [ ] SSL certificate configured
- [ ] API rate limiting setup
- [ ] CORS configured
- [ ] Security headers added
- [ ] Monitoring and alerting
- [ ] Disaster recovery plan
- [ ] User documentation
- [ ] Support contact configured

## Performance Optimization

1. **Streamlit-specific**
   - Enable caching with @st.cache_data
   - Use columns for parallel rendering
   - Lazy load components

2. **Database**
   - Add indices on frequently queried columns
   - Implement query pagination
   - Regular maintenance (VACUUM, ANALYZE)

3. **Frontend**
   - Compress images
   - Minify CSS/JavaScript
   - Enable gzip compression

4. **Backend**
   - Cache knowledge base in memory
   - Use connection pooling
   - Implement request queuing

## Monitoring

1. **Application Metrics**
   - Page load time
   - API response time
   - Error rate
   - User sessions

2. **Infrastructure**
   - CPU usage
   - Memory usage
   - Disk space
   - Network traffic

3. **Tools**
   - Streamlit Cloud metrics (built-in)
   - DataDog
   - Sentry for error tracking
   - Google Analytics for user analytics

## Maintenance

1. **Weekly**
   - Check error logs
   - Monitor resource usage
   - Verify backups

2. **Monthly**
   - Update dependencies
   - Review security logs
   - Performance optimization

3. **Quarterly**
   - Knowledge base update
   - Database optimization
   - User feedback review

## Scaling Considerations

- **Users <100**: Single Streamlit Cloud instance sufficient
- **Users 100-1000**: Consider Heroku or small EC2 instance
- **Users 1000+**: Docker + multiple instances with load balancer
- **Users 10000+**: Kubernetes cluster with auto-scaling

## Support & Troubleshooting

### Common Issues

**Issue**: App not loading
```bash
streamlit run app.py --logger.level=debug
```

**Issue**: Database locked
```bash
# Check for processes using database
lsof | grep jobpilot.db

# Restart application
sudo systemctl restart jobpilot
```

**Issue**: Out of memory
- Increase instance memory
- Enable Streamlit caching
- Reduce knowledge base size

### Resources

- Streamlit Docs: https://docs.streamlit.io/
- Deployment Guide: https://docs.streamlit.io/library/get-started/installation
- Community: https://discuss.streamlit.io/

---

**Last Updated**: 2024
