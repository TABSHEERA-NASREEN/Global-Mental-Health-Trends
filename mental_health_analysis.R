library(tidyverse)
df <- read.csv("data/cleaned_mental_health_data.csv")

ggplot(df %>% filter(Country == "India"), aes(x=Year, y=Value)) +
  geom_line(color='blue') +
  theme_minimal() +
  labs(title="Mental Health Value Over Time in India")
