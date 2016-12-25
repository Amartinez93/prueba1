# coding=utf-8
import datetime

ano_actual = str(datetime.date.today().year)

mes_actual = str(datetime.date.today().month)

dia_actual = str(datetime.date.today().day)

ano_recor = str(datetime.date.today().year)

mes_recor = str(datetime.date.today().month)

dia_recor = str(datetime.date.today().day)


def recordar():
    print dia_actual + '/' + mes_actual + '/' + ano_actual
    Recordatorio = input("recordar:")
    print 'fecha de recordatorio:'
    dia_recor = input('dia de recordatorio:')
    mes_recor = input('mes de recordatorio:')
    ano_recor = input('año de recordatorio:')
    print dia_recor + '/'+mes_recor+'/'+ano_recor
recordar()
