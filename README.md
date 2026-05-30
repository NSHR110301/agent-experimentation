# Agentic Email Classifier & Labeller

An AI-powered automation agent that uses Large Language Models (LLMs) and the Gmail API to contextually analyze, categorize, and 
label incoming emails. Unlike rigid keyword filters, this agent understands natural language rules—allowing you to define a label 
like "Interviews" using descriptive phrases, which the agent then maps accurately to incoming scheduling or HR messages.

## 🛠️ Setup & Local Authentication Guide

Because this is a portfolio showcase project, the Google OAuth screen is in "Testing Mode." To run this application locally, 
you will need to plug in your own Google API credentials.

### Prerequisites
* Python 3.10+ (or Node.js 18+)
* An OpenAI API Key (or your chosen LLM provider)

### Step 1: Google Cloud Console Configuration
1. Navigate to the [Google Cloud Console](https://google.com).
2. Create a new project named `email-agent-classifier`.
3. Go to **API & Services > Library**, search for **Gmail API**, and click **Enable**.
4. Configure the **OAuth Consent Screen**:
   * Select **External** user type.
   * Add your own email to the **Test Users** list (critical, or Google will block you).
5. Generate Credentials:
   * Go to **Credentials > Create Credentials > OAuth Client ID**.
   * Select **Desktop App** (or *Web Application* if using a web framework).
   * Download the resulting client secrets file and save it in your project root as `credentials.json`.

### Step 2: Project Installation
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd agent-experimentation
   git checkout feature-email-seg-v2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize your environment variables:
   ```bash
   cp .env.example .env
   ```

### Step 3: Run the Agent
On the first execution, a browser window will pop up asking you to log into your Gmail account. 
Click through the "Advanced > Proceed anyway (unsafe)" warning to grant the agent permission to read and label your test emails.

```bash
python main.py
```
<img width="1404" height="655" alt="Screenshot 2026-05-30 151527" src="https://github.com/user-attachments/assets/e8e08230-2eda-4a96-b517-11059fdefad1" />
