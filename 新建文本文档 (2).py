import  threading,time

def thead():
    # time.sleep(1)

    time.sleep(3)
    print("3")
def thead1():

    time.sleep(1)
    print("1")
def main():
    print("主方法开始执行")

    #创建2个线程
    poll = []#线程池
    thead_one = threading.Thread(target=thead, args=())
    poll.append(thead_one) #线程池添加线程
    thead_one = threading.Thread(target=thead1, args=())
    poll.append(thead_one) #线程池添加线程
    for n in poll:
        n.start()   #准备就绪,等待cpu执行
    for n in poll:
        n.join()   #准备就绪,等待cpu执行        
    print("主方法执行完毕")
    return

if __name__ == '__main__':
    num = main()


