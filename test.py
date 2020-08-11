from email.utils import formatdate

import pytest
def demo(num1,num2,num3):
    print(num1,num2,num3)


def test_demo(num1,num2,num3):
    demo(num1,num2,num3)