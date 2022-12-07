class directory:
    def __init__(self, full_path):
        self.full_path = full_path
        self.children = []
        self.files = []
        self.sum_size = -1

def calc_file_size_sum(directory):
    total_size = 0
    
    for (size, name) in directory.files:
        total_size += size
    
    for child in directory.children:
        if child.sum_size == -1:
            calc_file_size_sum(child)
        total_size += child.sum_size

    directory.sum_size = total_size

commands = []
with open('python/07.in','r') as f:
    for x in f.readlines():
        commands.append(x.strip())

# part 1

start_root = '/'

directories = dict()
directories[start_root] = directory(start_root)

current_directory = start_root

for command in commands:
    command_parts = command.split(' ')

    if command_parts[0] == '$':
        if command_parts[1] == 'cd':
            
            if command_parts[2] == '/':
                current_directory = '/'
            
            elif command_parts[2] == '..':

                current_directory = current_directory[:current_directory[:-1].rindex('/')+1]

            else:
                current_directory += command_parts[2] + '/'

        elif command_parts[1] == 'ls':
            pass # no action, output captured on next line
        else:
            print(f'unexpected command of {command_parts[1]}')

    # the rest assumed to be output of ls command
    elif command_parts[0] == 'dir':
        # create the directory
        folder_path = current_directory + command_parts[1] + '/'
        directories[folder_path] = directory(folder_path)
        directories[current_directory].children.append(directories[folder_path])

    else:
        # add the file to the list of files for that directory
        directories[current_directory].files.append((int(command_parts[0]), command_parts[1]))


calc_file_size_sum(directories[start_root])

size_limit = 100000

total_small_dir_sizes = 0

for path, dir in directories.items():
    if dir.sum_size < size_limit:
        total_small_dir_sizes += dir.sum_size

print(total_small_dir_sizes)

# part 2
total_available_space = 70000000
free_space_required   = 30000000

currently_used_space = directories[start_root].sum_size

need_to_free = free_space_required - (total_available_space - currently_used_space)

all_dir_sizes = []
for path, dir in directories.items():
    all_dir_sizes.append(dir.sum_size)

all_dir_sizes.sort()

for size in all_dir_sizes:
    if size > need_to_free:
        print(size)
        break