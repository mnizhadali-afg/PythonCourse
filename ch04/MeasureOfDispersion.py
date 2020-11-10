import statistics as st
import math


values = [1,3,4,2,6,5,3,4,5,2]
pstdev = st.pstdev(values)
stdev = st.stdev(values)
pvariance = st.pvariance(values)
print('Pupolation Variance: ', pvariance)
print('Pupolation Standard Deviation: ', pstdev)
print('Standard Deviation: ', stdev)

# meanOfValues = st.mean(values)
#
# print("Subtracting MEAN from every Die value:")
# for i in values:
#     print('\t(',i - meanOfValues,')')
#
# print()
#
# print("Squaring each subtracted value:")
# for i in values:
#     print('\t(', pow((i - meanOfValues), 2), ')')
#
