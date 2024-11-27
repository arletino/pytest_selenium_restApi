from datetime import datetime

def count_time(arg): 
    def outwraper(func):
        def wraper(*args, **kwargs):
            start = datetime.now()
            func(*args)
            time = (datetime.now() - start)
            print(time)
            return 
        return wraper
    return outwraper

@count_time
def calc(a, b):
    print(a + b)

if __name__ == '__main__':
    calc(3, 5)
