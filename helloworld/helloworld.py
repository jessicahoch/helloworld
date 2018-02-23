
import random
import datetime

def helloworld(name=None, howlong=None, countdown=None):
    """
    return hello world, or hello {name}
    """

    # print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))

    # print days til Darwin's birthday
    if howlong:
        dday = datetime.datetime(2019, 2, 12)
        diff = dday - datetime.datetime.now()
        print("{} days until Darwin's birthday".format(diff.days))

    # print countdown to armageddon
    if countdown:
        end = random.randint(0, 100)
        print("the world will end in {} days... maybe".format(end))