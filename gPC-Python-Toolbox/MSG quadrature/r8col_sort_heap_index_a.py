import numpy as np
from r8vec_compare import r8vec_compare

def r8col_sort_heap_index_a ( m, n, a ):

# R8COL_SORT_HEAP_INDEX_A does an indexed heap ascending sort of an R8COL.

#  Discussion:

#    The sorting is not actually carried out.  Rather an index array is
#    created which defines the sorting.  This array may be used to sort
#    or index the array, or to sort or index related arrays keyed on the
#    original array.

#    A(*,J1) < A(*,J2) if the first nonzero entry of A(*,J1)-A(*,J2) is negative.

#    Once the index array is computed, the sorting can be carried out
#    "implicitly:

#      A(*,INDX(1:N)) is sorted,

#  Licensing:

#    This code is distributed under the GNU LGPL license.

#  Modified:

#    26 October 2008

#  Author:

#    John Burkardt

#  Parameters:

#    Input, integer M, the number of rows in each column of A.

#    Input, integer N, the number of columns in A.

#    Input, real A(M,N), the array.

#    Output, integer INDX(N), the sort index.  The I-th element of the sorted 
#    array is column INDX(I).

    indx = np.zeros((1,1))
    column = np.zeros((1,1))
    if ( n < 1 ):
        indx = []
        return(indx)
    for i in range(1,int(n+1)):
        indx.resize(i)
        indx[i-1] = i
    
    if ( n == 1 ):
        return (indx)
    l = int(np.floor ( n / 2 ) + 1)
    ir = int(n)
    
    while ( 1 ):

        if (1 < l):

            l = l - 1
            indxt = indx[l-1]
           
            if (column.size<m):
                column.resize(m)
                column[0:m] = a[0:m,int(indxt-1)]
                           
            else:
                
                column[0:m] = a[0:m,int(indxt-1)]
            
        else:
            indxt = indx[ir-1]
            if (column.size<m):
                column.resize(m)
                column[0:m] = a[0:m,int(indxt-1)]
                         
            else:
                
                column[0:m] = a[0:m,int(indxt-1)]
            
            indx[ir-1] = indx[0]
            ir = ir - 1
            
            if ( ir == 1 ):
                indx[0] = indxt
                break
            
        i = l
        j = l + l
        
        
        while ( j <= ir ):

            if ( j < ir ):
                
                if ( r8vec_compare ( m, a[0:m,int(indx[j-1]-1)], a[0:m,int(indx[j]-1)] ) < 0 ):
                    j = j + 1
        
   
            if ( r8vec_compare ( m, column, a[0:m,int(indx[j-1]-1)] ) < 0 ):
                indx[i-1] = indx[j-1]
                i = j
                j = j + j
            else:
                j = ir + 1
            

  
        indx[i-1]=indxt
    
    return(indx)


   