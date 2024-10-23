from PIL.ImageChops import screen
from PyQt6.QtWidgets import QApplication, QWidget,  QLabel, QComboBox, QGridLayout
from PyQt6.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('Qt6 下拉菜单示例')
        self.resize(600, 400)

        # 调用居中方法
        self.center()

        # 创建垂直布局
        layout = QGridLayout()

        # 创建标签，显示选择的内容
        # self.label = QLabel("请选择一个选项")
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 创建 QComboBox（下拉菜单）
        self.combo_box1 = QComboBox()
        self.combo_box2 = QComboBox()
        self.combo_box3 = QComboBox()
        self.combo_box4 = QComboBox()

        self.combo_box1.addItems(["选项 1", "选项 2", "选项 3"])  # 添加选项
        self.combo_box2.addItems(["选项 1", "选项 2", "选项 3"])  # 添加选项
        self.combo_box3.addItems(["选项 1", "选项 2", "选项 3"])  # 添加选项
        self.combo_box4.addItems(["选项 1", "选项 2", "选项 3"])  # 添加选项

        # 将下拉菜单和标签添加到布局
        layout.addWidget(self.combo_box1)
        layout.addWidget(self.combo_box1)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.combo_box3)
        layout.addWidget(self.combo_box3)
        layout.addWidget(self.combo_box4)
        layout.addWidget(self.combo_box4)

        # 设置窗口的主布局
        self.setLayout(layout)

    def center(self):
        sc = QApplication.primaryScreen()  # 获取主屏幕
        screen_geometry = sc.availableGeometry()  # 获取屏幕的几何信息（例如屏幕的分辨率和可用区域）
        window_geometry = self.frameGeometry()  # 获取窗口的几何信息（包括其大小和位置）

        # 计算窗口居中的左上角坐标
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)  # 将窗口集合的中心移动到屏幕中心
        self.move(window_geometry.topLeft())  # 将窗口移动到左上角的计算位置


# 创建应用程序对象
app = QApplication(sys.argv)

# 创建主窗口并显示
window = MainWindow()
window.show()

# 运行应用程序主循环
sys.exit(app.exec())
