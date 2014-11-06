# -*- coding: utf-8 -*-

import citysae
import static
import requests

def getdetails(cityu):
    code = citysae.getcode(cityu)
    if code is not None:
        url = static.weatherbase.format(code)
        weath = requests.get(url, headers = static.UA)
        text = weath.json()
        # print(text['weatherinfo']['weather1'])
        return render(text)
    return None

def render(text):
    city = text['weatherinfo']['city'] 
    datetime = text['weatherinfo']['date_y']  + '  ' + text['weatherinfo']['week'] 

    todayqiwen = text['weatherinfo']['temp1']
    todaytianqi = text['weatherinfo']['weather1']
    todayfengli = static.todayfengli + text['weatherinfo']['fl1']
    todayzwx = static.todayzwx + text['weatherinfo']['index_uv']
    todaytuijian = text['weatherinfo']['index_d']

    #todayqiwen = static.todayqiwen + text['weatherinfo']['temp1']
    #todaytianqi = static.todaytianqi + text['weatherinfo']['weather1']
    #todayfengli = static.todayfengli + text['weatherinfo']['fl1']
    #todayzwx = static.todayzwx + text['weatherinfo']['index_uv']
    #todaytuijian = static.todaytuijian + text['weatherinfo']['index_d']
    # todayxiche = static.todayxiche + text['weatherinfo']['index_xc']
    # todaylvyou = static.todaylvyou + text['weatherinfo']['index_tr']
    # todayshushi = static.todayshushi + text['weatherinfo']['index_co']
    # todaychenlian = static.todaychenlian + text['weatherinfo']['index_cl']
    # todayliangshai = static.todayliangshai + text['weatherinfo']['index_ls']
    # todayganmao = static.todayganmao + text['weatherinfo']['index_ag']

    # today = (todayqiwen, todaytianqi, todayfengli, todayzwx, todayxiche, todaylvyou, 
    #         todayshushi, todaychenlian, todayliangshai, todayganmao)
    
    today = (todaytianqi, todayqiwen, todayfengli)
    todaystr = '\n'.join(today)
    today = (todaystr, static.fenge, todaytuijian)
    todaystr = '\n'.join(today)
    f1 = u'1: ' + text['weatherinfo']['temp1'] + '  ' + text['weatherinfo']['weather1']
    f2 = u'2: ' + text['weatherinfo']['temp2'] + '  ' + text['weatherinfo']['weather2']
    f3 = u'3: ' + text['weatherinfo']['temp3'] + '  ' + text['weatherinfo']['weather3']
    f4 = u'4: ' + text['weatherinfo']['temp4'] + '  ' + text['weatherinfo']['weather4']
    f5 = u'5: ' + text['weatherinfo']['temp5'] + '  ' + text['weatherinfo']['weather5']
    future = (f1, f2, f3, f4, f5)
    futurestr = '\n'.join(future)
    
    update = text['weatherinfo']['date_y'] + text['weatherinfo']['fchh'] + static.shi

    total = (city, datetime, static.fenge, todaystr, static.fenge, futurestr, static.fenge, update)
    totalstr = '\n'.join(total)

    return totalstr

if __name__ == '__main__':
    getdetails(u'成都')