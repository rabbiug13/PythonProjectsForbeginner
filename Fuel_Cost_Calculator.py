t_dist = input('Enter distance of trip: ')
f_ef = input('Enter fuel efficiency: ')
f_price = input('Enter fuel price: ')

dist = float(t_dist)
ef = float(f_ef)
price = float(f_price)

total_t = dist / ef
total_c = total_t * price
print('Total Fuel Consumption:', total_t,'gallons' )
print('Total Fuel Consumption:', '$',total_c )