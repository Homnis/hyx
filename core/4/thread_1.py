import time,threading

count=10

def saleTickets():
    global count
    while True:
        if lock.acquire():
            if count>0:
                print(threading.current_thread().getName(),"售出一张票",count)
                count-=1
                time.sleep(0.1)
                # lock.release()
            else:
                print(threading.current_thread().getName(),"售空")
                lock.release()
                break
            lock.release()



if __name__ == '__main__':
    lock = threading.Lock()
    t1=threading.Thread(name="窗口一",target=saleTickets)
    t2 = threading.Thread(name="窗口二", target=saleTickets)

    t1.start()
    t2.start()