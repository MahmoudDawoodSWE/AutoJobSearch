# AutoJobSearch
Python tool for automating job applications. It sends personalized HTML emails to employers, including a profile picture, LinkedIn and GitHub links, and an attached CV. With optional delays between emails, AutoJobSearch helps streamline the application process and improve job search efficiency



# Email Sending Script

This Python script allows you to send HTML-styled emails to multiple recipients using Gmail's SMTP server.

## Features

- Send personalized HTML emails.
- Filter out duplicate email addresses.
- Add delays between emails to avoid overloading the server.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your system. Download it from [python.org](https://www.python.org/downloads/).
2. **Gmail Account**: A Gmail account with 2-Step Verification enabled.
3. **App-Specific Password**: Generate an app-specific password for your Gmail account.

## Setup Instructions

### Step 1: Configure Gmail Settings

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
   - Under "Signing in to Google," select "2-Step Verification" and follow the prompts to enable it.

2. **Generate an App-Specific Password**:
   - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
   - Under "Signing in to Google," select "App passwords."
   - Select "Mail" as the app and "Other" as the device, then click "Generate."
   - Copy the generated password; you'll need it for the script.

### Step 2: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/AutoJobSearch

cd AutoJobSearch

