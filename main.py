from src.solitaire import Solitaire
import arcade


def main():
    """Main function"""
    window = Solitaire()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
