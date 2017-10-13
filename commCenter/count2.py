


import time



for i in range(100):
    with open ("newData.txt", "w") as myfile:
            myfile.write(str(i))

    with open ("newData2.txt", "w") as myfile:
            myfile.write(str(i))
    with open ("newData3.txt", "w") as myfile:
            myfile.write(str(i))
    with open ("newData4.txt", "w") as myfile:
            myfile.write(str(i))
    with open ("progressData.txt", "w") as myfile:
            myfile.write(str(i))
    time.sleep(1)









