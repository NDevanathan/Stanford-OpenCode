import self_modify

def example_fun():
    self_modify.function_start()

    for i in range(10):
        a = 2
        print(a)

        new_line = 'a = {}'.format(a+1)
        self_modify.replace_line(__file__, 7, new_line, 2)

    # new_line = 'a = {}'.format(0)
    # self_modify.replace_line(__file__, 5, new_line, 2)

    return True
