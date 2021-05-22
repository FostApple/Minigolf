import pygame
pygame.init()
win = pygame.display.set_mode((700,500))

x = 600
y = 350
xvel = 0
yvel = 0

strokes = 0

while True:
  win.fill((54,181,45))
  pygame.time.delay(10)

  pygame.event.pump()
  xcur,ycur = pygame.mouse.get_pos()

  # Slow down ball
  xvel = xvel * 0.95
  yvel = yvel * 0.95
  
  #Draw Hole
  hole = pygame.draw.circle(win, (0,0,0), (111,90), 20)

  #Making the player stop when the ball is moving
  if abs(xvel) < 0.05 and abs(yvel) < 0.05:
    pygame.draw.line(win, (120,230,12), (x,y), (xcur,ycur))
    if hole.collidepoint(x,y):
      #1: hole in one
      #2/3: birdies
      #4: bogie
      #5: big bogie
      #6: double bogie + 1
      #7: You are doodoo
      if strokes == 1:
        print('Hole in 1!')
      elif strokes == 2 or strokes == 3:
        print('Birdie!')
      elif strokes == 4:
        print('Bogie')
      elif strokes == 5:
        print('Big Bogie')
      elif strokes == 6:
        print('Double Bogie + 1')
      else:
        print('You are doodoo')
      break

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        strokes += 1
        xvel = (xcur-x) *0.1
        yvel = (ycur-y) *0.1
  
  #Draw the sand
  sand = pygame.draw.rect(win, (194,178,128), (230,291,125,220))
  if sand.collidepoint(x,y):
    xvel *= 0.95
    yvel *= 0.95
  
  #Aqua
  water = pygame.draw.rect(win, (50, 151, 168), (0,0,80,500)) and pygame.draw.rect(win, (50,151,168), (0,0,700,60))
  if water.collidepoint(x,y):
    xvel = 0.05
    yvel = 0.05
    x = 600
    y = 350

  #Draw Ball
  pygame.draw.circle(win, (255,255,255), (x,y), 10)

  #Ball speed and bouncing
  x = x + xvel
  y = y + yvel
    
  if x > 680:
    xvel = xvel * -1

  if x < 10:
    xvel = xvel * -1

  if y > 485:
    yvel = yvel * -1

  if y < 10:
    yvel = yvel * -1
    
  pygame.display.update()