def vacuum_cleaner_agent():
    environment = {'A': True, 'B': True}
    position = 'A'
    actions = []
    while True:
        if environment[position]:
            actions.append('Suck')
            environment[position] = False
        else:
            actions.append('Move')
            position = 'B' if position == 'A' else 'A'
        if not any(environment.values()):
            break
    return actions

print(vacuum_cleaner_agent())
