import pygame #type:ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #informs player of resolution
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set to 1280/720
    clock = pygame.time.Clock()
    score = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for obj in updatable:
            obj.update(dt)
            
        player.timer -= dt
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"You scored {score}!")
                raise SystemExit("Game over!")

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
                    score += 1

        screen.fill((0,0,0))
        
        for sprite in drawable:
            sprite.draw(screen) #draws the player sprite on the screen, starts at center

        pygame.display.flip()

        dt = clock.tick(60) /1000 #framerate set to 60


if __name__ == "__main__":
    main()