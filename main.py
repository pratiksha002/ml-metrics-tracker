from src.train import train_model
from src.evaluate import evaluate_regression
from src.logger import log_metrics, log_prediction
from src.tracker import track_experiment

def main():
    model_version = 'v1'

    y_true, y_pred = train_model()

    metrics = evaluate_regression(y_true, y_pred)

    log_metrics(model_version, metrics)
    log_prediction(model_version, y_true, y_pred)

    parameters = {
    "model": "LinearRegression"
     }

    track_experiment(model_version, parameters, metrics)

    print("Pipeline executed")
    print("Metrics:", metrics)


if __name__ == "__main__":
    main()


