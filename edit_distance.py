"""
Problem:
https://www.geeksforgeeks.org/edit-distance-dp-5/

Solution:
T [ A(n), B(n) ] = T [ A(n-1), B(n-1) ]
                    = 1 + T [ A(n-1), B(n) ] if len(A) > len(A)
                    = 1 + T [ B(n-1), A(n) ] if len(B) > len(A)
                    = 1 + T [ A(n-1), B(n) ] if len(A) = len(B)
"""

