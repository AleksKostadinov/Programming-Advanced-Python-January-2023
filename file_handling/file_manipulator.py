import os

command = input()

while command != 'End':
    action, *info = command.split('-')

    if action == 'Create':
        with open(f'./{info[0]}', 'w') as f:
            pass

    elif action == 'Add':
        with open(f'./{info[0]}', 'a') as f:
            f.write(f'{info[1]}\n')

    elif action == 'Replace':
        try:
            with open(f'./{info[0]}', 'r') as f:
                text = f.read()

            text = text.replace(info[1], info[2])

            with open(f'./{info[0]}', 'w') as file:
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif action == 'Delete':
        try:
            os.remove(f'./{info[0]}')

        except FileNotFoundError:
            print("An error occurred")

    command = input()