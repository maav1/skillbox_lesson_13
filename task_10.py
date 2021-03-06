print('Задача 10. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
# Числитель:  i(1 + i) **  n
# Знаменатель:  (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357

def calculating_annuity_payment(loan_amount,percent,years):
    annuity_payment = round(loan_amount * (((percent * (1 + percent) ** years) / ((1 + percent) ** years - 1))), 2)
    return annuity_payment

def credit_calculation(n,loan_amount,percent,annual_payment):
    for i in range(1, n+1):
            annual_percent = loan_amount * percent #Выплачено процентов
            body_credit = annual_payment - annual_percent #Выплочено тела кредита
            outcome(i,loan_amount, annual_percent, body_credit) #Вызов функции вывода
            loan_amount -= body_credit  # Остаток задолжности
    print('Остаток долга:',loan_amount,'\n\n')
    print('='*50)
    return loan_amount

def outcome(i,loan_amount,annual_percent,body_credit):
    print('*' * 10, 'ПЕРИОД:', i, '*' * 10)
    print('Остаток долга на начало периода:', loan_amount)
    print('Выплачено процентов:', annual_percent)
    print('Выплачено тела кредита:', body_credit,'\n')


n = 3
loan_amount = float(input('Ведите сумму кредита: '))
years = int(input('На сколько лет выдан?: '))
percent = float(input('Сколько процентов годовых?: \n')) / 100
annual_payment = calculating_annuity_payment(loan_amount,percent,years)


loan_amount = credit_calculation(n,loan_amount,percent,annual_payment) #Просчёт и вывод первой части программы
contract_extension = int(input('На сколько лет продляется договор?:'))
n = years - 3 + contract_extension
percent = float(input('Увеличение ставки до: ')) / 100
print()
annual_payment = calculating_annuity_payment(loan_amount,percent,n)
loan_amount = credit_calculation(n,loan_amount,percent,annual_payment) #Просчёт второй части программы с уже другими параметрами.























