# intake_demo
🚀 Immigration Workflow Automation Demo
AI-assisted client intake, document upload, and case summary automation for immigration law firms.
This project is a functional demo of a lightweight automation system designed for immigration lawyers. It collects client intake data, manages required document uploads, generates automatic summaries, and provides a clean dashboard for case tracking.

✨ Features
📝 Client Intake Form
Clean, structured intake designed for immigration cases
Organized sections: Personal Info, Case Type, Immigration Background, Logistics
Automatically generates an internal case summary
Supports bilingual intake (English & Spanish) — Pro Feature
📤 Client Document Upload
Upload multiple files (PDF, images, etc.)
Automatically tracks whether a case is None / Partial / Complete
Files stored locally in uploads/
📊 Attorney Dashboard
Shows all clients in a sortable table
Summaries, statuses, and document counts at a glance
"View Client" page displaying full case details + documents
📧 Automatic Email Notifications (Demo Only)
After document upload, the system prints a “fake email” to the console
Easy to swap in real email providers (SendGrid, Gmail API, Mailgun, etc.)
💬 AI Summary (Mocked, but fully pluggable)
Generates a human-like summary of the client case
Can be upgraded easily to real OpenAI API calls
🔐 Simple SQLite Database
All clients and documents stored in demo.db
SQLAlchemy ORM models for easy extension
🗂️ Project Structure
immigration_demo/
│
├── app.py                # Main Flask application
├── demo.db               # SQLite database (ignored in git)
├── .gitignore            # Git ignore file
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── intake.html
│   ├── upload.html
│   ├── success.html
│   ├── dashboard.html
│   └── client_detail.html
│
└── uploads/              # Uploaded documents (ignored in git)
🛠️ Installation
Clone the repository:
git clone https://github.com/YOURNAME/immigration-demo.git
cd immigration-demo
Create a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install flask flask_sqlalchemy
Run the server:
python app.py
Visit the app:
http://127.0.0.1:5000
🌐 Multi-Language Intake (Pro Feature)
The intake form includes a language dropdown:
English (?lang=en)
Español (?lang=es)
Labels are stored in a Python dictionary, making it easy to add more languages later (Somali, Vietnamese, Russian, etc.).
🧩 Roadmap
Near-term
Add real OpenAI summary generation
Add authentication for attorneys
Add downloadable PDF client dossiers
Add mobile-optimized intake
Mid-term
Cloud file storage (AWS S3)
Email + SMS notifications
Calendar integrations (Calendly / Google Calendar)
Long-term
Client portal
Firm-wide case analytics
Full SaaS product launch
🤝 Contributing
Pull requests are welcome.
If you find bugs or want features, open an issue or message the repository owner.
📄 License
This project is for portfolio/demo use only and not intended for production without additional security, encryption, and compliance features.
👤 Author
Theron Hamlin
AI Automation Engineer
Immigration Workflow & Document Automation
GitHub: https://github.com/YOURNAME
Email: your.email@example.com






ChatGPT can make mistakes. Check important info.
