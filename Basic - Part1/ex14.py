from datetime import date


start_date = date(2014, 7, 2)
end_date = date(2014, 7, 11)
delta_date = end_date - start_date
print(delta_date.days)
