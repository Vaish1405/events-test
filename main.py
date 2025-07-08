from jinja2 import Environment, FileSystemLoader
import os

# Dummy event data
events = [
    {
        "title": "Matador Morning Bash",
        "photo": "lib.png",
        "date": "JUL 10",
        "timeSt": "09:00 AM",
        "timeEn": "11:00 AM",
        "location": "CSUN Library Lawn",
        "url": "https://example.com/event1"
    },
    {
        "title": "Tech Career Fair",
        "photo": "usu.png",
        "date": "JUL 12",
        "timeSt": "12:00 PM",
        "timeEn": "04:00 PM",
        "location": "USU Grand Salon",
        "url": "https://example.com/event2"
    },
    {
        "title": "AI in Education Panel",
        "photo": "default.png",
        "date": "JUL 15",
        "timeSt": "03:00 PM",
        "timeEn": "04:30 PM",
        "location": "Online",
        "url": "https://example.com/event3"
    },
    {
        "title": "Clubs & Orgs Info Night",
        "photo": "lib.png",
        "date": "JUL 17",
        "timeSt": "05:00 PM",
        "timeEn": "06:30 PM",
        "location": "Oviatt Lawn",
        "url": "https://example.com/event4"
    },
    {
        "title": "Sustainability Meetup",
        "photo": "usu.png",
        "date": "JUL 20",
        "timeSt": "10:00 AM",
        "timeEn": "11:30 AM",
        "location": "CSUN Sustainability Center",
        "url": "https://example.com/event5"
    }
]

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('test.html')

# Render the HTML
rendered_html = template.render(e=events, url="https://itdocs.csun.edu/mobile-redesign/")

# Output file
output_path = "test_events_output.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

print(f"✅ HTML generated and saved as {output_path}")
