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
        sum234 = employee[2] + employee[3]  # 基本給 + 職能給
        SIP = cal_SIP(sum234)  # 社会保険料
        IT  = cal_IT(sum234 - SIP) # 所得税
        payment = sum234 - SIP - IT
    elif employee[1] == "一般社員":
        OF  = cal_OF(employee[2], employee[4]) # 残業代 = 残業時間*残業時間単位
        sum234 = employee[2] + employee[3] + OF  # 基本給 + 職能給 + 残業代
        SIP = cal_SIP(sum234)  # 社会保険料
        IT  = cal_IT(sum234 - SIP) # 所得税
        payment = sum234 - SIP - IT
    elif employee[1] == "アルバイト":
        IT  = cal_IT( employee[5] * employee[6] ) # 所得税
        payment = employee[5] * employee[6] - IT  # 時間給 - 所得税
		
		
    payment = int(payment)
    print(employee[0] + ": " + str(payment) + " 円")
