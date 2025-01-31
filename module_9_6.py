# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
#
# fib = fibonacci(10)
# print(fib)
#
# for i in fib:
#     print(i)
#
# import time
#
# start = time.time()
#
# def read_large_file(file_path):
#     with open(file_path, "r", encoding = "utf-8") as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_large_file("large_file.txt"):
#     print(line)
#
#
# fin = time.time()
# print((fin-start)*100)


def all_variants(text):
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            yield text[i:j]
a = all_variants("abc")

for i in a:
    print(i)
