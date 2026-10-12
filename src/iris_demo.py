from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
MODEL_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    model_path = MODEL_DIR / "iris_decision_tree.joblib"
    report_path = REPORT_DIR / "accuracy_report.txt"
    joblib.dump(model, model_path)

    report = (
        "IRIS FLOWER CLASSIFICATION — ACCURACY REPORT\n"
        "============================================\n"
        f"Dataset samples: {len(X)}\n"
        f"Training samples: {len(X_train)}\n"
        f"Testing samples: {len(X_test)}\n"
        "Algorithm: Decision Tree Classifier\n"
        "Test size: 20%\n"
        "Random state: 42\n"
        f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)\n\n"
        "Confusion Matrix:\n"
        f"{confusion_matrix(y_test, predictions)}\n\n"
        "Classification Report:\n"
        f"{classification_report(y_test, predictions, target_names=iris.target_names)}"
    )
    report_path.write_text(report, encoding="utf-8")

    print("Iris Flower Classification completed.")
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print(f"Saved model: {model_path.relative_to(ROOT)}")
    print(f"Saved report: {report_path.relative_to(ROOT)}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

if __name__ == "__main__":
    main()
