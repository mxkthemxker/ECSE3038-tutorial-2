readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(f"Device: {device['name']}, Temperature: {device['temp']},")
        

list_devices(readings)

def average_temp(devices):
    total_temp = 0
    
    for device in devices:
        total_temp = total_temp + device["temp"]

    return total_temp / len(devices)

print(f"Average temperature: {average_temp(readings)}")


def hottest_device(devices):
    hottest = devices[0]

    for device in devices:
        if device["temp"] > hottest["temp"]:
            hottest = device

    return hottest

print(f"Hottest device: {hottest_device(readings)}")

def to_status(device):
    return {
        "device": device["name"],
        "status": "ok" if device["online"] else "offline",
        "celsius": device["temp"]
    }
print(f"Device status: {to_status(readings[3])}")
