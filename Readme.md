# pytestdemo 🧪🐍

A hands‑on demo repository showcasing **pytest fundamentals and best practices** using simple, easy‑to‑understand examples. This project is intended for beginners to intermediate Python testers who want to learn pytest through practical code.

---

## 📌 What This Repository Covers

This repo demonstrates commonly used pytest concepts with clean examples:

* ✅ Basic pytest test structure
* ✅ Assertions and test discovery
* ✅ Fixtures (setup & teardown)
* ✅ Parameterized tests
* ✅ Grouping tests using markers
* ✅ Running selective tests from CLI

---

## 🗂 Recommended Project Structure

```
pytestdemo/
│
├── tests/
│   ├── test_basic.py
│   ├── test_fixtures.py
│   ├── test_parametrize.py
│   └── test_markers.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ⚙️ Prerequisites

* Python 3.8+
* pip / virtualenv

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/sanj29/pytestdemo.git
cd pytestdemo

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Verbose output:

```bash
pytest -v
```

Run a specific file:

```bash
pytest tests/test_basic.py
```

Run tests by marker:

```bash
pytest -m smoke
```

---

## 🧪 Pytest Concepts Explained

### 🔹 Fixtures

Reusable setup/teardown logic using `@pytest.fixture`

### 🔹 Parametrization

Run the same test with multiple data sets using `@pytest.mark.parametrize`

### 🔹 Markers

Tag tests as `smoke`, `regression`, etc., and execute selectively

---

## 🧩 Configuration (`pytest.ini`)

Example configuration:

```ini
[pytest]
addopts = -v
markers =
    smoke: smoke tests
    regression: regression tests
```

---

## 🚀 CI/CD (Optional Enhancement)

You can integrate this repo with **GitHub Actions** to run tests automatically on every push or PR.

Suggested next step:

* Add a `.github/workflows/python-pytest.yml`
* Run `pytest` on each commit

---

## 🤝 Contributing

Contributions are welcome!

Ideas:

* Add advanced fixtures
* Include mocking examples
* Add API testing samples

---

## 📚 Learning Resources

* Pytest Documentation: [https://docs.pytest.org/](https://docs.pytest.org/)
* Python Testing Best Practices

---

## 👤 Author

**Sanjay Singh**
Staff Software QA Engineer | Automation & AI Enthusiast

---

⭐ If you find this repo useful, consider starring it!
