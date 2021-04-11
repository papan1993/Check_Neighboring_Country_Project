## This Class Module is to implement KMP algorithm
## Input : Input Pattern (String), Input Text (String)
## Output : Output Pattern Matched Indexes (List)
## Time Complexity : O(M*N) where M=len(Input Text) and N=len(Input Pattern)
## Author : Soumyadeep Choudhury
## Email Id : papan1993@gmail.com

class KMP_class:

    ## class constructor
    def __init__(self):
        pass

    ## Function to create the LPS array : Longest Prefix of the Suffix : Private Function
    def __lps_create(self, inp_patt):
        len_lps = len(inp_patt)
        final_lps = [0] * len_lps

        j = 0  ## pattern len index
        i = 1  ## increment index : location of lps

        while (i < len_lps):

            ## if prefix=postfix match found
            if (inp_patt[i] == inp_patt[j]):
                final_lps[i] = j + 1
                j = j + 1
                i = i + 1

            ## no match between prefix character and postfix character
            else:
                if (j != 0):
                    j = final_lps[j - 1]

                else:
                    i = i + 1

        return final_lps

    ## Function to find the Matching indexes using the LPS array
    def kmp_algorithm(self, inp_patt, inp_text):

        ## compute lps
        final_lps = self.__lps_create(inp_patt)

        len_patt = len(inp_patt)
        len_text = len(inp_text)

        ### pattern matching
        i = 0  # text index
        j = 0  # pattern index
        match_index_list = []  ## match positions list

        while (i < len_text):

            ## if any matches found
            if (inp_patt[j] == inp_text[i]):
                i = i + 1
                j = j + 1

            ## if full pattern match found
            if (j == len_patt):
                temp_match_index = i - j
                match_index_list.append(temp_match_index)
                j = final_lps[j - 1]

            ## no match found : keep searching
            elif ((i < len_text) and (inp_text[i] != inp_patt[j])):
                if (j != 0):
                    j = final_lps[j - 1]
                else:
                    i = i + 1

        return match_index_list
