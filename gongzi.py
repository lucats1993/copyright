#coding:utf-8
class Pay():
    def __init__(self,basic_pay=4000,normal_over_hour=28,weekend_over_hour=32,absent_day=0):
        self.basic_pay =basic_pay
        self.hourly_wage =self.hour_pay(basic_pay)
        self.overtime_pay =self.get_overtime_pay(normal_over_hour,weekend_over_hour)
        self.absent_charge =self.get_absent_charge(absent_day)

    def get_overtime_pay(self,normal_hour,weekend_hour):
        return self.point((normal_hour*self.hourly_wage*1.5+weekend_hour*self.hourly_wage*2)*0.7*0.7)

    def get_absent_charge(self,day):
        return self.point(self.hourly_wage*day*8)

    def get_pre_tax(self):
        return  self.basic_pay + self.overtime_pay - self.absent_charge

    def summary(self):
        pre_tax = self.get_pre_tax()
        tax_sum= self.tax_charge(pre_tax-self.wxyj_charge())
        dict = {'overtime_pay': self.overtime_pay,
                'absent_charge': self.absent_charge,
                'wxyj_charge': self.wxyj_charge(),
                'tax_sum':tax_sum ,
                'pre_tax': self.point(pre_tax) ,
                'after_tax': self.point(pre_tax - tax_sum-self.wxyj_charge())
                }
        return dict

    @staticmethod
    def wxyj_charge(wx_basic=2772,gjj_basic=1890):
        return (wx_basic*10.5+gjj_basic*8)/100

    @staticmethod
    def hour_pay(x):
        return x / 21.75 / 8

    @staticmethod
    def tax_charge(x):
        m=x-3500
        if m <= 1500:
            tax_mount = m*3/100
        elif m < 4500:
            tax_mount = m * 10 / 100 -105
        else :
            tax_mount = m * 20 / 100 - 555
        return round(tax_mount,2)

    @staticmethod
    def point(x,n=2):
        return round(x,n)

if __name__ == '__main__':
    parm={
        "basic_pay":6000,
        "normal_over_hour":24,
        "weekend_over_hour":45,
        "absent_day":0
    }
    print Pay(**parm).summary()