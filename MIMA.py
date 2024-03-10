key=“888888"
k=input("请输入密码")
if k==key:
       print("密码正确")
       print("欢迎你")
       import time

       localtime = time.asctime(time.localtime(time.time()))
       print("本地时间 :", localtime)
       print("（程序已结束运行）")
else:
    print("密码错误")
    print("程序已强制停止")

    import time
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间 :", localtime)
    

