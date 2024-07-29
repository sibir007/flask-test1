with open('requirments.txt', 'rt') as rf:
    with open('requirments_toml.txt', 'wt') as tf:
        for line in rf:
        # line = rf.readline()
            line = line[:-1]
            tf.write(f'"{line}",\n')