from serpent.game_api import GameAPI


class WebTetrisAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class MainMenu:

        api = WebTetrisAPI.instance

        @classmethod
        def start_game(cls):
            cls.api.input_controller.click_screen_region(screen_region="MAIN_MENU_PLAY_BUTTON")

        # Only if the game allows level selection
        # TODO: [Low priority] input level after pressing it
        @classmethod
        def select_level(cls):
            select_level = "MAIN_MENU_SELECT_LEVEL_BUTTON"
            if cls.api.game.screen_regions.get(select_level) is not None:
                cls.api.input_controller.click_screen_region(screen_region=select_level)

    class Game:  # TODO: rename to PlayGame, but might need to re-train context classifier?

        api = WebTetrisAPI.instance

        #######################
        # GETTING GAME STATES #
        #######################

        @classmethod
        def parse_board(cls):
            pass

        @classmethod
        def get_next_tetrominoes(cls):
            # return a list of next tetrominoes
            pass

        @classmethod
        def get_tetromino_on_hold(cls):
            pass

        @classmethod
        def get_score(cls):
            pass

        @classmethod
        def get_lines_cleared(cls):
            pass

        @classmethod
        def get_level(cls):
            # get level only if the notion of levels is supported
            pass

        ##################
        # TAKING ACTIONS #
        ##################


        @classmethod
        def swap_with_tetromino_on_hold(cls):
            pass


        @classmethod
        def move_left(cls):
            pass


        @classmethod
        def move_right(cls):
            pass

        @classmethod
        def change_orientation(cls):
            pass

    class HighScore:

        api = WebTetrisAPI.instance

        @classmethod
        def parse_high_score(cls):
            pass

        @classmethod
        def enter_name(cls):
            pass

        @classmethod
        def ok(cls):
            pass

    class GameOver:

        api = WebTetrisAPI.instance

        @classmethod
        def go_to_main_menu(cls):
            pass

        @classmethod
        def retry(cls):
            pass
