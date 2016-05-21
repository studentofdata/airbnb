# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbItem(scrapy.Item):

    AboutListing = scrapy.Field()





    # Result Info
    R_Hostname   = scrapy.Field()
    R_Hostprofile = scrapy.Field()
    R_Listname = scrapy.Field()

    R_Value        = scrapy.Field()
    R_Roomtype   = scrapy.Field()
    R_Reviews    = scrapy.Field()
    R_Review_rating = scrapy.Field()

    #Space Info
    S_Proptype = scrapy.Field()
    S_Accommodates = scrapy.Field()
    S_Bedrooms = scrapy.Field()
    S_Bathrooms = scrapy.Field()
    S_Numbeds = scrapy.Field()
    S_Bedtype = scrapy.Field()
    S_Checkin = scrapy.Field()
    S_Checkout = scrapy.Field()




    #Accomodations Info
    A_Cleaningfee = scrapy.Field()
    A_Availability = scrapy.Field()











    ### Unused


    # R_hostimage  = scrapy.Field()


    # A_Kitchen = scrapy.Field()
    # A_Internet = scrapy.Field()
    # A_TV = scrapy.Field()
    # A_Essentials = scrapy.Field()
    # A_Shampoo = scrapy.Field()
    # A_Heat = scrapy.Field()
    # A_AC = scrapy.Field()
    # A_Washer = scrapy.Field()

    # A_Dryer = scrapy.Field()
    # A_Parking = scrapy.Field()
    # A_Internet = scrapy.Field()
    # A_CableTV = scrapy.Field()
    # A_Breakfast = scrapy.Field()
    # A_Pets = scrapy.Field()
    # A_FamilyFriendly = scrapy.Field()
    # A_Events = scrapy.Field()
    # A_Smoking = scrapy.Field()
    # A_Wheelchair = scrapy.Field()
    # A_Elevator = scrapy.Field() 
    # A_Fireplace = scrapy.Field()
    # A_Intercom = scrapy.Field()
    # A_Doorman = scrapy.Field()
    # A_Pool = scrapy.Field()
    # A_HotTub = scrapy.Field()
    # A_Gym = scrapy.Field()
    # A_SmokeDetector = scrapy.Field()
    # A_CarbonMonoxDetector = scrapy.Field()
    # A_FirstAidKit = scrapy.Field()
    # A_SafetyCard = scrapy.Field()
    # A_FireExt = scrapy.Field()

    # R_loc_lat    = scrapy.Field()
    # R_loc_lng    = scrapy.Field()


    pass
