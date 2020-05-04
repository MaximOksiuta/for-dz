from time import sleep


class TrafficLight:

    def __init__(self, rt, yt, gt):
        self.__color = [['red', rt], ['yellow', yt], ['green', gt]]

    def running(self):
        while True:
            for i in self.__color:
                print(i[0])
                sleep(i[1])


tl = TrafficLight(int(input('Time for red: ')), int(input('Time for yellow: ')), int(input('Time for green: ')))
tl.running()