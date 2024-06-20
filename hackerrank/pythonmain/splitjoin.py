# Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):
    # write your code here
    x = line.split()
    s = "-".join(x)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)