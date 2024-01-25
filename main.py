# Lindsay Green and Caleb Jenkinson
# https://github.com/lindllgrn/SalaryCalculator
# Calculate the unadjusted and adjusted salary, based on what the user makes and the time they work

DASH_LENGTH = 40
COLUMN_LENGTH = 25


def header():
    print('=' * DASH_LENGTH)
    print("The Salary Calculator Program")
    print('=' * DASH_LENGTH)


def inputs():
    salary_per_hour = float(input(f"{'Salary per hour':.<{COLUMN_LENGTH}}: "))
    hours_per_week = float(input(f"{'Hours per week':.<{COLUMN_LENGTH}}: "))
    days_per_week = float(input(f"{'Days per week':.<{COLUMN_LENGTH}}: "))
    holidays_per_year = float(input(f"{'Holidays per year':.<{COLUMN_LENGTH}}: "))
    vacation_days = float(input(f"{'Vacation days per year':.<{COLUMN_LENGTH}}: "))
    print('=' * DASH_LENGTH)

    unadjusted_salary = (salary_per_hour * (hours_per_week / days_per_week) * (52 * days_per_week))
    print(f"{'Unadjusted Salary':.<{COLUMN_LENGTH}}: ${unadjusted_salary:6,.2f}")

    adjusted_salary = (salary_per_hour * (hours_per_week / days_per_week) *
                       (52 * days_per_week - holidays_per_year - vacation_days))
    print(f"{'Adjusted Salary':.<{COLUMN_LENGTH}}: ${adjusted_salary:6,.2f}")

    print('=' * DASH_LENGTH)


if __name__ == '__main__':
    header()
    inputs()
    print('Goodbye!')
