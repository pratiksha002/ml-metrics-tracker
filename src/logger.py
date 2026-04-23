import os
import csv
from datetime import datetime

log_file = "logs/metrics.csv"

def log_metrics(model_version, metrics):
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "model_version", "mae", "rmse", "r2"])


        writer.writerow([
            datetime.now(),
            model_version,
            metrics["mae"],
            metrics["rmse"],
            metrics["r2"]
        ])

prediction_file = "logs/predictions.csv"

def log_prediction(model_version, y_true, y_pred):
    file_exists = os.path.isfile(prediction_file)

    with open(prediction_file, mode='a', newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "model_version", "y_true", "y_pred"])

        for yt, yp in zip(y_true, y_pred):
            writer.writerow([
                datetime.now(),
                model_version,
                yt,
                yp
            ])


if __name__ == "__main__":
    sample_metrics = {
        "mae": 2.3,
        "rmse": 3.1,
        "r2": 0.89
    }

    y_true = [10, 20, 30]
    y_pred = [12, 18, 29]

    log_metrics("v1", sample_metrics)
    log_prediction("v1", y_true, y_pred)

    print("Logged successfully!")