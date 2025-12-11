from typing import Optional
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Property
from PySide6.QtWidgets import QWidget, QLabel, QGraphicsOpacityEffect


class ErrorLabel(QLabel):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._opacity_effect)

        self._animation_start_value = 0
        self._animation_end_value = 1
        self._animation_diration = 500

        self.__init_animation()

    def __init_animation(self) -> None:
        self._animation = QPropertyAnimation(self._opacity_effect, b"opacity")
        self._animation.setStartValue(self._animation_start_value)
        self._animation.setEndValue(self._animation_end_value)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation.setDuration(self._animation_diration)
        self._animation.valueChanged.connect(self.update)
        self._animation.finished.connect(self.__show_hide)

    def __show_hide(self) -> None:
        if self._animation.direction() == QPropertyAnimation.Direction.Backward:
            self.hide()
            self.setText("")
        else:
            self.hide_alert()

    def show_alert(self, content: str) -> None:
        self.setText(content)

        self._animation.setDirection(QPropertyAnimation.Direction.Forward)
        self._animation.start()
        self.show()

    def hide_alert(self):
        self._animation.setDirection(QPropertyAnimation.Direction.Backward)
        self._animation.start()

    @Property(float)
    def animation_start_value(self) -> float:
        return self._animation_start_value
    
    @animation_start_value.setter
    def animation_start_value(self, value: float) -> None:
        self._animation_start_value = value
        self.__init_animation()
        self.update()

    @Property(float)
    def animation_end_value(self) -> float:
        return self._animation_end_value
    
    @animation_end_value.setter
    def animation_end_value(self, value: float) -> None:
        self._animation_end_value = value
        self.__init_animation()
        self.update()

    @Property(int)
    def animation_diration(self) -> int:
        return self._animation_diration
    
    @animation_diration.setter
    def animation_diration(self, value: int) -> None:
        self._animation_diration = value
        self.__init_animation()
        self.update()
    