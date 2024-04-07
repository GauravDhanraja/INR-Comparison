import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data_asian = {
    'Country': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Cambodia', 'China', 'Georgia', 'Hong Kong', 'Indonesia', 'Japan', 'Kazakhstan', 'Laos', 'Malaysia', 'South Korea', 'Sri Lanka', 'Maldives', 'Pakistan', 'Philippines', 'Thailand', 'Taiwan', 'Vietnam'],
    'Currency': ['Afghan Afghani', 'Armenian Dram', 'Azerbaijani Manat', 'Bangladeshi Taka', 'Cambodian Riel', 'Chinese Yuan', 'Georgian Lari', 'Hong Kong Dollar', 'Indonesian Rupiah', 'Japanese Yen', 'Kazakhstani Tenge', 'Lao Kip', 'Malaysian Ringgit', 'South Korean Won', 'Sri Lankan Rupee', 'Maldivian Rufiyaa', 'Pakistani Rupee', 'Philippine Peso', 'Thai Baht', 'Taiwanese Dollar', 'Vietnamese Dong'],
    'Currency Symbol': ['AFN', 'AMD', 'AZN', 'BDT', 'KHR', 'CNY', 'GEL', 'HKD', 'IDR', 'JPY', 'KZT', 'LAK', 'MYR', 'KRW', 'LKR', 'MVR', 'PKR', 'PHP', 'THB', 'TWD', 'VND'],
    'Value_in_INR': [1.06, 0.21, 48.95, 0.75, 0.020, 11.37, 31.11, 10.63, 0.0053, 0.56, 0.17, 0.0041, 17.61, 0.061, 0.25, 5.42, 0.29, 1.46, 2.24, 2.57, 0.0034]
}

data_middle_eastern = {
    'Country': ['Bahrain', 'United Arab Emirates', 'Saudi Arabia', 'Oman', 'Israel', 'Iraq', 'Iran', 'Jordan', 'Kuwait', 'Lebanon', 'Qatar', 'Libya'],
    'Currency': ['Bahraini Dinar', 'Emirati Dirham', 'Saudi Arabian Riyal', 'Omani Rial', 'Israeli Shekel', 'Iraqi Dinar', 'Iranian Rial', 'Jordanian Dinar', 'Kuwaiti Dinar', 'Lebanese Pound', 'Qatari Riyal', 'Libyan Dinar'],
    'Currency Symbol': ['BHD', 'AED', 'SAR', 'OMR', 'ILS', 'IQD', 'IRR', 'JOD', 'KWD', 'LBP', 'QAR', 'LYD'],
    'Value_in_INR': [220.72, 22.65, 22.18, 216.11, 21.64, 0.063, 0.0020, 117.29, 268.93, 0.0055, 22.85, 16.91]
}

data_european = {
    'Country': ['Bosnia', 'The European Union', 'Bulgaria', 'The Czech Republic', 'Croatia', 'Denmark', 'Hungary', 'Iceland', 'Moldova', 'Macedonia', 'Norway', 'Poland', 'Romania', 'Serbia', 'Russia', 'Norway', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom'],
    'Currency': ['Bosnian Convertible Marka', 'Euro', 'Bulgarian Lev', 'Czech Koruna', 'Croatian Kuna', 'Danish Krone', 'Hungarian Forint', 'Icelandic Krona', 'Moldovan Leu', 'Macedonian Denar', 'Norwegian Krone', 'Polish Zloty', 'Romanian Leu', 'Serbian Dinar', 'Russian Ruble', 'Norwegian Krone', 'Swedish Krona', 'Swiss Franc', 'Turkish Lira', 'Ukranian Hryvnia', 'British Pound'],
    'Currency Symbol': ['BAM', 'EUR', 'BGN', 'CZK', 'HRK', 'DKK', 'HUF', 'ISK', 'MDL', 'MKD', 'NOK', 'PLN', 'RON', 'RSD', 'RUB', 'NOK', 'SEK', 'CHF', 'TRY', 'UAH', 'GBP'],
    'Value_in_INR': [44.55, 87.06, 44.53, 3.56, 11.58, 11.67, 0.22, 0.59, 4.53, 1.42, 7.64, 18.85, 17.50, 0.74, 0.83, 7.64, 7.51, 90.49, 3.03, 2.25, 100.40]
}

# Combine all datasets into one DataFrame
df = pd.concat([pd.DataFrame(data_asian), pd.DataFrame(data_middle_eastern), pd.DataFrame(data_european)], ignore_index=True)

# Visualize the data using a line graph
plt.figure(figsize=(15, 8))
plt.plot(df['Country'], df['Value_in_INR'], marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Exchange Rate (INR)')
plt.title('Exchange Rates of Different Currencies Against INR')
plt.grid(True)
plt.show()


