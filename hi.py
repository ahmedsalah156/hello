#calling important modules

import numpy as np
import array

#taking the i/p from the user
mx1=input('enter the first in the format [a b c;d e f] and (;) stands for a new row  ')
operation=input('enter the type of operation : add(+) , subtraction(-) , multiplication(*) , inverse(-1)')
mx2=input('enter the second in the format [a b c;d e f] and (;) stands for a new row  ')

if mx1[0]=='[' and mx1[len(mx1)-1]==']' and mx2[0]=='[' and mx2[len(mx2)-1]==']':
    # function to get the no of coloums
    def coloums(mx):
        # some operation on the i/p
        y2 = mx.replace('[', '')
        mx3 = y2.replace(']', '')
        mx4 = mx3.replace(' ', '')

        ##determine the no of rows and coloums
        rows = mx1.count(';') + 1

        sum = 0
        for m in mx3:
            if m == ' ':
                sum = sum + 1

        coloums = sum/rows + 1

        # to convert the folat value into integer to be used as index latter
        coloums = int(coloums)
        return coloums


    # function to determine the no of rows
    def rows(mx):
        # some operation on the i/p
        y2 = mx.replace('[', '')
        mx3 = y2.replace(']', '')
        mx4 = mx3.replace(' ', '')

        ##determine the no of rows and coloums
        rows = mx.count(';') + 1
        return rows


    # function to convert the input string into a matrix
    def create_the_matrix(mx1):
        # some operation on the i/p
        y2 = mx1.replace('[', '')
        mx3 = y2
        mx4 = mx3.replace(' ', '')

        ##determine the no of rows and coloums
        rows = mx1.count(';') + 1
        sum=0
        for m in mx3:
            if m==' ':
                sum = sum + 1

        coloums = sum/rows + 1

        # to convert the folat value into integer to be used as index latter
        coloums = int(coloums)

        # convert the string into floats and put it into z1
        i = 0
        j = 0
        k = 0
        r = 0
        flag=0
        flag_final=0

        # define zeros matrix
        z = np.zeros([rows, coloums])

        ##three for loops : 1st one for each new row ...2nd is for the coloums....third on to loop over each element in the string
        for y in mx3:
            for o in mx3:
                for x in mx3:
                    # the main idea here is to find where is the (space) and if we find it we will make a list to thake the elements from [0:spce index]
                    # now after we have done this we will cut the string from the (space) index to the end and will save it in the same string
                    # as shown in the code below
                    # now we want to detect when we will have a new row and we can detect this throgh the semicolone if x is ';' then we will enter the
                    # if condition as shown be;ow and make a flag to exit also from the next outer loop to detect that we have a new row
                    # here we use  (i) to represent the coloums
                    # we use (j) to represent each element in the string
                    # we use (r) to represent the row number
                    # the final_flag to detect that we have finish the full string
                    if x == ' ' or x == ';' or x == ']':
                        z[r, i] = float(mx3[0:j])
                        mx3 = mx3[j + 1:]
                        i = i + 1
                        k = 0
                        if x == ';':
                            flag = 1
                            i = 0
                            j = 0
                            r = r + 1
                            break
                        if x == ']':
                            flag_final = 1
                            break

                        if k == 0:
                            break
                    j = j + 1
                if k == 0:
                    j = 0

            if flag == 1 or flag_final == 1:
                i = 0
                break

        return z


    # used for testing
    mx5 = create_the_matrix(mx1)
    mx6 = create_the_matrix(mx2)


    # function to add two matrices
    def sum_matrix(m1, m2):
        if coloums(m1) == coloums(m2) and rows(m1) == rows(m2):
            z = m1 + m2
        else:
            z = 'error'
        return z

    if operation=='+':
        print('sum is')
        print(sum_matrix(mx5,mx6))

    # function to subtract two matrices
    def subtract_matrix(m1, m2):
        if coloums(m1) == coloums(m2) and rows(m1) == rows(m2):
            z = m1 + m2
        else:
            z = 'error'
        return z
    if operation=='-':
        print('subtraction is')
        print(subtract_matrix(mx5,mx6))


    # multiplication of two matrices of 2*2
    i = 0
    j = 0
    k = 0

    # define a matrix of zeros
    zero = np.zeros([rows(mx1), coloums(mx2)])

    # no of coloums and rows for the second matrix
    no_rows1 = rows(mx1)
    no_col1 = coloums(mx1)

    # no of coloums and rows for the first matrix
    no_rows2 = rows(mx2)
    no_col2 = coloums(mx2)

    if operation=='*':
        # the if condition to make sure that the condition for multiplication is atisfied
        if no_col1 == no_rows2:
            for x in mx1:
                # condition to detect the no of rows
                if i >= no_rows1:
                    break
                else:
                    for y in mx1:
                        # condition to detect the no of coloums
                        if j >= no_col2:
                            # for each time we finsh the coloums for the first row for example we have to make j equal zero to repeat the same operation for the second row in the first with the coloums in the second
                            j = 0
                            break
                        else:
                            for z0 in mx1:
                                # first multiply each elemnt of the tow matrix and thend add them to zeros matrix then repeat the same operation for the second elemnt then add it to the first that we have calculated
                                # we first deal with the first row and we use (i) to represent it
                                # we then used k to represent the elemnt index in each row and coloum
                                # it is a must that the no of elemnt in each row in the first martix to equal the no of elemnt in each colom in the second matrix
                                if k < no_col1:
                                    multi_result = mx5[i, k] * mx6[k, j]
                                    zero[i, j] = multi_result + zero[i, j]
                                    k = k + 1
                                else:
                                    k = 0
                                    break

                        j = j + 1
                    i = i + 1
            else:
                print('error....make sure the no of col of the first equal the no of rows for the second')


    # function to calculate the determinant of 2*2 matrix
    def determ(mx0):
        if no_rows1 == no_col1:
            det = mx0[0, 0] * mx0[1, 1] - mx0[0, 1] * mx0[1, 0]
        else:
            det = 'error isnt a square matrix'
        return det


    if operation=='-1':
        # initial conditions
        i = 0
        j = 0
        n = 0
        flag = 0
        # define a zero matrix which will be used in condition (100) at line 169
        result = np.zeros([no_col1, no_col1])

        # (100) condition here to make sure the matrix is a square matrix
        if no_col1 == no_rows1:

            # if the input matrix is 2*2
            if no_col1 == 2:
                # determenant
                determenant = determ(mx5)

                # adj matrix
                result[0, 0] = mx5[1, 1]
                result[0, 1] = -1 * mx5[0, 1]
                result[1, 0] = -1 * mx5[1, 0]
                result[1, 1] = mx5[0, 0]
                # inverse matrix
                inverse = (1 / determenant) * result
                print(inverse)
            else:
                # define unity matrix
                unity = np.zeros([no_col1, no_col1])
                for x in mx1:
                    # condition to detect the no of rows
                    if i >= no_col1:
                        break
                    else:
                        # in each time we add one according to I ...for example the first time equal zero and the second time equals ones ...etc
                        unity[i, i] = unity[i, i] + 1
                        i = i + 1

                i = 0
                j = 0
                for x in mx1:
                    # condition to defint the end of coloums in the matrix
                    if j > no_col1 - 2:
                        break
                    else:
                        for y in mx1:
                            if i >= no_col1 - 1 - j:
                                i = 0
                                break
                            else:
                                # condition to dtect
                                if (mx5[j, j] > 0 and mx5[j + i + 1, j] > 0) or (
                                        mx5[j, j] < 0 and mx5[j + i + 1, j] < 0):
                                    s = -1
                                else:
                                    s = 1
                                unity[i + j + 1] = s * mx5[i + j + 1, j] * unity[j] + mx5[j, j] * unity[i + j + 1]
                                mx5[i + j + 1] = s * mx5[i + j + 1, j] * mx5[j] + mx5[j, j] * mx5[i + j + 1]

                                i = i + 1
                        j = j + 1

                i = 0
                j = 0
                k = 0

                for x in mx1:
                    if mx5[no_col1 - 1, no_col1 - 1] == 0:
                        flag = 1
                        break
                    # condition to gurantee that in each time we will deal with one coloume only from the unity matrix with mx5 (look at the note book for more detailes)
                    if k > no_col1 - 1:
                        break
                    else:
                        result[no_col1 - 1, k] = unity[no_col1 - 1, k] / mx5[no_col1 - 1, no_col1 - 1]

                        for y in mx1:
                            if i >= no_col1 - 1:
                                i = 0
                                break
                            else:
                                for z in mx1:
                                    # condition to gurantee we will loop for no of times equal to the no of non zero element - 1
                                    if j > i:
                                        j = 0
                                        break
                                    else:
                                        # to multiply the element in mx5 by the elemnt that we stored in result and add them together in each time
                                        result[no_col1 - i - 2, k] = mx5[no_col1 - i - 2, no_col1 - j - 1] * result[
                                            3 - j - 1, k] + result[no_col1 - i - 2, k]
                                        j = j + 1
                                # to subtract the last element we stored in result from the stored elemnt in unity
                                result[no_col1 - i - 2, k] = -1 * result[no_col1 - i - 2, k] + unity[no_col1 - j - 2, k]
                                result[no_col1 - i - 2, k] = result[no_col1 - i - 2, k] / mx5[
                                    no_col1 - i - 2, no_col1 - j - 2]
                                i = i + 1

                        k = k + 1

                # condition happends only if there is a complete row of zeros
                if flag == 1:
                    print('error because the matrix cnt be made in echelon form :')
                    print(mx5)
                else:
                    print(result)


        else:
            print('error no a square matrix' + '\n')


else:
    print('not a correct format')
























