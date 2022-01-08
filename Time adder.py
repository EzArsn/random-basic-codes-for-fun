def main():
    print('Start time (in 24 Hrs): ',end='')
    s=input()
    print('Time Taken: ', end='')
    t=input()
    col=s.find(':')
    s_hr=s[:col]
    s_hr=int(s_hr)
    s_min=s[col+1:]
    s_min=int(s_min)
    on=t.find(':')
    t_hr=t[:on]
    t_hr=int(t_hr)
    t_min=t[on+1:]
    t_min=int(t_min)
    def add_time():
        r_min=s_min+t_min
        carry=0
        if r_min>60:
            carry=1
            r_min=r_min-60
        r_hr=s_hr+t_hr+carry
        day=0
        if r_hr>24:
            day=1
            r_hr=r_hr-24
        print(f'Total time is {day}days, {r_hr} hours and {r_min} minutes')
    add_time()
main()

