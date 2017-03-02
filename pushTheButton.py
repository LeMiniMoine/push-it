import pygame
import json

from random import randint

screen = None
display = None
time_config = None
images_config = None

def load_image(path):
    return pygame.transform.scale(pygame.image.load(path), (display['width'], display['height']))


def load_base_images():
    pic_intro = load_image(images_config['first_image_path'])
    pic_button_pushed = load_image(images_config['second_image_path'])
    return {'intro': pic_intro, 'pushed': pic_button_pushed}


def load_results_matrix():
    first_rebel_pic = load_image(images_config['first_rebel_image_path'])
    second_rebel_pic = load_image(images_config['second_rebel_image_path'])
    third_rebel_pic = load_image(images_config['third_rebel_image_path'])
    fourth_rebel_pic = load_image(images_config['fourth_rebel_image_path'])

    first_gift_pic = load_image(images_config['first_gift_image_path'])
    second_gift_pic = load_image(images_config['second_gift_image_path'])
    third_gift_pic = load_image(images_config['third_gift_image_path'])
    fourth_gift_pic = load_image(images_config['fourth_gift_image_path'])

    first_gift_ratio = images_config['first_gift_ratio']
    second_gift_ratio = images_config['second_gift_ratio'] + first_gift_ratio
    third_gift_ratio = images_config['third_gift_ratio'] + second_gift_ratio
    fourth_gift_ratio = images_config['fourth_gift_ratio'] + third_gift_ratio

    matrix_width, matrix_height = 3, 4

    results = [[0 for x in range(matrix_width)] for y in range(matrix_height)]

    results[0][0], results[0][1], results[0][2] = first_gift_ratio, first_rebel_pic, first_gift_pic
    results[1][0], results[1][1], results[1][2] = second_gift_ratio, second_rebel_pic, second_gift_pic
    results[2][0], results[2][1], results[2][2] = third_gift_ratio, third_rebel_pic, third_gift_pic
    results[3][0], results[3][1], results[3][2] = fourth_gift_ratio, fourth_rebel_pic, fourth_gift_pic

    return results


def load_display():
    pygame.mouse.set_visible(False)

    display_info = pygame.display.Info()
    display_width = display_info.current_w
    display_height = display_info.current_h

    return {'width': display_width, 'height': display_height}


def change_image(image):
    screen.blit(image, [0, 0])
    pygame.display.flip()


def load_config(filename):
    return json.load(open(filename))


def load_screen():
    return pygame.display.set_mode((display['width'], display['height']), pygame.FULLSCREEN)


def init_script():
    pygame.init()
    pygame.mixer.init()

    global display
    display = load_display()
    global screen
    screen = load_screen()
    global time_config
    time_config = load_config('config/time_config.json')
    global images_config
    images_config = load_config('config/images_config.json')

    base_images = load_base_images()
    results_matrix = load_results_matrix()

    pygame.mixer.music.load('sounds/puppy.mp3')

    return {'base_im': base_images, 'res_mat': results_matrix}


def main():
    script_data = init_script()
    running = True
    animation_ongoing = False

    while running:
        if not animation_ongoing:
            change_image(script_data['base_im']['intro'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.clear()
                    pygame.mixer.music.play()
                    animation_ongoing = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    running = False
        else:
            change_image(script_data['base_im']['pushed'])
            pygame.time.delay(time_config['first_screen_in_ms'])
            result = randint(1, 100)
            result_found = False
            for y in range(len(script_data['res_mat'])):
                if not result_found and result < script_data['res_mat'][y][0]:
                    result_found = True
                    change_image(script_data['res_mat'][y][1])
                    pygame.time.delay(time_config['second_screen_in_ms'])
                    change_image(script_data['res_mat'][y][2])
                    pygame.time.delay(time_config['third_screen_in_ms'])
            pygame.mixer.music.stop()
            pygame.event.set_allowed(pygame.KEYDOWN)
            animation_ongoing = False

    pygame.mixer.quit()
    pygame.quit()


main()
