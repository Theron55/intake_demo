# Workflow Automation Demo

AI-assisted client intake, document upload, and case summary automation for immigration law firms.

This project is a functional demo of a lightweight automation system designed for immigration attorneys. It collects client intake data, manages uploaded documents, generates automatic summaries, and provides a clean internal dashboard for case tracking.

---

## Features

### Client Intake Form

* Clean, structured intake designed specifically for immigration cases
* Organized sections: Personal Info, Case Type, Immigration Background, Logistics
* Automatically generates an internal case summary
* Supports bilingual intake (English & Spanish) — Pro Feature

### Document Upload

* Clients can upload multiple files (PDF, JPG, PNG, etc.)
* Case status updates automatically (None / Partial / Complete)
* Files stored locally in the `uploads/` folder

### Attorney Dashboard

* Displays all clients with key details
* Shows document count, summary preview, and submission date
* “View Client” page for full case detail and document list

### Automatic Email Notifications (Demo Only)

* Prints a “fake email” in the backend console after document upload
* Can be replaced with real email providers: SendGrid, Gmail API, Mailgun, etc.

### AI Summary (Mocked but Upgradable)

* Generates human-like case summaries based on form inputs
* Ready for OpenAI API integration

### SQLite Database via SQLAlchemy

* All client data stored in `demo.db`
* ORM models allow easy expansion

---

## Project Structure

```
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
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOURNAME/immigration-demo.git
cd immigration-demo
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask flask_sqlalchemy
```

Run the server:

```bash
python app.py
```

Open the app in your browser:

```
http://127.0.0.1:5000
```

---

## Multi-Language Intake (Pro Feature)

The intake form includes a language dropdown:

* English (default)
* Español (Spanish)

Labels and section text are stored in a Python dictionary, allowing easy expansion into additional languages such as Somali, Vietnamese, Mandarin, Russian, etc.

---

## Roadmap

### Short Term

* Real OpenAI-powered summaries
* Attorney login system
* Mobile-friendly intake templates

### Medium Term

* Cloud document storage (AWS S3)
* Email and SMS notifications
* Calendar integration (Google Calendar / Calendly)

### Long Term

* Client portal
* Analytics dashboard
* Full SaaS deployment

---

## Contributing

Pull requests are welcome.
For bugs or feature requests, please open an issue on GitHub.

---

## License

This project is provided for demonstration and portfolio purposes only and is **not production-ready**. A real deployment would require additional security, authentication, encryption, and compliance measures.

---

## Author

**Theron Hamlin**
AI Automation Developer — Immigration Workflow Systems
GitHub: [https://github.com/YOURNAME](https://github.com/YOURNAME)
Email: [your.email@example.com](mailto:your.email@example.com)

---

If you want, I can:

* Add screenshots
* Add animated GIF of the demo flow
* Add OpenAI integration setup
* Add deployment instructions (Netlify, Render, Fly.io)

Just tell me.
