"""
Given a temperature (in Celsius), print the state of water at that temperature
"""

# Todo: Handle invalid inputs
try:
    temp = float(input("What's the H20 temperature? "))
    if temp <= 0:
        print("  It’s ice")
    elif temp >= 100:
        print("  It’s steam")
    else:
        print("  It's water")
except ValueError as e:
    print(f"Incorrect Input: {e}")