from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

def send_email(to_email: str, subject: str, body: str):
    """
    DEMO-ONLY email sender.
    For now this just prints to the console so you can show it in a demo.
    Later, you can replace this with real SMTP / SendGrid / etc.
    """
    print("\n" + "=" * 60)
    print("EMAIL SENT (DEMO ONLY)")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print("-" * 60)
    print(body)
    print("=" * 60 + "\n")


app = Flask(__name__)

# --- Config ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "demo.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

db = SQLAlchemy(app)


# --- Models ---

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    full_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    country_citizenship = db.Column(db.String(200))
    current_city_country = db.Column(db.String(200))
    dob = db.Column(db.String(50))

    case_type = db.Column(db.String(200))
    in_us = db.Column(db.String(20))
    current_status = db.Column(db.String(200))
    prior_applications = db.Column(db.String(500))

    arrest_history = db.Column(db.String(20))
    deported = db.Column(db.String(20))
    overstayed = db.Column(db.String(20))
    background_notes = db.Column(db.Text)

    urgency = db.Column(db.String(50))
    communication = db.Column(db.String(50))
    referral_source = db.Column(db.String(200))

    summary = db.Column(db.Text)  # "AI-style" summary text

    docs_requested = db.Column(db.Boolean, default=True)
    docs_received = db.Column(db.String(50), default="None")  # None / Partial / Complete
    status = db.Column(db.String(100), default="New Lead")    # pipeline status
    next_action = db.Column(db.String(200), default="Review intake")
    notes = db.Column(db.Text)


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    filename = db.Column(db.String(300))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship("Client", backref=db.backref("documents", lazy=True))


# --- Utility: fake "AI" summary for now ---

def generate_case_summary(client: Client) -> str:
    """
    Placeholder for an AI summary.
    In production you’d call OpenAI’s API here.
    """
    lines = [
        f"Client: {client.full_name} ({client.email}, {client.phone})",
        f"Citizenship: {client.country_citizenship}",
        f"Location: {client.current_city_country}",
        f"Case type: {client.case_type}",
        f"In U.S.: {client.in_us}, Current status: {client.current_status}",
    ]

    risk_flags = []
    if client.arrest_history == "Yes":
        risk_flags.append("Possible criminal history")
    if client.deported == "Yes":
        risk_flags.append("Prior deportation/removal")
    if client.overstayed == "Yes":
        risk_flags.append("Possible overstay issues")

    if risk_flags:
        lines.append("Risk flags: " + ", ".join(risk_flags))
    else:
        lines.append("Risk flags: none reported")

    if client.prior_applications:
        lines.append(f"Previous applications: {client.prior_applications}")

    if client.background_notes:
        lines.append(f"Client notes: {client.background_notes[:200]}...")

    lines.append(f"Urgency: {client.urgency}")
    lines.append(f"Preferred communication: {client.communication}")

    return "\n".join(lines)


# --- Routes ---

@app.route("/")
def index():
    return render_template("intake.html")


@app.route("/intake", methods=["GET", "POST"])
def intake():
    if request.method == "POST":
        # Grab form data
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        country_citizenship = request.form.get("country_citizenship")
        current_city_country = request.form.get("current_city_country")
        dob = request.form.get("dob")

        case_type = request.form.get("case_type")
        in_us = request.form.get("in_us")
        current_status = request.form.get("current_status")
        prior_applications = request.form.get("prior_applications")

        arrest_history = request.form.get("arrest_history")
        deported = request.form.get("deported")
        overstayed = request.form.get("overstayed")
        background_notes = request.form.get("background_notes")

        urgency = request.form.get("urgency")
        communication = request.form.get("communication")
        referral_source = request.form.get("referral_source")

        client = Client(
            full_name=full_name,
            email=email,
            phone=phone,
            country_citizenship=country_citizenship,
            current_city_country=current_city_country,
            dob=dob,
            case_type=case_type,
            in_us=in_us,
            current_status=current_status,
            prior_applications=prior_applications,
            arrest_history=arrest_history,
            deported=deported,
            overstayed=overstayed,
            background_notes=background_notes,
            urgency=urgency,
            communication=communication,
            referral_source=referral_source,
        )

        # Generate fake AI summary
        client.summary = generate_case_summary(client)

        db.session.add(client)
        db.session.commit()

        return redirect(url_for("upload_docs", client_id=client.id))

    return render_template("intake.html")


@app.route("/upload/<int:client_id>", methods=["GET", "POST"])
def upload_docs(client_id):
    client = Client.query.get_or_404(client_id)

    if request.method == "POST":
        files = request.files.getlist("documents")
        count = 0
        for f in files:
            if f and f.filename:
                safe_name = f"{client.id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{f.filename}"
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], safe_name)
                f.save(filepath)
                doc = Document(client_id=client.id, filename=safe_name)
                db.session.add(doc)
                count += 1

        if count > 0:
            # simple logic for demo: if client has any docs, mark as Partial
            client.docs_received = "Partial"
            client.status = "Waiting on additional documents"
            client.next_action = "Review documents when complete"

        db.session.commit()

        # --- DEMO EMAIL: notify client that docs were received ---
        if client.email:
            subject = "We received your immigration documents"
            body_lines = [
                f"Hi {client.full_name},",
                "",
                "Thank you for submitting your documents. We have received them in our secure system.",
                "",
                "Current status:",
                f"  - Documents received: {client.docs_received}",
                f"  - Case type: {client.case_type or 'Not specified'}",
                "",
                "If anything else is needed, our office will reach out with next steps.",
                "",
                "Best regards,",
                "Your Immigration Law Office (Demo)"
            ]
            send_email(client.email, subject, "\n".join(body_lines))

        # After upload, go straight to the dashboard so the lawyer can see the update
        return redirect(url_for("dashboard"))

    return render_template("upload_docs.html", client=client)


@app.route("/dashboard")
def dashboard():
    # newest first
    clients = Client.query.order_by(Client.created_at.desc()).all()
    return render_template("dashboard.html", clients=clients)

@app.route("/client/<int:client_id>")
def client_detail(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template("client_detail.html", client=client)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
