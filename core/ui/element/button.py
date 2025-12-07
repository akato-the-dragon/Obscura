# Import modules
from typing import Optional
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import (Qt, QRect, QEvent, Property, QVariantAnimation,
                            QEasingCurve, Signal, Slot, QSequentialAnimationGroup)
from PySide6.QtGui import QPainterPath, QPainter, QBrush, QPen, QColor, QFont, QIcon


class FadingButton(QPushButton):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Properties
        self._background_color = QColor(0, 0, 0, 0)
        self._color = QColor(255, 255, 255)
        self._radius = 0

        self._hover_animation_start_value = 0
        self._click_animation_start_value = 0

        self._hover_animation_end_value = 10
        self._click_animation_end_value = 20

        self._hover_animation_duration = 100
        self._click_animation_duration = 100

        # Init animation
        self.__init_animation()
    
    def __init_animation(self) -> None:
        # Hover animation
        self._hover_animation = QVariantAnimation(self)
        self._hover_animation.setStartValue(self._hover_animation_start_value)
        self._hover_animation.setEndValue(self._hover_animation_end_value)
        self._hover_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._hover_animation.setDuration(self._hover_animation_duration)
        self._hover_animation.valueChanged.connect(self.update)

        # Click animation
        self._click_animation = QVariantAnimation(self)
        self._click_animation.setStartValue(self._click_animation_start_value)
        self._click_animation.setEndValue(self._click_animation_end_value)
        self._click_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._click_animation.setDuration(self._click_animation_duration)
        self._click_animation.valueChanged.connect(self.update)

    def enterEvent(self, event: QEvent) -> None:
        super().enterEvent(event)

        self._hover_animation.setDirection(QVariantAnimation.Direction.Forward)
        self._hover_animation.start()

    def leaveEvent(self, event: QEvent) -> None:
        super().leaveEvent(event)

        self._hover_animation.setDirection(QVariantAnimation.Direction.Backward)
        self._hover_animation.start()

    def mousePressEvent(self, event: QEvent):
        super().mousePressEvent(event)

        self._click_animation.setDirection(QVariantAnimation.Direction.Forward)
        self._click_animation.start()

    def mouseReleaseEvent(self, event: QEvent):
        super().mouseReleaseEvent(event)

        self._click_animation.setDirection(QVariantAnimation.Direction.Backward)
        self._click_animation.start()

    def paintEvent(self, event: QEvent) -> None:
        # Asign painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background
        background_rect = QRect(0, 0, self.width(), self.height())

        painter.setBrush(self._background_color)
        painter.setPen(Qt.GlobalColor.transparent)
        painter.drawRoundedRect(background_rect, self._radius, self._radius)

        # Draw filler
        filler_rect = QRect(0, 0, self.width(), self.height())

        color = self._color
        color.setAlpha(max(self._hover_animation.currentValue(), self._click_animation.currentValue()))

        painter.setBrush(color)
        painter.setPen(Qt.GlobalColor.transparent)
        painter.drawRoundedRect(filler_rect, self._radius, self._radius)

        # End painter
        painter.end()

        # Draw button things
        super().paintEvent(event)
    
    @Property(int)
    def radius(self) -> int:
        return self._radius
    
    @radius.setter
    def radius(self, value: int) -> None:
        self._radius = value

        self.update()
    
    @Property(QColor)
    def background_color(self) -> QColor:
        return self._background_color
    
    @background_color.setter
    def background_color(self, value: QColor) -> None:
        self._background_color = value

        self.update()

    @Property(QColor)
    def color(self) -> QColor:
        return self._color
    
    @color.setter
    def color(self, value: QColor) -> None:
        self._color = value

        self.update()

    @Property(int)
    def hover_animation_start_value(self) -> int:
        return self._hover_animation_start_value
    
    @hover_animation_start_value.setter
    def hover_animation_start_value(self, value: int) -> None:
        self._hover_animation_start_value = value
        self.__init_animation()
        self.update()
    
    @Property(int)
    def click_animation_start_value(self) -> int:
        return self._click_animation_start_value
    
    @click_animation_start_value.setter
    def click_animation_start_value(self, value: int) -> None:
        self._click_animation_start_value = value
        self.__init_animation()
        self.update()

    @Property(int)
    def hover_animation_end_value(self) -> int:
        return self._hover_animation_end_value
    
    @hover_animation_end_value.setter
    def hover_animation_end_value(self, value: int) -> None:
        self._hover_animation_end_value = value
        self.__init_animation()
        self.update()
    
    @Property(int)
    def click_animation_end_value(self) -> int:
        return self._click_animation_end_value
    
    @click_animation_end_value.setter
    def click_animation_end_value(self, value: int) -> None:
        self._click_animation_end_value = value
        self.__init_animation()
        self.update()
    
    @Property(int)
    def hover_animation_duration(self) -> int:
        return self._hover_animation_duration
    
    @hover_animation_duration.setter
    def hover_animation_duration(self, value: int) -> None:
        self._hover_animation_duration = value
        self.__init_animation()
        self.update()
    
    @Property(int)
    def click_animation_duration(self) -> int:
        return self._click_animation_duration
    
    @click_animation_duration.setter
    def click_animation_duration(self, value: int) -> None:
        self._click_animation_duration = value
        self.__init_animation()
        self.update()
