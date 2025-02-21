print("hello nabiha this is your salary saving script")

salary = (float(input("what is your monthly income? $")))

month = input("what is the month you are storing the salary for? ")

per_savings, per_rent, per_electricity = input("enter the percentage of: savings, rent, and electricity separated by space. ").split()

print(f"savings percentage: {per_savings}")
print(f"rent percentage: {per_rent}")
print(f"electricity percentage: {per_electricity}")

saving = float(per_savings) / 100 * salary
rent = float(per_rent) / 100 * salary
electricity = float(per_electricity) / 100 * salary

print (f"the saving amount: {saving}")
print (f"the rent amount: {rent}")
print (f"the electricity amount: {electricity}")

combined_bills = saving + rent + electricity
print (f"combined spendings: {combined_bills}")

remainder = salary - combined_bills
print (f"remainder: {remainder}")

yearly_estimation = (rent + electricity) * 12
print (f"yearly estimate: {yearly_estimation}")

salary_powered_by_two = salary ** 2 
print (f"salary powered by two: {salary_powered_by_two}")

