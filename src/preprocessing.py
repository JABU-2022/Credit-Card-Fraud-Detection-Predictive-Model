# distribution of legit transactions & fraudulent transactions
credit_card_data['Class'].value_counts()

# separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

# statistical measures of the data
legit.Amount.describe()

# compare the values for both transactions
credit_card_data.groupby('Class').mean()

legit_sample = legit.sample(n=492)

df = pd.concat([legit_sample, fraud], axis=0)

