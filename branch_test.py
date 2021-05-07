import pandas as pd

employee_list = [["寺尾哲雄"  , "管理職"    , 700000, 80000, 0 , 0   , 0],
                 ["若林仁継"  , "管理職"    , 375000, 40000, 0 , 0   , 0],
                 ["寺田帆香"  , "一般社員"  , 320000, 0    , 30, 0   , 0],
                 ["広田康博"  , "一般社員"  , 295000, 0    , 20, 0   , 0],
                 ["菅沼洋一郎", "一般社員"  , 220000, 0    , 35, 0   , 0],
                 ["菊地章"    , "アルバイト", 0     , 0    , 0 , 1200, 90], 
                 ["山岸柑奈"  , "アルバイト", 0     , 0    , 0 , 1000, 120]]

cal_OF  = lambda base,time: time * int(base*1.25/(160*10))*10
cal_SIP = lambda x: round(x*0.15, -1)
cal_IT =  lambda x: x*0.10

for employee in employee_list:
    OF  = 0
    SIP = 0
    IT  = 0
    if employee[1] == "管理職":
		# 処理記述 （ここ）
    elif employee[1] == "一般社員":
		# 処理記述
    elif employee[1] == "アルバイト":
		# 処理記述
		
		
    payment = int(payment)
    print(employee[0] + ": " + str(payment) + " 円")
