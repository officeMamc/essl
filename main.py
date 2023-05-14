import csv
from datetime import date, timedelta
import random

def timeGen(date,x):
    if x =="in":
        hh = "09"
        mm = random.randint(30,57)
        mm = str(mm)
        return str(date) + ' ' + hh + str(mm)
    elif x == "out":
        hh = "17"
        mm = random.randint(30,57)
        mm = str(mm)
        return str(date) + ' ' + hh +str(mm)
    elif x == "hwo":
        return str(date) + ' ' + "00:00"



#attendancelogid	AttendanceDate	EmployeeId	InTime	             InDeviceId	      OutTime	      OutDeviceId	Duration	LateBy	EarlyBy	IsOnLeave	LeaveType	LeaveDuration	WeeklyOff	Holiday	LeaveRemarks	PunchRecords	ShiftId	Present	Absent	Status	StatusCode	P1Status	P2Status	P3Status	IsonSpecialOff	SpecialOffType	SpecialOffRemark	SpecialOffDuration	OverTime	OverTimeE	MissedOutPunch	MissedInPunch	C1	C2	C3	C4	C5	C6	C7	Remarks	LeaveTypeId	LossOfHours
#attendancelogid	AttendanceDate	EmployeeId	InTime	             InDeviceId	      OutTime	      OutDeviceId	Duration	LateBy	EarlyBy	IsOnLeave	LeaveType	LeaveDuration	WeeklyOff	Holiday	LeaveRemarks	PunchRecords	ShiftId	Present	Absent	Status	StatusCode	P1Status	P2Status	P3Status	IsonSpecialOff	SpecialOffType	SpecialOffRemark	SpecialOffDuration	OverTime	OverTimeE	MissedOutPunch	MissedInPunch	C1	C2	C3	C4	C5	C6	C7	Remarks	LeaveTypeId	LossOfHours
#115	              30-03-2023	  2523	   1900-01-01 00:00:00		 TD     1900-01-01 00:00:00		               0	      0	        0	  No		   0	    0	0			2	0	1	Absent	A				No			0	0	-1	No	No									0	570
#hospi starts at 2588

empIdlist = [2527,2536,2626,2627,2628,2629,2630,2631,2632,2633,2634,2635,2537,2636,2637,2638,2641,2642,2643,2644,2645,2538,2646,2649,2650,2652,2653,2654,2655,2539,2657,2658,2659,2661,2662,2663,2664,2665,2540,2666,2667,2668,2541,2542,2543,2544,2545,2528,2546,2547,2548,2549,2550,2551,2552,2553,2554,2555,2529,2556,2557,2558,2559,2560,2561,2562,2563,2564,2565,2530,2566,2567,2568,2569,2570,2571,2572,2573,2574,2575,2531,2576,2577,2578,2579,2580,2581,2582,2583,2584,2585,2532,2586,2588,2533,2603,2604,2605,2534,2606,2607,2608,2609,2610,2611,2612,2613,2614,2615,2535,2616,2617,2618,2619,2620,2621,2622,2623,2624,2625,2639,2640,2647,2648,2651,2656,2660,2669,2587,2589,2590,2591,2592,2593,2594,2595,2596,2597,2598,2599,2600,2601,2602,2523,2524,2525]

holidays = ['2022-11-01','2022-11-11']
wo = ['2022-11-06','2022-11-13','2022-11-20','2022-11-27']


def date_range_list(start_date, end_date):
    curr_date = start_date
    while curr_date <= end_date:
        yield curr_date 
        curr_date += timedelta(days=1)

start_date = date(year=2022, month=11, day=1)
stop_date = date(year=2022, month=11, day=30)
date_list = date_range_list(start_date, stop_date)

counter = 12345
mainList = []
for i in empIdlist:
    if True:
        for j in date_list:
            if j not in holidays and wo:
                counter = counter + 1
                inTime = timeGen(j,"in")
                outTime = timeGen(j,"out")
                subList = [counter, j, i, inTime, "TD", outTime, "TD",0,0,0,"No",0,0,0,2,0,1,"Present","P","No",0,0,-1,"No","No",0,570]
                mainList.append(subList)
            elif j in wo:
                subList = [counter, j, i, timeGen(j,"hwo"), "", timeGen(j,"hwo"), "",0,0,0,"No",0,0,0,2,0,1,"WeeklyOff","WO","No",0,0,-1,"No","No",0,570]
                mainList.append(subList)
            elif j in holidays:
                subList = [counter, j, i, timeGen(j,"hwo"), "", timeGen(j,"hwo"), "",0,0,0,"No",0,0,0,2,0,1,"Holiday","H","No",0,0,-1,"No","No",0,570]
                mainList.append(subList)
              


for w in mainList:
    with open('nov.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(w)
