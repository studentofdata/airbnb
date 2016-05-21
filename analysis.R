#############################################
# Libraries needed


#############################################
# Pull in datasets

data <- read.csv("output.csv")
tourism_RO  <- read.csv("tour2014 - RO.csv", stringsAsFactors = FALSE)
tourism_CO  <- read.csv("tour2014 - CO.csv", stringsAsFactors = FALSE)
tourism_EMP <- read.csv("tour2014 - EMP.csv", stringsAsFactors = FALSE)
##############################################
# Constants:
# Airbnb Estimated Bookings (an exogenous figure used to estimate occ rate)
# Airbnb length, when minimum stay is less than 3 we assume 3 nights is the average stay
# BEA CPI estimate from 2016 to 2009 dollars
airbnbEst <- .4 #Estimated Bookings
airbnbLength <- 3
BEAcpi_2016_2009 <- 1.22064193461303


##############################################
# Subset Columns

col_vars <- c("R_Listname","R_Value","A_Availability","A_Cleaningfee","S_Accommodates","R_Reviews")
data_v1 <- data[,col_vars]

##############################################
# Munge the fields into appropriate formats and clean the availability field, *consider doing this in a pipeline*
data_v1$R_Value <- gsub("[$]","", data_v1$R_Value)
data_v1$R_Value <- as.numeric(as.character(data_v1$R_Value))
data_v1$A_Availability <- as.character(data_v1$A_Availability)
data_v1$A_Availability <- gsub("nights", "", data_v1$A_Availability)
data_v1$A_Availability <- gsub("night", "", data_v1$A_Availability)
data_v1$A_Availability <- gsub("varies", "", data_v1$A_Availability)
data_v1$A_Availability <- gsub("Fridays and Saturdays", "", data_v1$A_Availability)

data_v1$A_Availability <- gsub(" ", "", data_v1$A_Availability)
data_v1$A_Availability <- gsub(",", "", data_v1$A_Availability)
#Those who have minimum night stays, those are used to calculate length stays, all else assumes three nights
data_v1$A_Availability[nchar(data_v1$A_Availability) == 0] <- airbnbLength
data_v1$A_Availability[nchar(data_v1$A_Availability) > 2] <- substr(data_v1$A_Availability[nchar(data_v1$A_Availability) > 2],0,1)

data_v1$A_Availability <- as.numeric(data_v1$A_Availability)

#If someone doesn't have a review, give them exactly one so as to not exclude them from the analysis, their impacts are minimal
data_v1$R_Reviews[is.na(data_v1$R_Reviews)] <- 1

##############################################
# Calculate Columns of interest
# Estimated Bookings
# Nights per year
# Occupancy Rate
# Cap occupancy rate at 70%
# Re assign nights per year after adjusting for capped occupancy rate
# Total dollar value of airbnb travel stay in a year

data_v1$R_estimatedBookings <- data_v1$R_Reviews * airbnbEst
data_v1$R_nightsYear        <- data_v1$R_estimatedBookings * data_v1$A_Availability

data_v1$R_occRate           <- data_v1$R_nightsYear/365
data_v1$R_occRate[data_v1$R_occRate > .7] <- .7

data_v1$R_nightsYear        <- data_v1$R_occRate * 365

data_v1$R_annSpend          <- data_v1$R_nightsYear * data_v1$R_Value

tot_airbnb_spend <- sum(data_v1$R_annSpend)
tot_airbnb_spend <- tot_airbnb_spend/BEAcpi_2016_2009

##############################################
# Now that we have the total spend of airbnb travels in the same
# dollars as our satellite accounts, lets calculate the total amount
# spent during travel

tourism_RO$Commodity <- as.character(tourism_RO$Commodity)
# Convert strings to numeric and remove commas
tourism_RO$Direct_output_millions <- as.numeric(gsub(",","",tourism_RO$Direct_output_millions))
tourism_RO$Real_output_millions_2009 <- as.numeric(gsub(",","",tourism_RO$Real_output_millions_2009))

total_output <- tourism_RO[tourism_RO$Commodity == "Total", c("Real_output_millions_2009")]
tourism_RO$output_shares <- tourism_RO$Real_output_millions_2009/total_output

traveler_accomodations <- subset(tourism_RO, Commodity == "Traveler accommodations", select = c(Real_output_millions_2009, output_shares))

#Total economic contributions
economic_total <- tot_airbnb_spend/traveler_accomodations[,c("output_shares")]


#Column for economic contributions by industry
tourism_RO$economic_airbnb_output_totals <- tourism_RO$output_shares*economic_total





