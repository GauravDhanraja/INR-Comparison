# Load the ggplot2 library
library(ggplot2)
library(dplyr)

# Extract currency names from the first column of your dataset
currencies <- currency_data[, 1]
exchange_rate <- currency_data[,2]
inv_exchange_rate <- currency_data[,3]

currency_data_filtered <- currency_data %>%
  filter(Country != "Venezuelan Bolivar")
# Create a bar plot
print(ggplot(currency_data_filtered, aes(x = Country, y = "Exchange Rate to 1 INR", fill = `1.00 INR`)) +
        geom_tile() +
        scale_fill_gradient(low = "white", high = "skyblue") +  # Adjust color gradient as needed
        theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
        labs(title = "Exchange Rates against Indian Rupee (INR)",
             x = "Currency",
             y = ""))
