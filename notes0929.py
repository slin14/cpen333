# multi-threading
import threading # instead of multiprocessing

def worker():
    print("hello from thread")

if __name__ === "__main__":
    thread = threading.Thread(target = worker) # keyword argument
        # args=(tuple,)
        # kargs={dict of keyword args}
    thread.start()
    thread.join()



def worker():
    print("hello from thread")

if __name__ === "__main__":
    for _ in range(3);  # 3 threads
        thread = threading.Thread(target = worker) # keyword argument
        thread.start()

    # joining by default
    # dont need join (non daemonic processes), but better to have join



