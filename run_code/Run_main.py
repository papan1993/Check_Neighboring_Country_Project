from Check_Neighboring_Country_Library.NeighboringCountry_module import Neighbor_Country_class

def check_neighbor_country_function():
    ## Input Manual
    #url_link_1 = "https://en.wikipedia.org/wiki/Indonesia"
    #url_link_2 = "https://en.wikipedia.org/wiki/China"

    ## Run Time Input
    print(" --- Welcome To Program to Check : Two Countries are Neighbors or Not --- ")
    url_link_1 = input(" Enter the URL for country - 1 : ")
    url_link_2 = input(" Enter the URL for country - 2 : ")
    print(" --- Executing --- ")

    ## main code
    check_country_object = Neighbor_Country_class()
    result_flag = check_country_object.is_neighboring_country(url_link_1, url_link_2)

    if (result_flag == True):
        print("\n *** Result -> Both the countries are Neighbors : " + str(result_flag) + " : " + str(url_link_1) + " and " + str(url_link_2))

    else:
        print(" *** Result -> Both the countries are not Neighbors : " + str(result_flag) + " : " + str(url_link_1) + " and " + str(url_link_2))

#####################################
if __name__ == '__main__':

    check_neighbor_country_function()
    print(" --- Exiting the Program --- ")
    exit(0)
