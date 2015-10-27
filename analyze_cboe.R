#source("http://bit.ly/dasi_inference")

CBOE_2015Q2 = read.csv("cboe_volume_2015q2.csv")

summary(CBOE_2015Q2)

total_Option_volume_q2 = sum(CBOE_2015Q2$Sum_of_All_Products_Volume)
total_Equity_LEAPS_Volume_q2 = sum(CBOE_2015Q2$Equity_LEAPS_Volume)
total_Weeklys_Options_Volume_q2 = sum(CBOE_2015Q2$Weeklys_Options_Volume)


CBOE_2014Q3 = read.csv("cboe_volume_2014q3.csv")
CBOE_2014Q2 = read.csv("cboe_volume_2014q2.csv")
summary(CBOE_2014Q2)

total_Option_volume_q2 = sum(CBOE_2014Q2$Sum_of_All_Products_Volume)
total_Equity_LEAPS_Volume_q2 = sum(CBOE_2014Q2$Equity_LEAPS_Volume)
total_Weeklys_Options_Volume_q2 = sum(CBOE_2014Q2$Weeklys_Options_Volume)

