print ('welcome to the tip calculator')
alpha = float(input ('\nwhat was the total bill? '))
beta = int(input('\nwhat percentage of the bill would u like to tip? (10,15,20)'))
gama = int(input('\nHow many people are splitting the bill?'))
tip_with_bill = int((alpha/100 * beta + alpha))
print('\nyour tip with bill is = ' + str(tip_with_bill))
tip_division = tip_with_bill/gama
final_amount = round(tip_division, 2)
print('\nHence each individual is to pay ' + str(final_amount) + ' as tip')




