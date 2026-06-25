import asyncio, json, random, string
try:
    import websockets
    from websockets.server import serve
except ImportError:
    raise SystemExit("Install websockets: pip install websockets")

# rooms[room_code] = {player_id: {id, name, x, z}}
rooms = {}
MAX_PLAYERS = 20

def gen_code(n=5):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))

async def handler(websocket):
    player_id = None
    room_code = None
    try:
        async for raw in websocket:
            try:
                data = json.loads(raw)
            except Exception:
                continue
            t = data.get("type")

            if t == "join":
                player_id = data.get("id", gen_code())
                room_code = data.get("room", "PUBLIC").upper() or "PUBLIC"
                name      = data.get("name", "Player")[:20]

                if room_code not in rooms:
                    rooms[room_code] = {}
                room = rooms[room_code]

                if len(room) >= MAX_PLAYERS:
                    await websocket.send(json.dumps({"type":"room_full"}))
                    continue

                room[player_id] = {"id": player_id, "name": name,
                                   "x": 0.0, "z": 0.0, "ws": websocket}

                # Broadcast updated player list (without ws)
                await broadcast_players(room_code)

            elif t == "move" and room_code and player_id:
                room = rooms.get(room_code, {})
                if player_id in room:
                    room[player_id]["x"] = data.get("x", 0)
                    room[player_id]["z"] = data.get("z", 0)
                    msg = json.dumps({"type":"move","id":player_id,
                                      "x":room[player_id]["x"],
                                      "z":room[player_id]["z"]})
                    for pid, p in list(room.items()):
                        if pid != player_id:
                            try: await p["ws"].send(msg)
                            except Exception: pass

            elif t == "chat" and room_code:
                room = rooms.get(room_code, {})
                msg  = json.dumps({"type":"chat","id":player_id,
                                   "name":data.get("name","?"),
                                   "msg": data.get("msg","")[:200]})
                for pid, p in list(room.items()):
                    try: await p["ws"].send(msg)
                    except Exception: pass

    except Exception:
        pass
    finally:
        if room_code and player_id and room_code in rooms:
            rooms[room_code].pop(player_id, None)
            if not rooms[room_code]:
                del rooms[room_code]
            else:
                await broadcast_players(room_code)

async def broadcast_players(room_code):
    room = rooms.get(room_code, {})
    players = [{"id":p["id"],"name":p["name"],"x":p["x"],"z":p["z"]}
               for p in room.values()]
    msg = json.dumps({"type":"players","players":players})
    for p in list(room.values()):
        try: await p["ws"].send(msg)
        except Exception: pass

async def main():
    print("LifeSim 3D WebSocket server starting on ws://0.0.0.0:8765")
    print(f"Max players per room: {MAX_PLAYERS}")
    async with serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
