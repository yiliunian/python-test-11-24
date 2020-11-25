def make_album(name ,music_name ,time=''):
    """"返回歌手歌曲年份"""
    zj = {'f_time':time ,'f_name':name ,'f_music_name':music_name}
    return zj
while True:
    print("(enter 'q' at any time to quit)")
    print("\nPlease tell me your  like star's name:")
    f_name = input('name')
    if f_name == 'q':
        break
    print("\nPlease tell me your  like star's music:")
    f_music_name = input('name')
    if f_music_name == 'q':
        break
    print("\nPlease tell me your  like star's music time:")
    f_time = input('name')
    if f_time == 'q':
        break
    print("\nyou like star name is " + f_name+"his music is "+ f_music_name+ " fashou time is" + f_time )
make_album('zj')
print('zj')