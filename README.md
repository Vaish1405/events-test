# 🧪 Accessible Events Carousel (Temporary Test Repo)

This temporary repository is used to develop and test **ARIA-compliant accessibility fixes** for the events carousel component.

Once the accessibility updates are finalized and approved, this implementation will be migrated to the official repo.

---

## ✨ What's New?

- Fully integrated **WAI-ARIA carousel pattern** based on the official [ARIA Practices Guide](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/)
- On **arrow key navigation**, only the **event title** is announced by screen readers
- On **tabbing into an event card**, the **full event details** are read aloud

---

## ▶️ Generate the demo HTML

Prereqs: Python 3.9+.

1. Install dependencies
   
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Generate HTML

   ```bash
   python main.py
   ```

This writes `test_events_output.html` to the project root, using `templates/test.html` and the sample events in `main.py`.

Notes:
- The Jinja environment uses autoescape for HTML/XML.
- The template expects an absolute `url` prefix for images; update `url` in `main.py` if your asset host changes.

