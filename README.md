# CHECK NEIGHBORING COUNTRY : version : 1.0.0

** Note : PLEASE READ THE INSTRUCTIONS CAREFULLY BEFORE EXECUTING IT

** "PART - A" -> Theory : The Library is designed to check whether two countries are neighbors or not.
--------- ASSUMPTIONS TO DESIGN THE LOGIC:
1) Only information available in the wikipedia article of the country is used to validate the logic
2) Maritime Borders or Ocean Neighbors are also considered true in the logic
3) 25 tokens are used to extract and match the neighboring countries
4) No Latitude or Longitude or GeoLocation information is used to verify the logic
5) Only Geography and Introduction sections are considered to detect the neighboring country information

#################################

** "PART - B" -> Project Design **
1) It is designed as a pure python3 package and library such that it can be installed and run from any machine
2) wheel file in the "Check_Neighboring_Country_Project/dist/" is automatically generated while following setup commands 
   which can be easily used to install in any environment or machine as it creates an image file.
3) Project Structure:
    __/Check_Neighboring_Country_Project
         |__Check_Neighboring_Country_Library
            |____init__.py
            |__KMP_module.py
            |__NeighboringCountry_module.py
            |__Scrapper_module.py
         |__run_code
            |__Run_main.py
         |__tests
            |____init__.py
            |__test_check_neighbor_country.py
         |__setup.py
         |__README.md

4) You can Run the projects in 2 ways : 
   i) Directly use the given wheel file to install in system python3 lib 
   ii)(Recommended Way) Run setup and install the package in the system with test cases
   
#######################################################
   
** "PART - C" -> INSTALLATION AND EXECUTION **
------------------------------------------------------
1) Base Pre-required Dependencies or Libraries : 
    
    -> "sudo apt-get install python3 python3-pip python3-setuptools wheel"
   
2) * Optional: If you just want to install the package and don't have the full-project zip, then install the following dependent libraries
   
    -> "sudo pip3 install requests bs4"

3) If you have the project package wheel file : Directly install it from the location where the wheel is downloaded

    -> "sudo pip3 install Check_Neighboring_Country_Library-1.0.0-py3-none-any.whl"
    
4) Unzip and Go to the project folder (If you downloaded the whole archive project):

    -> "cd /system_path/Check_Neighboring_Country_Project/"
   
5) Run the setup file with wheel : If you don't have the wheel file, otherwise install like step-3

    -> "chmod +x setup.py"                     ##(To make executable)
    -> "python3 setup.py bdist_wheel"
   
6) Go to the generated dist folder to install the package :

    -> "cd /system_path/Check_Neighboring_Country_Project/dist/"
    -> "sudo pip3 install Check_Neighboring_Country_Library-1.0.0-py3-none-any.whl"
   
7) Run the setup with testcases to run all the 10 test cases:

    -> "cd /system_path/Check_Neighboring_Country_Project/"
    -> "python3 setup.py pytest"
   
8) Run the main code to manually give URL input and check the results

    -> "cd /system_path/Check_Neighboring_Country_Project/run_code/"
    -> "python3 Run_main.py"
   
11) To uninstall the library / package from the system : Run the following command :
    
    -> "sudo pip3 uninstall Check-Neighboring-Country-Library"

10) To use the library universally in any machine and code : Follow the steps after installing the library :

    ## import the library
    from Check_Neighboring_Country_Library.NeighboringCountry_module import Neighbor_Country_class
    
    ## create an object
    check_country_object = Neighbor_Country_class()
   
    ## Input (String : 2 country URL's)
    url_link_1 = "https://en.wikipedia.org/wiki/Indonesia"
    url_link_2 = "https://en.wikipedia.org/wiki/China"
   
    ## Get the result in Boolean : True or False
    result_flag = check_country_object.is_neighboring_country(url_link_1, url_link_2)

########################  CONTACT FOR BUGS  OR INFORMATION  ####################

Name : Soumyadeep Choudhury
Email : papan1993@gmail.com

################  END  ###############

