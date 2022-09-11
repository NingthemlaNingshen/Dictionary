# # Remove spaces from dictionary keys
# Product_list = {'P  M': 'D','P A' : ' O S ','P  s': ' Comp  uting   '}
# a={}
# for i, j in Product_list.items():
#     if i==""


student_list = {'P  M': 'Mo     di','P      A' : ' kim     ','P  S': ' Comp  uting   '}
a={}
for x, y in student_list.items():
    x = {x.replace(' ', '')}
    y = {y.replace(' ', '')}
    a[x]=y
    print("New dictionary: ",a)
