import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import frogger
"""
DNumber: D00090307
Name: Andrew Nelson
Picture: House
Assignment: FROGGER

"""
# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME


TITLE = "FROGGER" # window title bar text
CELL_SIZE = 50
NUM_COLS = 14
NUM_ROWS = 11
WINDOW_WIDTH  = NUM_COLS * CELL_SIZE # pixels width
WINDOW_HEIGHT = NUM_ROWS * CELL_SIZE # pixels high
DESIRED_RATE  = 30 # frames per second


class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.frogger = frogger.Frogger(NUM_COLS,NUM_ROWS,CELL_SIZE)
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        # KEYS TO MOVE THE FROG

        if pygame.K_UP in newkeys:
            self.frogger.actOnPressUP( )
        if pygame.K_DOWN in newkeys:
            self.frogger.actOnPressDOWN( )
        if pygame.K_LEFT in newkeys:
            self.frogger.actOnPressLEFT( )
        if pygame.K_RIGHT in newkeys:
            self.frogger.actOnPressRIGHT( )
        self.frogger.evolve(dt)

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.frogger.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
