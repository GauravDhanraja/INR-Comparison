library(ggplot2)

data <- read.csv('./data/current_data.csv')

countries <- data$Country
inr <- data$INR

lrg_plot <- ggplot(data, aes(x=INR, y=inv_INR)) +
            geom_point() +
            geom_text(
                label=rownames(data), 
                nudge_x = 0.25, nudge_y = 0.25, 
                check_overlap = T
            ) +
            scale_x_continuous(limits = c(0, 50)) +
            scale_y_continuous(limits = c(0, 120))

sml_plot <- ggplot(data, aes(x=INR, y=inv_INR)) +
            geom_point() +
            geom_text(
                label=rownames(data), 
                nudge_x = 0.01, nudge_y = 0.1, 
                check_overlap = T
            ) +
            scale_x_continuous(limits = c(0, 0.7)) +
            scale_y_continuous(limits = c(0, 25))

ggsave("./plots/lrgplot.png", plot = lrg_plot, width = 20, height = 14, dpi = 1000)
ggsave("./plots/smlplot.png", plot = sml_plot, width = 20, height = 20, dpi = 1000)

