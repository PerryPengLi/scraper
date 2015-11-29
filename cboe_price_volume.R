price = read.csv("data/cboe_price_3years.csv")
volume = read.csv("data/cboe_volume_3years.csv")

f20 <- rep(1/20, 20)
mva_volume <- filter(volume$Sum_of_All_Products_Volume, f20, method = "convolution", sides=2)[10:723]
mva_price <- filter(price$Adj.Close, f20, method = "convolution", sides=2)[10:723]

cor(mva_volume, mva_price)

linear_model = lm(mva_price ~ mva_volume)
summary(linear_model)