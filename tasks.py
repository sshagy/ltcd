def repeated_substring_pattern(s: str | list):
    """Given a string s, check if it can be constructed by taking 
    a substring of it and appending multiple copies of the substring together.

    >>> assert repeated_substring_pattern('abcabcabcabc')
    >>> assert repeated_substring_pattern([1,2,3,1,2,3,4, 1,2,3,1,2,3,4])
    """
    sl = len(s)
    for i in range(1, sl // 2 + 1):
        # if not any(s.split(s[:i])):  # simple string solution, but not optimal 
        #     return True
        
        if sl % i != 0: 
          continue
          
        ptrn = s[:i]
        # print(f'Trace #{i}:', ptrn, list(ptrn == s[j*i:(j+1)*i] for j in range(1, sl // i)))
        if all(ptrn == s[j*i:(j+1)*i] for j in range(1, sl // i)):
            return True  # , ptrn
    return False
  
def find_peak_point(arr) :
    """https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
    need log(n)

    >>> assert find_peak_point([ 1, 3, 20, 4, 1, 0 ]) == 20
    """
    n = len(arr)

    # first or last element is peak element
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
  
    # check for every other element
    for i in range(1, n - 1) :
  
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
    
    return None
