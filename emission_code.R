# emission_code
# Justin Pizano

# Libraries
library(icesTAF)
library(writexl)

# Make folder
mkdir("emission_folder")

# Set new working directory for the folder
setwd(paste(getwd(), "/emission_folder", sep = ""))

# The imported dataset (use your own directory, as the data was obtained
# through the RStudio IDE method)
GHG <- read.csv("~/All_Backups_etc/SupplyChainGHGEmissionFactors_v1.2_NAICS_CO2e_USD2021.csv")

# The length of the data
data_len <- length(GHG$GHG)

# Data name variables
margins = GHG$Margins.of.Supply.Chain.Emission.Factors
emissions_without = GHG$Supply.Chain.Emission.Factors.without.Margins
emissions_with = GHG$Supply.Chain.Emission.Factors.with.Margins

## Linear model summaries
# Without Margins
summary(lm(margins ~ emissions_without))

# With Margins
summary(lm(margins ~ emissions_with))

# Both with Margins and without, including interaction
summary(lm(margins ~ 
     emissions_without * emissions_with)
)

# ANOVA: Emission Factors: With or without margins
summary(aov(emissions_with ~ emissions_without))

# Average of Margins
sum(margins)/data_len

# Average of Emission Factors without Margins
sum(emissions_without)/data_len

# Average of Emission Factors with Margins
sum(emissions_with)/data_len

# Running t-test on each of Margins, Emission Factors with Margins,
# and those without Margins.
# Margins
margin_t <- t.test(emissions_with)

# No Margin Emissions
without_t <- t.test(emissions_without)

# Emissions with Margins
with_t <- t.test(emissions_with)

# Create lists
companies <- {}
margin_pvalues <- {}
em_without_pvalues <- {}
em_with_pvalues <- {}

# Instantiate increment variable
num = 1

while(num <= data_len){
  # Companies
  companies[num] <- GHG$X2017.NAICS.Title[num]
  # P-values: Margins
  margin_pvalues[num] <- t.test(
    margins, mu = margins[num])$p.value
  # P-values: Emission Factors without Margins
  em_without_pvalues[num] <- t.test(
    emissions_without,
    mu = emissions_without[num])$p.value
  # P-values: Emission Factors with Margins
  em_with_pvalues[num] <- t.test(
    emissions_with,
    mu = emissions_with[num])$p.value
  # Increment
  num = num + 1
}

# Data frame: Emission Data
emission_data <- data.frame(
  companies, margins, margin_pvalues, emissions_without,
  em_without_pvalues, emissions_with, em_with_pvalues)


# Data frame column names
colnames(emission_data) <- c(
  "Companies", "Margin Value", "P-value: Margin", 
  "Emission Factor without Margin", "P-value: E.F., no M",
  "Emission Factors with Margin", "P-value: E.F., with M")


# Write a csv of the data
write.csv(emission_data, "emission_data")
# Write an excel file of the same data
write_xlsx(emission_data, path = paste(getwd(), "/emission_data.xlsx", sep = ""))




