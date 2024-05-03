library(ggplot2)

data <- read.csv('./data/current_data.csv')

lrg_plot <- ggplot(data, aes(x=INR, y=inv_INR)) +
            geom_point() +
            geom_text(aes(label = Country), 
                nudge_x = 1, nudge_y = 0.5, 
                check_overlap = T
            ) +
            scale_x_continuous(limits = c(0, 50)) +
            scale_y_continuous(limits = c(0, 120))

sml_plot <- ggplot(data, aes(x=INR, y=inv_INR)) +
            geom_point() +
            geom_text(aes(label = Country),
                nudge_x = 0.015, nudge_y = 0.2, 
                check_overlap = F
            ) +
            scale_x_continuous(limits = c(0, 0.6)) +
            scale_y_continuous(limits = c(0, 25))

ggsave("./plots/lrgplot.png", plot = lrg_plot, width = 32, height = 20, dpi = 1000)
ggsave("./plots/smlplot.png", plot = sml_plot, width = 32, height = 20, dpi = 1000)

