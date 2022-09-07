import sys

sys_argv_list = sys.argv
cmd_args = sys.argv[1:]

print("The sys.argv list looks like this: ", sys_argv_list)
print("But we are only interested in these arguments: ", cmd_args)
