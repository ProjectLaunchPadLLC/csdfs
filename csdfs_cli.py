import subprocess

def up():
    subprocess.run(["uvicorn", "api.server:app", "--reload"])

def run():
    print("Running CSDFS system...")

if __name__ == "__main__":
    up()
