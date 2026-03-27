def helper_count(current_day, final_day):
    if current_day > final_day:
        print("Harvest time!")
        return
    print(f'Day {current_day}')
    helper_count(current_day + 1, final_day)


def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))

    helper_count(1, days)
