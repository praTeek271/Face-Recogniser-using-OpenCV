import time
from tqdm import tqdm


def loading():
    for _ in tqdm(range(100),desc="Loding.....",ascii=False):
        time.sleep(0.01)
        pass
    
    print("loding done")


    time.sleep(3)



if __name__ == '__main__':
    loading()
    