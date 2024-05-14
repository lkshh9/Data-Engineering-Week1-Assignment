import itertools


result_string = ''
for key, group in itertools.groupby(input()):
    result_string = result_string + f'{((len(list(group)), int(key)))} '

print(result_string)
