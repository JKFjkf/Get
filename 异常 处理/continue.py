#!/usr/bin/python
# --coding:utf-8--
import time


def test():
    while True:
        try:
            a = 1 / 0
        except Exception as e:
            print("exception")
            continue
            #break
        finally:
            print("finally")
            time.sleep(3)
        print("out of try")


if __name__ == '__main__':
    test()