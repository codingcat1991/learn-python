# 7.1 You have a list of list called `my_list` as below. Sum each list in it with your multiple processes.
# Also provide the running time of your computation compared with the running time of
# `list(map(sum, my_list))`. Any external packages are allowed.
# ```Python
# >>> from random import random
#
# >>> my_list = [[random(), random()] for _ in range(int(1e7))]
# ```
# 7.2 Write a decorator that can impose runtime type check for a function. This decorator allow
# users to decide to raise a warning or an exception when mismatch happens, which defaults to
# raising a warning. You can assume all the functions you apply will have only keyword arguments
# with proper default values. The usage would look like:
#
# ```Python
# # This should be equivalent to `@type_check(at_mismatch=’warning’)`
# @type_check
# def some_func1(*, a=6, b=’cc’):
#     pass
#
# @type_check(at_mismatch=’exception’)
# def some_func2(*, a=7, b=’dd’):
#     pass
# ```
#
# 7.3 Write unit tests for the above questions (question 7.1 - 7.2). Any frameworks are allowed.
