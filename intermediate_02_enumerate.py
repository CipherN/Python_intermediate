#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

example = ['right', 'left', 'up', 'down']

# enumrate  demo1
for i in range(len(example)):
    print(i, example[i])

# enumrate  demo2
for i, j in enumerate(example):
    print(i, j)

# enumrate  demo3
example_dict = {'left': '<', 'right': '>', 'up': '^', 'down': 'v', }
[print(i, j) for i, j in enumerate(example_dict)]

# enumrate  demo4
new_dict = dict(enumerate(example))
print(new_dict)