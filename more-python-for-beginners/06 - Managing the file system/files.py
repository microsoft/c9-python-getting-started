from pathlib import Path
cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# Get the file name
print('\nfile name: ' + demo_file.name)

# Get the extension
print('\nfile suffix: ' + demo_file.suffix)

# Get the folder
print('\nfile folder: ' + demo_file.parent.name)

# Get the size
print('\nfile size: ' + str(demo_file.stat().st_size) + '\n')