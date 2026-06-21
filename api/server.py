from fastapi import FastAPI, WebSocket
from csdfs.ray_cluster.cluster import CSDFSCluster

app = FastAPI()
cluster = CSDFSCluster()

clients = []

@app.websocket("/ws")
async def websocket(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

    while True:
        data = await ws.receive_text()
