from flask import Flask, render_template

app = Flask(__name__)

# Sample Data for Agency Showcase
SERVICES = [
    {
        "icon": "🎨",
        "title": "UI/UX Product Design",
        "desc": "High-fidelity mobile and web application interfaces designed for seamless user engagement and conversion."
    },
    {
        "icon": "⚡",
        "title": "Modern Web Engineering",
        "desc": "Blazing fast Python & JavaScript web apps built with modular architectures and responsive styling."
    },
    {
        "icon": "🚀",
        "title": "Brand Systems & Strategy",
        "desc": "Cohesive brand identities, visual style guides, and positioning crafted to make your business stand out."
    }
]

PORTFOLIO = [
    {
        "key": "web",
        "icon": "📊",
        "category": "Web Application",
        "title": "FinTech Dashboard Suite",
        "desc": "Real-time analytics portal with responsive data visualization and modular design components."
    },
    {
        "key": "design",
        "icon": "💎",
        "category": "UI/UX Design",
        "title": "Luxe E-Commerce Experience",
        "desc": "Custom digital storefront with fluid animations, custom checkout flow, and glassmorphism UI."
    },
    {
        "key": "branding",
        "icon": "⚡",
        "category": "Branding",
        "title": "Vortex AI Identity & System",
        "desc": "Complete brand overhaul including dynamic logo design, typography guidelines, and marketing assets."
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Apex Studio · Digital Product & Design Agency",
        services=SERVICES,
        portfolio=PORTFOLIO
    )

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html", title="404 Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html", title="500 Internal Error"), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
