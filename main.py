from src.game import Solitare
import arcade


def main():
    """Main function"""
    window = Solitare()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
