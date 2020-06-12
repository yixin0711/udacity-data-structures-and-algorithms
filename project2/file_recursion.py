import os

def find_files(suffix=None, path=None):
    if suffix == None:
        return "Please input the suffix"
    elif path == None:
        return "Please input the path"
    path_list = []
    try:
        subdir = os.listdir(path)
    except Exception as inst:
        return "No such directory found"
    subdir_path = [os.path.join(path, item) for item in subdir]
    for item in subdir_path:
        if os.path.isfile(item) and item.endswith(suffix):
            path_list.append(os.path.join(path, item))
        elif os.path.isdir(item):
            sub_list = find_files(suffix, item)
            path_list.extend(sub_list)
    return path_list

print(find_files('.c', '/Users/Sharonvy/Downloads/testdir'))
#this will return all the .c files in the directory

'''
['/Users/Sharonvy/Downloads/testdir/subdir3/subsubdir1/b.c', 
'/Users/Sharonvy/Downloads/testdir/t1.c', '/Users/Sharonvy/Downloads/testdir/subdir5/a.c', 
'/Users/Sharonvy/Downloads/testdir/subdir1/a.c']
'''


#marginal cases tested
print(find_files(path='/Users/Sharonvy/Downloads/testdir'))
#this will raise error "Please input the suffix"

print(find_files(".c"))
#this will raise error "Please input the path"

print(find_files(".c", "~/Downloads"))
#this will raise error "No such directory found"

