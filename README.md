# MLOps Agile Demo — Iris Flower Classification

## Aim
Demonstrate Agile methodology and the Scrum framework through a small MLOps project that trains and evaluates a Decision Tree model for Iris flower classification.

## Product Goal
Develop an Iris Flower Classification model with at least 95% accuracy.

## Project Structure
```text
MLOps_Agile_Demo/
├── data/
├── docs/
│   ├── Daily_Scrum.md
│   ├── Product_Backlog.md
│   ├── Product_Backlog.xlsx
│   ├── Scrum_Team.md
│   ├── Sprint_Planning.md
│   ├── Sprint_Review.md
│   └── Sprint_Retrospective.md
├── models/
├── reports/
├── src/
│   └── iris_demo.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements
- Python 3.10 or later recommended
- pip

## Run on Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/iris_demo.py
```

If PowerShell blocks virtual-environment activation, run:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/iris_demo.py
```

## Run on macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/iris_demo.py
```

## Outputs
The script trains and evaluates a Decision Tree classifier and writes:
- `models/iris_decision_tree.joblib` — trained model
- `reports/accuracy_report.txt` — accuracy and classification metrics

The Iris dataset is loaded from scikit-learn, so a separate manual download is not required. The dataset is split into training and testing subsets with an 80:20 ratio and `random_state=42` for reproducibility.

## Agile/Scrum Activities
See the `docs/` folder for Scrum roles, Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, and Sprint Retrospective.

## Result
The Agile and Scrum workflow is demonstrated by producing a working Iris classification model, evaluation report, and saved model artifact. Record the actual accuracy printed by your run in your submission.
