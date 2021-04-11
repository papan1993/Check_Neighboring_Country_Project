## This Class Module is implemented to extract Introduction and Geography Sections from Wikipedia
## Input : wikipedia of a country URL link (String)
## Output : All the paragraphs in Introduction and Wikipedia Section (List)
## Time Complexity : O(N) where N is the total number of paragraphs/sections available in wikipedia
## Author : Soumyadeep Choudhury
## Email Id : papan1993@gmail.com

import bs4
import requests

class Wiki_Scrapper_class:

    ## class constructor
    def __init__(self):
        pass

    ### Function to extract country name and append 'The' with country name
    def extract_name_options(self, url_link, option):
        url_split = url_link.split("/")
        len_pos = len(url_split) - 1
        temp_name = url_split[len_pos]

        ## Replace underscore from the country name with empty space
        if (temp_name.find("_") != -1):
            temp_name = temp_name.replace("_", " ")

        country_name_1 = temp_name   ## original country name
        country_name_2 = "The " + temp_name ## 'The' country name : beacuse some of the countries uses 'The' in wiki

        if (option == 1):
            return country_name_1, country_name_2
        elif (option == 2):
            return country_name_1

    ## Function to extract geography and introduction section paragraphs
    def scrapping_wikipedia(self, url_link):

        ## extract the country names
        country_name_1, country_name_2 = self.extract_name_options(url_link, option=1)

        try:

            ## extract data from wikipedia from the URL link
            extract_wiki = requests.get(url_link)

            ## verify data availability in wikipedia
            if extract_wiki is not None:

                ## wikipedia html parser
                soup = bs4.BeautifulSoup(extract_wiki.content, 'html.parser')

                ## extract the full content data from the html using div
                full_content = soup.find('div', id="bodyContent").text
                paragraphs_unordered = full_content.split("\n")

                ### initialized variables
                paragraphs_ordered = [] ## list to store the final paragraphs of introduction and geography
                start_section1_flag = 0 ## control introduction section
                start_section2_flag = 0 ## control geography section
                token_count = 0
                len_country_name_1 = len(country_name_1)
                len_country_name_2 = len(country_name_2)
                ## control to maintain count and exit code if retrieved required data : saves unnecessary iterations and time
                section_count = 1
                extract_token = ''
                exception_count = 0

                ## each paragraph or lines section in the whole wikipedia content list : extract the main data and remove the rest
                for i in range(0, len(paragraphs_unordered), 1):

                    each_para = paragraphs_unordered[i]

                    ## remove empty string
                    if (len(each_para) >= 1):

                        ### Extract the Introduction Section from the wikipedia
                        if (section_count == 1):

                            ## start extraction of introduction section
                            if ((country_name_1 == each_para[:len_country_name_1]) or (country_name_2 == each_para[:len_country_name_2])):
                                start_section1_flag = 1
                                paragraphs_ordered.append(each_para)

                            ## stop extraction of introduction section
                            elif (("Contents" == each_para) and (start_section1_flag == 1)):
                                section_count = section_count + 1
                                start_section1_flag = 0

                            ## continue extraction of introduction section
                            elif (start_section1_flag == 1):
                                paragraphs_ordered.append(each_para)

                        ### Find the token from contents : next after geography (to avoid extracting un-necessary paragraphs/sections)
                        elif (section_count == 2):

                            if (each_para.find("Geography") != -1):
                                token_count = 1

                            ### Got the end token for Geography Section
                            elif (token_count == 1):
                                temp_token = each_para.split(" ")

                                for i in range(1, len(temp_token), 1):
                                    if (i == 1):
                                        extract_token = extract_token + temp_token[i]
                                    else:
                                        extract_token = extract_token + ' ' + temp_token[i]

                                token_count = 0
                                section_count = section_count + 1


                        ### Extract the Geography Section from wikipedia
                        elif (section_count == 3):

                            ## start extracting geography section signal
                            if (('Geography' == each_para) or ('Geography[edit]' == each_para) or ('Geography and natural history' == each_para)):
                                start_section2_flag = 1

                            ## stop extracting geography section signal :option1
                            elif ((each_para == extract_token) and (start_section2_flag == 1)):
                                section_count = section_count + 1
                                start_section2_flag = 0

                            ## stop extracting geography section signal :option2
                            elif ((each_para == (extract_token+'[edit]')) and (start_section2_flag == 1)):
                                section_count = section_count + 1
                                start_section2_flag = 0

                            ## extract geography section : continue
                            elif (start_section2_flag == 1):
                                paragraphs_ordered.append(each_para)

                        ## break from extraction, reuired sections collected
                        elif (section_count == 4):

                            if (i <= 350):

                                if (each_para == "Political geography"):
                                    exception_count = 1

                                elif (each_para == "Politics"):
                                    exception_count = 0
                                    break

                                elif (exception_count == 1):
                                    paragraphs_ordered.append(each_para)

                            else:
                                break

                print(" Introduction and Geography from Wikipedia Extracted for Country : ", country_name_1)
                return paragraphs_ordered

            else:
                ## requests failed to receive any information from wikipedia page
                print(" No data found in the wikipedia ! in URL : ", url_link)
                return None

        ## exception raised if failed to connect the url
        except (requests.exceptions.RequestException, requests.ConnectionError) as e:
            print(" Failed to connect to the URL : ", url_link)
            raise SystemExit(e)