library(ggplot2)

data <- read.csv('currency_data.csv')

INR_heatmap <- ggplot(data, aes(x = Country, y = Country, fill = 'INR')) +
                geom_tile() + 
                scale_fill_gradient(low="white", high="red") +
                theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
                labs(title="Heatmap of 1.00 INR") +
                theme_minimal()

ggsave("heatmap.png", INR_heatmap)
