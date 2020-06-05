import sys
import pygame

    def run_game():
        # 初始化游戏并创建一个屏幕对象
        pygame.init()   #初始化背景设置，让Pygame能够正确地工作
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        bg_color = (230, 230, 230)    #该颜色只需指定一次，因此我们在进入主while循环前定义它。
        
        # 开始游戏的主循环
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    .....
             # 每次循环时都重绘屏幕
            screen.fill(bg_color)           
            # 让最近绘制的屏幕可见
            pygame.display.flip()
            
run_game()
