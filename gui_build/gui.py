import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('semi-utils')
        self.resize(800, 450)

        # 调用窗口居中方法
        self.center()

        # 水平为主布局
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # 左侧垂直布局
        left_layout = QVBoxLayout()
        self.combos = [
            ("选择背景", ["黑色", "白色", "模糊"]),
            ("选择样式", ["1", "2", "3"]),
            ("选择样式", ["2", "2", "3"]),
            ("选择样式", ["3", "2", "3"]),
        ]

        for label_text, items in self.combos:
            combo = QComboBox()
            combo.setFixedWidth(150)
            for item in items:
                combo.addItem(item)
            combo.currentIndexChanged.connect(lambda _, c=combo, l=label_text: self.onComboChange(c, l))

            left_layout.addWidget(QLabel(label_text))
            left_layout.addWidget(combo)

        # 右侧垂直布局
        right_layout = QVBoxLayout()

        # 创建标签显示图片
        self.image_label = QLabel(self)
        self.loadDefaultImage()
        right_layout.addWidget(self.image_label)

        # 底部按钮
        button_layout = QHBoxLayout()
        select_folder_button = QPushButton('选取文件夹')
        export_button = QPushButton('导出')
        cancel_button = QPushButton('关闭')

        select_folder_button.clicked.connect(self.selectFolder)
        export_button.clicked.connect(self.exportAction)
        cancel_button.clicked.connect(self.close)

        button_layout.addWidget(select_folder_button)
        button_layout.addWidget(export_button)
        button_layout.addWidget(cancel_button)

        right_layout.addLayout(button_layout)

        # 添加到主布局
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

    def onComboChange(self, combo, label_text):
        index = combo.currentIndex()
        current_text = combo.itemText(index)
        if label_text == "选择背景":
            self.applyBackgroundEffect(current_text)

    def applyBackgroundEffect(self, effect):
        if effect == "黑色":
            self.add_black_border()
        elif effect == "白色":
            self.add_white_border()
        elif effect == "模糊":
            self.apply_blur_effect()

    def add_black_border(self):
        pixmap = self.image_label.pixmap()
        if pixmap:
            self.draw_border(pixmap, Qt.GlobalColor.black)

    def add_white_border(self):
        pixmap = self.image_label.pixmap()
        if pixmap:
            self.draw_border(pixmap, Qt.GlobalColor.white)

    def draw_border(self, pixmap, color):
        painter = QPainter(pixmap)
        pen = QPen(color, 20)
        painter.setPen(pen)
        rect = pixmap.rect()
        painter.drawRect(rect.adjusted(0, 0, -1, -1))
        painter.end()
        self.image_label.setPixmap(pixmap)

    def apply_blur_effect(self):
        pixmap = self.image_label.pixmap()
        if pixmap:
            self.image_label.setGraphicsEffect(QGraphicsBlurEffect())

    def selectFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件夹')
        if folder_path:
            print(f"选择了文件夹：{folder_path}")

    def exportAction(self):
        print('导出操作执行...')

    def loadDefaultImage(self):
        default_image_path = '../images/_DSC4839.JPG'
        pixmap = QPixmap(default_image_path)
        if pixmap.isNull():
            print("无法加载默认图片")
        else:
            self.image_label.setPixmap(pixmap.scaledToWidth(400))  # 调整图片宽度
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def center(self):
        sc = QApplication.primaryScreen()  # 获取主屏幕
        screen_geometry = sc.availableGeometry()  # 获取屏幕的几何信息
        window_geometry = self.frameGeometry()  # 获取窗口的几何信息

        # 计算窗口居中的左上角坐标
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)  # 将窗口集合的中心移动到屏幕中心
        self.move(window_geometry.topLeft())  # 将窗口移动到左上角的计算位置

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()