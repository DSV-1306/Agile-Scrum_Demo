
# Sprint Review

## Sprint Goal
Build the first working Iris flower classification model.

## Demonstration Checklist
- [x] Iris dataset loaded
- [x] Dataset split into training and testing sets
- [x] Decision Tree model trained
- [x] Accuracy and classification metrics calculated
- [x] Trained model saved to `models/iris_decision_tree.joblib`
- [x] Accuracy report generated in `reports/accuracy_report.txt`

## Actual Execution Result

- Algorithm: Decision Tree Classifier
- Dataset: Iris dataset
- Total samples: 150
- Training samples: 120
- Testing samples: 30
- Actual test accuracy: 100.00% (1.0000)

The model correctly classified all 30 samples in the selected test set. This result applies to the selected train/test split and does not guarantee identical performance on all unseen data.

## Was the Sprint Goal Achieved?

Yes. The model was trained and evaluated successfully. The Python script generated predictions, calculated evaluation metrics, saved the trained model, and generated the accuracy report.

## What Was Delivered?

- Working machine learning model
- Python source code
- Trained model artifact
- Accuracy report
- Product Backlog
- Scrum documentation

## What Went Well?

- Tasks were prioritized using the Product Backlog.
- The Decision Tree model was trained successfully.
- The fixed random seed made the experiment reproducible.
- Evaluation metrics were generated successfully.

## Problems Encountered

- Python dependencies needed to be installed before execution.
- The project initially required navigating to the correct working directory.

## Improvements for the Next Sprint

- Install dependencies before beginning development.
- Add automated tests for model predictions.
- Track model versions and experiment results.
- Improve documentation and automate model evaluation.
