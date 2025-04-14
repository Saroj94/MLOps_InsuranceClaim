# 🧠 Claim Prediction ML Pipeline - End-to-End ML & MLOps Project

Welcome to the **Claim Prediction ML Pipeline**, an end-to-end machine learning project that showcases the implementation of a full MLOps lifecycle, integrating robust backend engineering, data pipeline automation, model training, evaluation, and seamless deployment using AWS services and CI/CD workflows.

## 🚀 Project Highlights

- 📦 **Modular Code Architecture** with reusable components
- 📊 **MongoDB Atlas** for cloud-based data storage
- 🧹 **Data Ingestion, Validation & Transformation Pipelines**
- 🤖 **Custom Model Training & Evaluation Logic**
- ☁️ **AWS Integration (S3, IAM, EC2, ECR)**
- 🐳 **Docker Containerization**
- ⚙️ **CI/CD Workflow** via GitHub Actions + Self-Hosted Runner on EC2
- 🌐 **FastAPI Web App Deployment** (port 5000)

## 🛠️ Project Setup

### 1. 🔧 Project Initialization

# Run project template generator
    python template.py

## 2. 📚 Package Structure & Setup
- Add local packages to setup.py and pyproject.toml

## 3. 🐍 Virtual Environment
    python -m venv inclaim
    source inclaim/bin/activate
    pip install -r requirements.txt
    pip list # Ensure local packages are installed

## 📦 MongoDB Atlas Setup (Cloud NoSQL)
    1. Sign up & create MongoDB Atlas cluster (M4 - free tier)
    2. Create DB user & allow access from anywhere (0.0.0.0/0)
    3. Copy connection string for Python (v3.6+)
    4. Add mongoDB_demo.ipynb to notebook/ and push sample data to MongoDB
    5. Confirm upload via MongoDB Atlas → Database → Browse Collection

## 🧾 Logging, Exception Handling & EDA
- Custom logger.py and exception.py tested on demo.py
- Initial Exploratory Data Analysis and Feature Engineering notebooks provided

## 🛠️ Data Engineering Workflow
## 🔄 Data Ingestion
- Define MongoDB connection logic in configuration.mongo_db_connections.py
- Implement data fetch and transformation in data_access.proj1_data
- Structure config and artifact classes in:
- entity/config_entity.py
- entity/artifact_entity.py
- Implement component in components.data_ingestion.py
- Run end-to-end from demo.py

## 🌐 MongoDB URL Setup
# Bash
    export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"
    echo $MONGODB_URL

## ✅ Data Validation & Transformation
- Define schema in config/schema.yaml
- Add validation logic in components/data_validation.py
- Add transformation logic and estimator in components/data_transformation.py

## 🤖 Model Training
- Implement training logic in components/model_trainer.py
- Add model wrapper to entity/estimator.py

## ☁️ AWS Integration (Model Evaluation & Deployment)
### AWS Setup
- Create IAM user (firstproj) with AdminAccess
- Generate & download access keys
- Export as environment variables:

    export AWS_ACCESS_KEY_ID="your_key"
    export AWS_SECRET_ACCESS_KEY="your_secret"

## AWS S3 Configuration
- Create bucket claimproj (Region: eu-north-1a)
- Set S3 access in constants/__init__.py
- Implement logic in:
- src/aws_storage
- entity/s3_estimator.py
- configuration/aws_connection.py

## 📈 Model Evaluation & Pusher
- Compare models using threshold score
- Push best model to S3
- Setup prediction service using FastAPI/Flask (app.py)

## 🐳 Docker + 🛠️ CI/CD Pipeline
- Create Dockerfile and .dockerignore

## GitHub Actions + EC2 Self-Hosted Runner
1. Connect EC2 to GitHub via runner
2. Setup GitHub Secrets:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
3. Create ECR repository (claimproject)
4. Configure .github/workflows/aws.yaml

## 🚢 Deployment
- Run pipeline → Docker builds & pushes to ECR
- EC2 instance serves model on port 5000
- Add 5000 port in AWS security group for public access

# Access App
- http://<your-ec2-public-ip>:5000
- Sorry i remove the instance from EC2 instance for docker image.

## 🔁 Re-Train Model
- Use /training route to trigger model retraining on new data.

## 📍 Conclusion
This project reflects production-ready ML pipeline practices:
- Real-world data integration
- Scalable architecture
- CI/CD automation
- Cloud-first deployment mindset

## 👨‍💻 Author

- Saroj: [Data Analyst | ML Engineer]
- Feel free to connect on LinkedIn

