import pygame
import sys

# 초기 설정
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# 플랫폼 설정
platform_width, platform_height = 100, 10
platform_x = (width - platform_width) / 2
platform_y = height - 30
platform_speed = 0

# 공 설정
ball_x = width / 2
ball_y = height / 2
ball_radius = 8
ball_speed_x = 5
ball_speed_y = -5

# 벽돌 설정
brick_width = 50
brick_height = 20
num_bricks_x = width // (brick_width + 10)
num_bricks_y = 5
bricks = []
for x in range(num_bricks_x):
    for y in range(num_bricks_y):
        bricks.append(pygame.Rect(x * (brick_width + 10), y * (brick_height + 5) + 50, brick_width, brick_height))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                platform_speed = -6
            elif event.key == pygame.K_RIGHT:
                platform_speed = 6
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                platform_speed = 0

    # 플랫폼 움직임
    platform_x += platform_speed
    platform_x = max(0, min(width - platform_width, platform_x))

    # 공 움직임
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 공이 벽에 부딪히면 반대 방향으로 튕김
    if ball_x <= ball_radius or ball_x >= width - ball_radius:
        ball_speed_x *= -1
    if ball_y <= ball_radius:
        ball_speed_y *= -1

    # 공이 플랫폼에 닿으면 튕김
    if platform_x <= ball_x <= platform_x + platform_width and platform_y <= ball_y + ball_radius <= platform_y + platform_height:
        ball_speed_y *= -1

    # 공이 벽돌에 닿으면 벽돌 제거 및 공 방향 변경
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    # 공이 바닥에 닿으면 게임 종료
    if ball_y >= height - ball_radius:
        print("Game Over")
        running = False

    # 화면 그리기
    screen.fill(black)
    for brick in bricks:
        pygame.draw.rect(screen, blue, brick)
    pygame.draw.rect(screen, white, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)
    pygame.display.flip()

    # 프레임 속도 조절
    clock.tick(60)

pygame.quit()
sys.exit()

