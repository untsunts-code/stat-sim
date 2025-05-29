# 📊 Stat-Sim

**Hypothesis Testing Simulator in Python**  
Simulate false positives under the null hypothesis using statistical tests and visualize the p-value distribution. This project is built with future reuse in mind—clean functions, modular design, and full documentation.

---

## 🚀 Project Overview

This tool runs thousands of independent t-tests on random samples drawn from the same distribution to simulate Type I errors (false positives). It helps visualize how often p-values fall below the standard 0.05 threshold under the null hypothesis.

---

## 🧱 Features

- Generate and compare random samples
- Run independent t-tests
- Collect and analyze p-values
- Plot distribution of p-values
- Modular functions, reusable for future services

---

## 📦 Tech Stack

- Python 3.10+
- `numpy`
- `scipy`
- `matplotlib`
- `seaborn`

---

## 📂 Project Structure

stat-sim/
├── src/
│   ├── simulate.py      # Core simulation logic
│   ├── plot.py          # Plotting utilities
│   └── __init__.py
├── tests/
│   └── test_simulate.py
├── notebooks/
│   └── exploration.ipynb
├── requirements.txt
├── README.md
└── main.py

---

## 🧪 How to Run
# Install dependencies
pip install -r requirements.txt

# Run the main simulation
python main.py

---

📈 Sample Output
(To be added later): Distribution plot of 10,000 p-values, showing frequency below 0.05 threshold.

---

📘 License
MIT License — feel free to use, fork, and contribute.

---

🧠 Author
Made with ❤️ by untsunts-code, guided by The Python Architect Trainer.

---
