import asyncio
import json

async def broadcast(clients, payload):
    dead = []
    for c in clients:
        try:
            await c.send_text(json.dumps(payload))
        except:
            dead.append(c)

    for d in dead:
        clients.remove(d)
