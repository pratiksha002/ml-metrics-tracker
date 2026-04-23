from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_regression(y_true, y_pred):
    """Compute regression metrics"""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)


    return{
        "mae": round(mae, 4),
        "rmse": round(float(rmse), 4),
        "r2": round(r2, 4)
    }