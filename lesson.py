def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update']
    return any(word in command for word in ignore)

print(ignore_command('a'))