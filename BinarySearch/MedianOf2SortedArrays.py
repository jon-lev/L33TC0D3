class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #Problem asks for O(log(m+n)), means binary search on smaller array
        #Merging array would be O(m+n)
    #Odd cases: Partition left and right to have same number of elements and grab middle
    #Even cases: Partition to have same number of elements and grab right most from leftP and left-most in rightP
        #Partition will be roughly half of total length
    #Find midpoint in shorter array
        #Use midpoint and subtract it from 'half' (of total length) to find midpoint element of other array
    #Correctness check: Check if last value in partition 'A' is less than value next value in parition 'B' and vice versa
        #If one of the values is not less, one of partitions is incorrect
        #Have to update corresponding pointers and recalculate the midpoints
    #Median Find
        #Odd:to find the median, will take minimum of the next elements in the partitions 
        #Even: max value of last element and min value of next element in partition / 2 
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        #Make sure A is the shorter array
        if len(B) < len(A):
            A,B = B,A
            
        #Begin binary search    
        l, r = 0, len(A) - 1

        #Always can find median
        while True:
            midA = (l + r) // 2
            midB = half - midA - 2 #represents index so -2 represents correct index
            
            #Aleft/Aright/Bleft/Bright values for comparing if partitions are correct
            #Aleft would be last value in left partition and Aright would be first val in right
            
            #Avoid OOB error if taking just partition from other array
            #If midA is less than 0, "too far to left"
            if(midA >= 0):
                Aleft = A[midA]
            else:
                Aleft = float("-infinity")

            #If this OOB then all values in array A should be part of partition
            if (midA + 1) < len(A):
                Aright = A[midA + 1]
            else:
                Aright = float("infinity")
            
            #Same logic as above
            if midB >= 0:
                Bleft = B[midB]
            else:
                Bleft = float("-infinity")

            if (midB + 1) < len(B):    
                Bright = B[midB + 1]
            else:
                Bright = float("infinity")

            #partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #Odd Elements Case
                if total % 2:
                    return min(Aright, Bright)
                #Even Elements C ase
                return (max(Aleft, Bleft) + min (Aright, Bright)) / 2
            #Too many elements from A, reduce size
            elif Aleft > Bright:
                r = midA - 1
            #Last value in A left partition too small,    
            else:
                l = midA + 1