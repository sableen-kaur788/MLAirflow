import subprocess

def dvc_pull():
    """Pull data from DVC remote."""
    subprocess.run(["dvc", "pull"], cwd="/opt/airflow/mlpipeline", check=True)

def dvc_push():
    """Add & push trained model to DVC remote."""
    subprocess.run(["dvc", "add", "models/model.pkl"], cwd="/opt/airflow/mlpipeline", check=True)
    subprocess.run(["dvc", "push"], cwd="/opt/airflow/mlpipeline", check=True)
