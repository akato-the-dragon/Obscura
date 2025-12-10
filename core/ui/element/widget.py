# Import modules
from typing import Optional, Final
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtCore import Qt, QVariantAnimation, QEasingCurve, QRect, Property, QEvent


class StatusWidget(QWidget):
    class Status:
        ONLINE: Final[int] = 1
        OFFLINE: Final[int] = 0

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._status = self.Status.OFFLINE

        # Properties
        self._online_color = QColor(0, 255, 0)
        self._offline_color = QColor(255, 0, 0)
        self._radius = 5

        self._animation_diration = 500

        # Init animation
        self.__init_animation()
    
    def __init_animation(self) -> None:
        self._animation = QVariantAnimation(self)
        self._animation.setStartValue(self._offline_color)
        self._animation.setEndValue(self._online_color)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation.setDuration(self._animation_diration)
        self._animation.valueChanged.connect(self.update)

    def paintEvent(self, event: QEvent) -> None:
        # Create qpainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background
        current_color = self._animation.currentValue()
        background_rect = QRect(0, 0, self.width(), self.height())

        painter.setPen(QPen(Qt.GlobalColor.transparent))
        painter.setBrush(QBrush(current_color))

        painter.drawRoundedRect(background_rect, self._radius, self._radius)
    
    @Property(int)
    def radius(self) -> int:
        return self._radius
    
    @radius.setter
    def radius(self, value: int) -> None:
        self._radius = value

        self.update()
    
    @Property(QColor)
    def online_color(self) -> QColor:
        return self._online_color
    
    @online_color.setter
    def online_color(self, value: QColor) -> None:
        self._online_color = value
        self.__init_animation()
        self.update()

    @Property(QColor)
    def offline_color(self) -> QColor:
        return self._offline_color
    
    @offline_color.setter
    def offline_color(self, value: QColor) -> None:
        self._offline_color = value
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
    
    @property
    def status(self) -> int:
        return self._status

    def set_status(self, status: int = Status.ONLINE) -> None:
        if self._status != status:
            self._animation.setDirection(QVariantAnimation.Direction.Forward if status else QVariantAnimation.Direction.Backward)
            self._animation.start()

        self._status = status
