from pathlib import Path
cwd = Path.cwd()

# Get the parent directory
parent = cwd.parent

# Is this a directory?
print('\nIs this a directory? ' + str(parent.is_dir()))

# Is this a file?
print('\nIs this a file? ' + str(parent.is_file()))

# List child directories
print('\n-----directory contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
