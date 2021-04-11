## This class module is implemented to check whether two countries are neighboring or not
## Input : Wikipedia Page URL of Two Countries (String) : (Country_1_url, Country_2_url)
## Output : True or False (Boolean) : True means Neighboring Countries
## Time Complexity : O(M*N) where M = No. of paragraphs in Geography and Introduction Section, N = No. of tokens to search matching (25 : Default)
## No. of Tokens : Can be varied from Config File : Search_tokens_list.txt or __search_tokens_list (Prediction Accuracy may also vary)
## Author : Soumyadeep Choudhury
## Email Id : papan1993@gmail.com

from Check_Neighboring_Country_Library.KMP_module import KMP_class
from Check_Neighboring_Country_Library.Scrapper_module import Wiki_Scrapper_class

class Neighbor_Country_class:

    ## All the tokens for the pattern matching : private
    __search_tokens_list = [" borders "," bordered "," surrounded "," maritime border "," maritime boundary "," maritime borders "," maritime boundaries "," neighboring islands "," nearest mainland "," border "," bodering "," nearby "," neighboring island "," north "," south "," east "," west "," northeast "," northwest "," southeast "," southwest "," seperated "," vicinity "," covers "," apart "]

    ## default constructor
    def __init__(self):
        pass

    ## function to verify my visited lines in a paragraph : Private
    def __verify_visited_lines(self, visit_list, index):

        ret_flag = False

        if (len(visit_list) != 0):
            for i in range(0, len(visit_list), 1):
                if (index >= visit_list[i][0]) and (index <= visit_list[i][1]):
                    ret_flag = True
                    break

        return ret_flag

    ## function to extract the line where the pattern matching found and verify the neighboring country name
    def __extract_country_lines(self, input_paragraph, pattern_index_list, visited_lines_index, find_country_name, para_j):

        find_flag = False

        visit_para_array = []
        if (para_j in visited_lines_index.keys()):
            visit_para_array = visited_lines_index[para_j]

        ####
        for index in pattern_index_list:

            ## check whether previously visited the same line or not
            visit_flag = self.__verify_visited_lines(visit_para_array, index)

            if (visit_flag == False):
                pre_para_index = -1
                pre_found = False
                post_found = False
                post_para_index = -1
                temp_index_list = []

                ### find the pre-index and post-index dot
                for i in range(index-1, 0, -1):
                    if (input_paragraph[i] == "."):
                        pre_para_index = (i+2)
                        pre_found = True
                        break

                if (pre_found == False):
                    pre_para_index = 1

                for i in range(index, len(input_paragraph), 1):
                    if (input_paragraph[i] == "."):
                        post_para_index = (i)
                        post_found = True
                        break

                if (post_found == False):
                    pre_para_index = len(input_paragraph) - 1

                ## extracting the exact line that contains the country name
                each_para_line = input_paragraph[pre_para_index:post_para_index]
                temp_index_list.append(pre_para_index)
                temp_index_list.append(post_para_index)

                ### update the visit map
                visit_para_array.append(temp_index_list)
                visited_lines_index[para_j] = visit_para_array

                ## check the country name exists or not
                if (each_para_line.find(find_country_name) != -1):
                    find_flag = True
                    break

        return find_flag, visited_lines_index

    def __pattern_matching_algorithm(self, input_data_list, find_country_name, token_list):

        found_neighbor = False
        visited_lines_index = {}

        ## verify for token with decreasing priority
        for i in range(0, len(token_list), 1):

            each_token = token_list[i]

            ## iterate in extracted paragraphs
            for j in range(0, len(input_data_list), 1):

                each_para = input_data_list[j]

                ## execute KMP pattern matching to index : where it is found
                kmp_object = KMP_class()
                pattern_index_list = kmp_object.kmp_algorithm(each_token, each_para)

                if (len(pattern_index_list) != 0):

                    ## exctract and verify the paragraph
                    find_flag, visited_lines_index = self.__extract_country_lines(each_para, pattern_index_list, visited_lines_index, find_country_name, j)

                    if (find_flag == True):
                        found_neighbor = True
                        break

            if (found_neighbor == True):
                break

        return found_neighbor

    def is_neighboring_country(self, url_link_1, url_link_2):

        neighboring_country_flag = False

        ### This section can be used if you want to give input of the tokens from a text file : just uncomment it

        # curr_dir_path = os.path.abspath(os.path.dirname(__file__))
        # token_file_path = str(curr_dir_path) + "/Config/Search_tokens_list.txt" ## make Config folder and put the token file in it
        #file1_readlines = []
        #token_file = []

        # try :
        #     file1 = open(token_file_path, "r")
        #     if file1 is not None:
        #         file1_readlines = file1.readlines()
        #
        #     file1.close()
        #
        #     for each_line in file1_readlines:
        #         each_line = each_line.replace("\n", "")
        #         each_line = " " + each_line + " "
        #         token_file.append(each_line)
        ##############

        try :
            scrapper_object = Wiki_Scrapper_class()

            country_name_1 = scrapper_object.extract_name_options(url_link_1, option=2)
            country_name_2 = scrapper_object.extract_name_options(url_link_2, option=2)

            ### extract the Geography and Introduction Paragraphs : ordered
            para_order_country_1 = scrapper_object.scrapping_wikipedia(url_link_1)

            if (para_order_country_1 != None):
                print(" Executing Country-based Pattern Matching Algorithm ")
                neighboring_country_flag = self.__pattern_matching_algorithm(para_order_country_1, country_name_2, Neighbor_Country_class.__search_tokens_list)

                ## If the result is False from the first wikipedia article
                if (neighboring_country_flag != True):

                    print(" -- Neighboring Country Flag : " + str(neighboring_country_flag) + " : " + country_name_2 + " not found in Wiki article : " + country_name_1 + " -- ")
                    print(" -- Cross - Checking the Neighboring Country Data in the Second Country Wiki Article -- ")
                    para_order_country_2 = scrapper_object.scrapping_wikipedia(url_link_2)

                    if (para_order_country_2 != None):
                        print(" Executing Country-based Pattern Matching Algorithm ")
                        neighboring_country_flag = self.__pattern_matching_algorithm(para_order_country_2, country_name_1,
                                                                              Neighbor_Country_class.__search_tokens_list)

            return neighboring_country_flag

        except (IndentationError, IOError, BaseException, BrokenPipeError, AttributeError, ArithmeticError) as e:
            print (" An error found in the class I/O, Arthimatic, Indentation or Broken Pipe ")
            raise SystemExit(e)

        # except (FileNotFoundError, IOError) as e:
        #     print(" Search_tokens_list file not found : Wrong or Wrong Path ")
        #     raise SystemExit(e)