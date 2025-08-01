"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.

Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]
print(luggage)
Map = {
luggage[0][0]: luggage[0][1],
luggage[1][0]: luggage[1][1],
luggage[2][0]: luggage[2][1]
}
print(Map)

luggage.insert(3, ("Daisy" , 20))
print(luggage)
luggage.remove(luggage[1])
print(luggage)

report = {
"passengers": luggage
}
print(report)
