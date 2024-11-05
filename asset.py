import pygame
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Life is better if there are feelings')

black = (0, 0, 0)
white = (255, 255, 255)
font_size = 25
font = pygame.font.SysFont('Arial', font_size)

def display_text(text, delay=50):
    screen.fill(black)
    x, y = 10, 10
    for i in range(len(text) + 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        rendered_text = font.render(text[:i], True, white)
        screen.fill(black) 
        screen.blit(rendered_text, (x, y))
        pygame.display.flip()
        pygame.time.delay(delay)
    pygame.time.delay(2000)

def main():
    running = True
    messages = [
        "hai cantik",
        "okay i know...",
        "saya tahu kita belum saling kenal",
        "jadi pada kesempatan ini saya akan jujur sama kamu...",
        "sebenarnya saya dari dulu dah ingin kenalan dengan kamu",
        "alasan saya ingin kenalan dengan kamu itu...",
        "karena hanya satu momen",
        "satu momen yang menurut saya paling indah di hidup saya",
        "momen yang selalu membuat saya ingat wajahmu",
        "momen yang membuat saya suka, tertarik, dan penasaran sama kamu",
        "saya tidak akan bilang di sini",
        "tapi yang pasti saya akan mengingat momen itu",
        "selamanya sepanjang hidup gw",
        "walaupun momen pertama kali melihatmu itu hanya sepersekian detik",
        "namun hal itu selalu berhasil...",
        "membuat hariku lebih berwarna",
        "karena tanpamu...",
        "aku merasa seperti...",
        "gambar yang kehilangan warna",
        "maaf jika tiba-tiba aku bilang ini ke kamu...",
        "soalnya aku dah terlanjur suka",
        "because...",
        "you're just like an angel",
        "your skin makes me cry",
        "you float like a feather",
        "in this beautiful world",
        "you're so fuckin' special",
        "life is better without feelings?",
        "are you sure honey",
    ]
    
    for message in messages:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        display_text(message)
    
    pygame.quit()

if __name__ == '__main__':
    main()
