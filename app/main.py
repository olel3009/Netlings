from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import json
import asyncio

from app.AgentEnvironment import Enviroment

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"Client connected: {websocket.client}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        print(f"Client disconnected: {websocket.client}")

    async def broadcast(self, message: dict):
        if not self.active_connections:
            print("No active connections to broadcast to.")
            return
        data = json.dumps(message)
        for connection in self.active_connections:
            await connection.send_text(data)

manager = ConnectionManager()
environment = Enviroment()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    print("TEST")
    await manager.connect(websocket)
    try:
        while True:
            agents_data = environment.collectAll(False)
            await manager.broadcast(agents_data)
            await asyncio.sleep(1 / 30)  # 30 updates per second
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        print(f"Error: {e}")
        manager.disconnect(websocket)

@app.websocket("/heartbeat/")
async def heartbeat_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.send_text("heartbeat")
            await asyncio.sleep(5)  # Sends a heartbeat every 5 seconds
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        print(f"Error: {e}")
        manager.disconnect(websocket)
