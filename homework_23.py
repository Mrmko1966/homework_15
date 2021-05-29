from datetime import datetime
import  time
import os
def my_new_decorator(func: callable) -> callable:
    print("decorated")
    def decor(file1):
        start_time = datetime.now()
        print("func starts at {}".format(start_time))

        result = func()

        end_time = datetime.now() - start_time
        print("it took {} seconds for {}".format(end_time.seconds, func.__name__))

        return result

    return decor
def wirte_file():
    print("kkkk")
    file_path='myfile1.txt'
    with open("myfile1.txt", "a") as file1:
        file1.write(f"{datetime.now()}")
    if os.stat(file_path).st_size == 0 or None:
        with open("myfile1.txt", "w") as file1:
            file1.write(f"{datetime.now()}")
    else:
        with open("myfile1.txt", "a") as file1:
            file1.write(f"\n{datetime.now()}")
    time.sleep(1.0)

decor =my_new_decorator(wirte_file)
file1=1
decor(file1)


