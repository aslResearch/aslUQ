
def r8vec_compare ( n, a1, a2 ):
    
# R8VEC_COMPARE compares two R8VEC's.

#  Discussion:
#
#    The lexicographic ordering is used.
#
#  Example:
#
#    Input:
#
#      A1 = ( 2.0, 6.0, 2.0 )
#      A2 = ( 2.0, 8.0, 12.0 )
#
#    Output:
#
#      ISGN = -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vectors.
#
#    Input, real A1(N), A2(N), the vectors to be compared.
#
#    Output, integer ISGN, the results of the comparison:
#    -1, A1 < A2,
#     0, A1 = A2,
#    +1, A1 > A2.
#

    isgn = 0
    
    k = 1

    while ( k <= n ):
        if ( a1[k-1] < a2[k-1] ):
            isgn = -1
            return(isgn)
        elif ( a2[k-1] < a1[k-1]):
            isgn = +1
            return(isgn)
    
        k = k + 1
   
    return(isgn)
