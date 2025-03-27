import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 250, 300)

        # 레이아웃 설정
        grid = QGridLayout()
        self.setLayout(grid)

        # 입력창 생성
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setStyleSheet('font-size: 20px; height: 40px;')
        grid.addWidget(self.display, 0, 0, 1, 4)

        # 버튼의 구성
        buttons = [
            ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 1, 2), ('.', 5, 2), ('=', 5, 3)
        ]

        for btn_text, x, y, *size in buttons:
            button = QPushButton(btn_text)
            button.setFixedSize(50, 50)
            grid.addWidget(button, x, y, *size)

            # 이벤트 연결 (버튼 클릭 시 동작 설정)
            button.clicked.connect(self.button_clicked)

        self.show()

    def button_clicked(self):
        sender = self.sender()
        btn_text = sender.text()

        # 간단한 버튼 클릭 시 표시만 (연산 기능은 아직 미구현)
        current_text = self.display.text()

        if current_text == '0':
            self.display.setText(btn_text)
        else:
            self.display.setText(current_text + btn_text)

    def button_clicked(self):
        sender = self.sender()
        btn_text = sender.text()

        if btn_text == 'AC':
            self.display.setText('0')
        elif btn_text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        else:
            current_text = self.display.text()
            if current_text == '0':
                self.display.setText(btn_text)
            else:
                self.display.setText(current_text + btn_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
