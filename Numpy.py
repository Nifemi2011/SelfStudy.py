# What is Numpy?
#  Numpy is a moduled library used in python to create arrays of info or data. 🧱

---------------------------------------------------------------------------------------------
 # How to install Numpy:
# 1. First make sure you have python installed in your computer.(latest Version)
# 2. Then you open our Windows Powershell on your computer and, type
 # -pip m install numpy
----------------------------------------------------------------------------------------------
#                           Which is better Numpy or List🤔

# Both are good in their own ways. But if we were talking about which is faster it would be Numpy⬅️. Why you ask?
# Because Numpy has a backend that operates with binary code.Not using the regular framework that was used in the latest versions of python.

       # Numpy allows you to work with large datasets or if u you need efficient numerical computations.      
       # Lists only allows us to create general public list once at a time. Making our pace slower than using Numpy.
-------------------------------------------------------------------------------------------
          The Basics of Numpy:
   # Below will be the basic code of how Numpy will be used in python 

Input:
      import numpy as np
    a = np.array([1,2,3])
Output:
   [1,2,3]

b = np.array([[9.0,8.0,7.0] , [6.0,5.0,4.0]])
Output: [[9. 8. 7.]
         [6. 5. 4.]]

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                               Dimensions in Numpy/ Arrays
                                                                                         # What are Dimensions in arrays?
                                                                               # Dimensions in arrays is one level of array dept.
                                     # Which means it allows us to create a bigger way of expanding our array instead of repeating the same code over and over again.🙃
                                                                                       Types of Dimensions in arrays:   

          # 0-D Arrays , or scalars, are the elements in an array.
                         import numpy as np
                         arr = np.array(42)
                           print(arr)

        # 1-D Arrays, Meaning uni-dimensional arrays are basically just in row of arrays.
                              import numpy as np
                        arr = np.array([1, 2, 3, 4, 5])
                                   print(arr)

        # 2-D Arrays, Arrays that has 1-D arrays as its element is called a 2-D Arrays.
                import numpy as np
          arr = np.array([[1, 2, 3], [4, 5, 6]])
                     print(arr)

            # 3-D Arrays, Arrays that has 2-D arrays (matrices) as it's element
                                  import numpy as np
           arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
                                    print(arr)
                    
                    # The Dimensions stated above ⬆️ basically tells you that there are different ways to set your code depnding on the sicze and how long you want your Array to be.😮‍💨
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           # How to check number of dimesions in Arrays:
                                                  
