from arcade import Sprite


class Refresh(Sprite):
    def __init__(self, scale: float = 1.0) -> None:
        super().__init__(
            "src/images/refresh.png", hit_box_algorithm="None", scale=scale
        )
        self.alpha = 0

    def visibility(self, visibility: bool) -> None:
        if visibility:
            self.alpha = 255
        else:
            self.alpha = 0
