'''
Given string s of length n, and integer k where k is factor of n:

Split s into n/k subsegments that are each unique and separated by \n

'''


def merge_the_tools(string, k):
    substring_len = len(string) // k
    start,end = 0,k
    for i in range(substring_len):
        substring = list(string[start:end])

        dict = [] #empty dict

        for j in range(len(substring)):
            if (substring[j] not in dict):
                dict.append(substring[j])

        u = "".join(dict)
        print(u)

        start += k
        end += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
