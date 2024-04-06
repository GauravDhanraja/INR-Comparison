import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Define your data
data = {
    'Country': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bangladesh', 'Cambodia', 'China', 'Georgia', 'Hong Kong', 'Indonesia', 'Japan', 'Kazakhstan', 'Laos', 'Malaysia', 'South Korea', 'Sri Lanka', 'Maldives', 'Pakistan', 'Philippines', 'Thailand', 'Taiwan', 'Vietnam', 'Bahrain', 'United Arab Emirates', 'Saudi Arabia', 'Oman', 'Israel', 'Iraq', 'Iran', 'Jordan', 'Kuwait', 'Lebanon', 'Qatar', 'Libya', 'Bosnia', 'European Union', 'Bulgaria', 'Czech Republic', 'Croatia', 'Denmark', 'Hungary', 'Iceland', 'Moldova', 'Macedonia', 'Norway', 'Poland', 'Romania', 'Serbia', 'Russia', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'United States', 'Canada', 'Aruba', 'Barbados', 'Bermuda', 'Bahamas', 'Dominica', 'Jamaica', 'Mexico', 'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Columbia', 'Peru', 'Paraguay', 'Uruguay', 'Venezuela', 'South Africa', 'Egypt', 'Ghana', 'Gambia', 'Kenya', 'Morocco', 'Mauritius', 'Namibia', 'Nigeria', 'Seychelles', 'Tunisia', 'Uganda', 'Central Africa', 'Australia', 'Fiji', 'New Zealand', 'CPF'],
    'Currency': ['Afghan Afghani', 'Armenian Dram', 'Azerbaijani Manat', 'Bangladeshi Taka', 'Cambodian Riel', 'Chinese Yuan', 'Georgian Lari', 'Hong Kong Dollar', 'Indonesian Rupiah', 'Japanese Yen', 'Kazakhstani Tenge', 'Lao Kip', 'Malaysian Ringgit', 'South Korean Won', 'Sri Lankan Rupee', 'Maldivian Rufiyaa', 'Pakistani Rupee', 'Philippine Peso', 'Thai Baht', 'Taiwanese Dollar', 'Vietnamese Dong', 'Bahraini Dinar', 'Emirati Dirham', 'Saudi Arabian Riyal', 'Omani Rial', 'Israeli Shekel', 'Iraqi Dinar', 'Iranian Rial', 'Jordanian Dinar', 'Kuwaiti Dinar', 'Lebanese Pound', 'Qatari Riyal', 'Libyan Dinar', 'Bosnian Convertible Marka', 'Euro', 'Bulgarian Lev', 'Czech Koruna', 'Croatian Kuna', 'Danish Krone', 'Hungarian Forint', 'Icelandic Krona', 'Moldovan Leu', 'Macedonian Denar', 'Norwegian Krone', 'Polish Zloty', 'Romanian Leu', 'Serbian Dinar', 'Russian Ruble', 'Swedish Krona', 'Swiss Franc', 'Turkish Lira', 'Ukranian Hryvnia', 'British Pound', 'United States Dollar', 'Canadian Dollar', 'Aruban/Dutch Guilder', 'Bajan Dollar', 'Bermudian Dollar', 'Bahamian Dollar', 'Dominican Peso', 'Jamaican Dollar', 'Mexican Peso', 'Argentine Peso', 'Bolivian Boliviano', 'Brazilian Real', 'Chilean Peso', 'Colombian Peso', 'Peruvian Sol', 'Paraguayan Guaraní', 'Uruguayan Peso', 'Venezuelan Bolívar', 'South African Rand', 'Egyptian Pound', 'Ghanian Cedi', 'Gambian Dalasi', 'Kenyan Shilling', 'Moroccan Dirham', 'Mauritian Rupee', 'Namibian Dollar', 'Nigerian Naira', 'Seychellois Rupee', 'Tunisian Dinar', 'Ugandan Shilling', 'CFA Franc', 'Australian Dollar', 'Fijian Dollar', 'New Zealand Dollar', 'CPF'],
    'Currency Symbol': ['AFN', 'AMD', 'AZN', 'BDT', 'KHR', 'CNY', 'GEL', 'HKD', 'IDR', 'JPY', 'KZT', 'LAK', 'MYR', 'KRW', 'LKR', 'MVR', 'PKR', 'PHP', 'THB', 'TWD', 'VND', 'BHD', 'AED', 'SAR', 'OMR', 'ILS', 'IQD', 'IRR', 'JOD', 'KWD', 'LBP', 'QAR', 'LYD', 'BAM', 'EUR', 'BGN', 'CZK', 'HRK', 'DKK', 'HUF', 'ISK', 'MDL', 'MKD', 'NOK', 'PLN', 'RON', 'RSD', 'RUB', 'SEK', 'CHF', 'TRY', 'UAH', 'GBP', 'USD', 'CAD', 'AWG', 'BBD', 'BMD', 'BSD', 'DOP', 'JMD', 'MXN', 'ARS', 'BOB', 'BRL', 'CLP', 'COP', 'PEN', 'PYG', 'UYU', 'VEF', 'ZAR', 'EGP', 'GHS', 'GMD', 'KES', 'MAD', 'MUR', 'NAD', 'NGN', 'SCR', 'TND', 'UGX', 'XAF', 'AUD', 'FJD', 'NZD', 'XPF'],
    'Value': [1.06, 0.21, 48.95, 0.75, 0.020, 11.37, 31.11, 10.63, 0.0053, 0.56, 0.17, 0.0041, 17.61, 0.061, 0.25, 5.42, 0.29, 1.46, 2.24, 2.57, 0.0034, 220.72, 22.65, 22.18, 216.11, 21.64, 0.063, 0.0020, 117.29, 268.93, 0.0055, 22.85, 16.91, 44.55, 87.06, 44.53, 3.56, 11.58, 11.67, 0.22, 0.59, 4.53, 1.42, 7.64, 18.85, 17.50, 0.74, 0.83, 7.51, 90.49, 3.03, 2.25, 100.40, 83.21, 60.68, 46.23, 40.93, 83.21, 82.68, 1.45, 0.53, 4.69, 0.24, 11.97, 16.43, 0.092, 0.020, 21.82, 0.011, 2.16, 0.0000241856, 4.49, 2.65, 7.29, 1.38, 0.60, 8.23, 1.80, 4.49, 0.18, 6.21, 26.66, 0.022, 0.14, 56.31, 37.28, 51.04, 0.74]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare the data for modeling
X = df['Value'].values.reshape(-1, 1)  # Independent variable (Value)
y = df.index.values.reshape(-1, 1)  # Target variable (Index)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
r_squared = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print the evaluation metrics
print(f'R-squared: {r_squared}')
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.title('Comparison of INR Exchange Rate with Other Currencies')
plt.xlabel('INR Exchange Rate')
plt.ylabel('Currency Index')
plt.legend()
plt.grid(True)
plt.show()


