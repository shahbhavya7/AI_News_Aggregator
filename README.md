# 🤖 Global Digest

<div align="center">
  
  [![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini%20AI-4285F4?style=for-the-badge&logo=google)](https://ai.google.dev)
  [![RAG Pipeline](https://img.shields.io/badge/Technology-AI%20Agents-00D9FF?style=for-the-badge&logo=databricks)](https://en.wikipedia.org/wiki/Intelligent_agent)
  [![Neon DB](https://img.shields.io/badge/Database-Neon%20DB-00E699?style=for-the-badge&logo=postgresql)](https://neon.tech)
  [![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)


_Your personalized AI news digest - scraped, curated, and delivered daily!_

</div>

## 🌟 Features

<div align="center">
  
  | 🔍 **Smart Scraping** | 🤖 **AI Curation** | 📧 **Email Digest** |
  |:---------------------:|:------------------:|:-------------------:|
  | Multi-source content aggregation | Personalized ranking algorithm | Beautiful HTML emails |
  | YouTube, OpenAI, Anthropic | Relevance scoring (0-10) | Daily automated delivery |
  
  | 📊 **Database Storage** | 🎯 **User Profiles** | ⚡ **Automated Pipeline** |
  |:-----------------------:|:--------------------:|:------------------------:|
  | Neon DB (Serverless Postgres) | Customizable interests | Scheduled daily runs |
  | Article deduplication | Expertise-based filtering | End-to-end automation |
  
</div>

## ✨ What makes Global Digest special?

- **🤖 Multi-Agent Architecture** - Specialized AI agents for digesting, curating, and email generation
- **🔍 Multi-Source Scraping** - Aggregates content from YouTube, OpenAI Blog, and Anthropic News
- **🎯 Personalized Curation** - Ranks articles based on your specific interests and expertise level
- **📧 Beautiful Email Digests** - HTML-formatted emails with your top 10 most relevant articles
- **💾 Smart Storage** - Neon DB serverless Postgres with deduplication and history tracking
- **⚡ Automated Pipeline** - Fully automated daily workflow from scraping to email delivery
- **🧠 Gemini-Powered** - Leverages Google's Gemini 2.5 Flash for fast, accurate AI processing
- **📺 Transcript Processing** - Extracts and analyzes YouTube video transcripts automatically
- **📄 Markdown Extraction** - Converts web articles to clean markdown for better analysis

## 🛠️ Tech Stack

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Google AI](https://img.shields.io/badge/Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
  ![Neon DB](https://img.shields.io/badge/Neon%20DB-00E699?style=for-the-badge&logo=postgresql&logoColor=white)
  ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
  ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
  
</div>

### Core Technologies

- **AI Model**: Google Gemini 2.5 Flash (Fast, structured output, cost-effective)
- **Database**: Neon DB (Serverless Postgres) with SQLAlchemy ORM
- **Data Validation**: Pydantic (Type-safe models and structured outputs)
- **Web Scraping**: Feedparser, BeautifulSoup, Requests
- **Content Processing**: Docling (Web to Markdown), YouTube Transcript API
- **Email Delivery**: SMTP with HTML/Markdown rendering

## 💡 How It Works

### System Architecture

```mermaid
graph TD
    A[🔍 Scrapers] --> B[📺 YouTube Videos]
    A --> C[📰 OpenAI Blog]
    A --> D[🧠 Anthropic News]

    B --> E[💾 Neon DB Database]
    C --> E
    D --> E

    E --> F[📝 Process Transcripts]
    E --> G[📄 Process Markdown]

    F --> H[🤖 Digest Agent]
    G --> H

    H --> I[💾 Store Digests]

    I --> J[🎯 Curator Agent]

    J --> K[📊 Ranked Articles]

    K --> L[✉️ Email Agent]

    L --> M[📧 HTML Email Digest]

    style A fill:#4ECDC4,stroke:#333,stroke-width:2px,color:#fff
    style H fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#45B7D1,stroke:#333,stroke-width:2px,color:#fff
    style L fill:#96CEB4,stroke:#333,stroke-width:2px,color:#fff
    style M fill:#F7DC6F,stroke:#333,stroke-width:2px,color:#333
```

### Processing Pipeline

1. **🔍 Content Scraping** (30-60 seconds)
   - YouTube: Fetches recent videos from configured channels via RSS feeds
   - OpenAI: Scrapes blog articles from RSS feed
   - Anthropic: Scrapes news, research, and engineering posts from RSS feeds

2. **💾 Database Storage** (Instant)
   - Deduplicates content based on unique IDs
   - Stores metadata (title, URL, published date, description)
   - Tracks processing status for each article

3. **📝 Content Processing** (2-5 minutes)
   - **Transcripts**: Fetches YouTube video transcripts using YouTube Transcript API
   - **Markdown**: Converts Anthropic web articles to clean markdown using Docling
   - Handles unavailable content gracefully

4. **🤖 Digest Generation** (5-15 minutes, rate-limited)
   - Gemini AI creates concise summaries for each article
   - Generates compelling titles (5-10 words)
   - Produces 2-3 sentence summaries highlighting key insights
   - Rate limited to 15 seconds between requests (free tier compliance)

5. **🎯 Personalized Curation** (30-60 seconds)
   - Curator Agent ranks all digests based on your profile
   - Assigns relevance scores (0.0-10.0) to each article
   - Provides reasoning for each ranking decision
   - Sorts articles from most to least relevant

6. **✉️ Email Generation** (15-30 seconds)
   - Email Agent creates personalized introduction
   - Formats top N articles (default: 10) with summaries and links
   - Generates both plain text and beautiful HTML versions

7. **📧 Email Delivery** (Instant)
   - Sends digest via Gmail SMTP
   - HTML email with responsive design
   - Includes read-more links to original content

## 📧 Email Digest Format

Your daily email will look like this:

```
Subject: Daily AI News Digest - January 26, 2026

Hey Bhavya, here is your daily digest of AI news for January 26, 2026.

Today's top articles cover breakthrough advances in multimodal AI,
new LLM architectures, and practical RAG implementations. You'll
find deep technical insights aligned with your expertise in AI systems.

---

## Revolutionary Approach to Vision-Language Models

OpenAI's latest research introduces a novel architecture that
significantly improves image understanding in LLMs. The technique
shows promising results on standard benchmarks and could transform
multimodal applications.

[Read more →](https://openai.com/...)

---

## Scaling RAG Systems to Production

A comprehensive guide to deploying RAG pipelines at scale, covering
vector database optimization, chunking strategies, and real-world
performance considerations.

[Read more →](https://anthropic.com/...)

---

[... 8 more articles ...]
```

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.9 or higher
python --version

# pip package manager
pip --version

# Neon DB account (free tier available)
# Get started at https://neon.tech
```

### Installation

**Clone the repository**

```bash
git clone https://github.com/yourusername/ai-news-aggregator.git
cd ai-news-aggregator
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Set up environment variables**

```bash
# Create a .env file in the root directory
# Add your credentials:

# Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash

# Email configuration (Gmail)
MY_EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password

# Database configuration (Neon DB)
DATABASE_URL=postgresql://user:password@host.neon.tech:5432/dbname?sslmode=require

# Optional: YouTube proxy (for transcript fetching)
WEBSHARE_USERNAME=your_proxy_username
WEBSHARE_PASSWORD=your_proxy_password
```

**Get your API keys:**

- Gemini API: [Google AI Studio](https://ai.google.dev)
- Gmail App Password: [Google Account Settings](https://myaccount.google.com/apppasswords)
- Neon DB Connection String: [Neon Console](https://console.neon.tech)

**Set up the database**

```bash
# Create tables
python app/database/create_tables.py

# Verify connection
python app/database/check_connection.py
```

**Configure your profile**

Edit `app/profiles/user_profile.py` to customize your interests:

```python
USER_PROFILE = {
    "name": "Your Name",
    "background": "Your background and expertise",
    "interests": [
        "Large Language Models",
        "AI Safety",
        # Add your interests...
    ]
}
```

**Run the pipeline**

```bash
# Run daily pipeline (last 24 hours, top 10 articles)
python main.py

# Or customize hours and article count
python main.py 48 15  # Last 48 hours, top 15 articles
```

## 🤝 Contributing

Contributions are welcome to enhance the Global Digest!

1. **🍴 Fork the repository**

2. **🌟 Create your feature branch**

   ```bash
   git checkout -b feature/MultiLanguageSupport
   ```

3. **💻 Commit your changes**

   ```bash
   git commit -m 'Add support for non-English sources'
   ```

4. **🚀 Push to the branch**

   ```bash
   git push origin feature/MultiLanguageSupport
   ```

5. **📬 Open a Pull Request**

## 🔒 Privacy & Security

- **Local Processing**: Content scraping and processing happens locally
- **API Communication**: Only summaries sent to Gemini API, not full articles
- **Database Security**: Neon DB uses SSL by default, automated backups, and secure connections
- **Email Security**: Gmail App Passwords prevent exposing main credentials
- **Environment Variables**: Sensitive data stored securely in `.env` file
- **No Data Sharing**: Your profile and preferences stay private

## 📮 Future Roadmap

- 🌍 **Multi-Language Support** - Process articles in multiple languages
- 📊 **Analytics Dashboard** - Track reading patterns and topic trends
- 🔔 **Slack/Discord Integration** - Deliver digests to team channels
- 🎯 **Topic Clustering** - Group related articles automatically
- 📱 **Mobile App** - iOS/Android apps for on-the-go reading
- 🤝 **Collaborative Filtering** - Learn from similar user preferences
- 🔍 **Full-Text Search** - Search through your digest history
- 📈 **Trending Topics** - Identify emerging themes across sources
- 🎨 **Custom Templates** - User-defined email formats
- ⚡ **Real-Time Updates** - Push notifications for breaking news

---

<div align="center">
  
  **Built by AI enthusiasts, for AI enthusiasts**
  
  *Stay informed, stay ahead*
  
  ⭐ Star this repo if you find it helpful!
  
</div>

---

_Last updated: January 2026_
