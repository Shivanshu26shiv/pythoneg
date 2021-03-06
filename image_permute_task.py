'''
We need a Python program that generates all the possible flags with 3 colored stripes, see attachment.
The colors can be: White, Black, Green, Red, Blue, Green and Orange.

Question 1: Please generate alle the possible flags. One color van not be the same in two stripes next to each other. So green, white, green is possible.

Question 2: Please generate alle the possible flags. One color can only be used onces in a flag. So green, white, green is not good, but So green, white, blue is possible.

Make a Python-program (for mathematic education) that makes this visable. We leave it to your creativity if it is possible to show the flags very small on the screen.

It would be very nice if you can help us!

Thanks in advance, Durk Jan de Bruin

PS: Not all the flags exist in real countries. That is no problem
'''

from PIL import Image, ImageColor
from itertools import permutations, product


def image_maker(color_tuple):

    global counter
    color_1, color_2, color_3 = color_tuple

    if task == '1':

        if color_1 == color_2 or color_2 == color_3:
            print('Not possible for task ' + task + ':', color_tuple)
            return

    elif task not in ['1', '2']:

        print('Invalid task '+task)
        return

    output_image = Image.new('RGBA', (width, height), color_1)

    for x in range(1, width):

        if x in range(width//3, 2*(width//3)):
            set_color = color_2

        elif x in range(2*(width//3), width):
            set_color = color_3

        else:
            continue

        for y in range(height):
            output_image.putpixel((x, y), ImageColor.getcolor(set_color, 'RGBA'))

    counter += 1
    output_image.save(folder_path+'task_'+task+'_'+str(counter)+'.png')
    return

if __name__ == '__main__':

    # width of image
    width = 200

    # height of image
    height = 100

    # number of stripes of flags
    number_of_stripes = 3

    # folder path to save flag images
    folder_path = 'temp/'

    color_list = ['White', 'Black', 'Green', 'Red', 'Blue', 'Orange']

    counter = 0
    color_list_filtered = list(product(color_list, repeat=number_of_stripes))
    for task in ['1', '2']:

        for elem in color_list_filtered:
            image_maker(elem)

        counter = 0
        task = '2'
        color_list_filtered = list(permutations(color_list, number_of_stripes))
