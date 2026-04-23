import json
import os
from datetime import datetime

track_file = "logs/experiments.json"

def load_experiments():
    if not os.path.exists(track_file):
        return[]
    
    with open(track_file, "r") as f:
        return json.load(f)
    

def save_experiments(experiments):
    with open(track_file, "w") as f:
        json.dump(experiments, f, indent=4)

def get_next_run_id(experiments):
    if not experiments:
        return 1
    return experiments[-1]["run_id"] + 1



def track_experiment(model_version, parameters, metrics):
    experiments = load_experiments()
    run_id = get_next_run_id(experiments)

    new_run = {
        "run_id": run_id,
        "model_version": model_version,
        "parameters": parameters,
        "metrics": metrics,
        "timestamp": str(datetime.now())
    }

    experiments.append(new_run)
    save_experiments(experiments)

    print(f"Experiment {run_id} tracked")