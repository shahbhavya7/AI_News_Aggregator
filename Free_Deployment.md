# Free Deployment Guide (No Credit Card Required)

This project can be deployed completely for free without providing credit card details using **GitHub Actions**. This replaces the Render Blueprint.

## Option 1: GitHub Actions (Recommended)

Run the news aggregator automatically in the cloud every day.

### 1. Configure Secrets

1. Go to your GitHub Repository.
2. Navigate to **Settings** > **Secrets and variables** > **Actions**.
3. Click **New repository secret** and add the following:
   - `OPENAI_API_KEY`: Your OpenAI key.
   - `MY_EMAIL`: The destination email address.
   - `APP_PASSWORD`: Your Gmail App Password.

### 2. Enable Permissions (Crucial!)

1. Go to **Settings** > **Actions** > **General**.
2. Scroll to "Workflow permissions".
3. Select **Read and write permissions**.
4. Click **Save**.
   _(This allows the database to be saved back to the repository so you don't lose data)_.

### 3. Activate

The workflow is already created in `.github/workflows/daily_digest.yml`.

- By default, it runs daily at **8:00 AM UTC**.
- To test it immediately:
  1. Go to the **Actions** tab in GitHub.
  2. Select **Daily AI News Digest**.
  3. Click **Run workflow**.

---

## Option 2: Run Locally (Windows Task Scheduler)

You can run the script on your own computer.

### 1. Setup

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
python -m app.database.create_tables
```

### 2. Create `run_daily.bat`

Create a file named `run_daily.bat` in the project folder:

```batch
@echo off
cd /d "%~dp0"
call venv\Scripts\activate
set OPENAI_API_KEY=your_key_here
set MY_EMAIL=your_email@gmail.com
set APP_PASSWORD=your_app_password
set USE_SQLITE=true
python main.py
```

_(Replace secrets with your actual values or ensure they are set in your system environment)_

### 3. Schedule it

1. Press `Win + R`, type `taskschd.msc`, press Enter.
2. Click **Create Basic Task**.
3. Name: "AI News Aggregator".
4. Trigger: **Daily**.
5. Action: **Start a program**.
6. Program/script: Browse and select your `run_daily.bat` file.
7. Finish.
