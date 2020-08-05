for _ in range(int(input())):
    sh,sm,eh,em=map(int,input().split())
    s=(sh*60)+sm
    e=(eh*60)+em
    ans=e-s
    hour=ans//60
    min =ans%60
    print(hour,min)