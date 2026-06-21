import subprocess

def run():
    subprocess.Popen(["uvicorn", "csdfs.api.server:app", "--reload"])
    subprocess.Popen(["npm", "run", "dev", "--prefix", "frontend"])
    subprocess.Popen(["python", "-m", "csdfs.ray_cluster.cluster"])

if __name__ == "__main__":
    run()
