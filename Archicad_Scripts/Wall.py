from archicad import ACConnection

conn = ACConnection.connect()
assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities

walls = acc.GetElementsByType("Wall")
print(f'Number of Walls: {len(walls)}')