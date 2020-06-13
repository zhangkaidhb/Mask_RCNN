import os


address1= os.path.abspath('../../..')+'\\Recordings'
print(address1)

address_id='exports\\000\\world.mp4' #需要更改到你自己的eye-trackingsystem对应输出文件夹
print(address_id)
global picture_number
picture_number = 1
counter=0
for file_name in os.listdir(address1):
    # print(file_name)
    address2=address1+'\\'+file_name+'\\'+address_id
    print(address2)
    counter+=1
    print('The %dth group:%s finished'%(counter,file_name))
# print(counter)