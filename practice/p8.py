captain = {
    'Madiba': 'Chubby Obiora-Okafo', 
    'Blue-Jays': 'Christopher Uweh',
    'Cirok': 'Alexander', 
    'TSG Walkers': 'Ikechukwu'
}

goalkeepers = {
    'Madiba': 'Chubby Obiora-Okafo',
    'Blue-Jays': 'Oladimeji Abaniwondea/Jeffery Awagu',
    'Cirok': 'Timileyin Pearse/Izuako Jeremy',
    'TSG Walkers': 'Ayomide Ojituku'
}

# Print captains
print("Captains:")
for team in captain:
    print(f"{team}: {captain[team]}")

# Print a separator
print("\nGoalkeepers:")

# Print goalkeepers
for team in captain:
    print(f"{team}: {goalkeepers[team]}")
