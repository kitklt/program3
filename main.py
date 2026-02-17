from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_MainWindow
import PyQt5.QtChart as pg
import sys
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        
        self.matrix = []
        self.data = []

        self.ui.setupUi(self)
        self.setChart()
        self.setUiSettings()

        self.ui.pushButton_2.clicked.connect(self.function_for_inport)

    def function_for_inport(self):
        self.data.clear()
        self.matrix.clear()
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text Files (*.txt);;All Files (*)")[0] 
        if filePath:
            with open(file=filePath, encoding="UTF-8")as f:
                count_towns = int(f.readline())
                for i in range(count_towns):
                    data = []
                    for j in range(4):
                        element = f.readline()
                        if '\n' in element:
                            element = element[:element.index('\n')]
                        if j == 0:
                            data.append(element)
                        else:
                            data.append(int(element))
                    self.data.append(tuple(data))
                else:
                    f.readline()
                    for i in range(count_towns):
                        line_matrix = f.readline()
                        if "\n" in line_matrix:
                            line_matrix = line_matrix[:line_matrix.index('\n')]
                        self.matrix.append(tuple(map(int, list(line_matrix))))

    def setChart(self):
        self.series = pg.QLineSeries()
        self.chart = pg.QChart()
        self.chart.addSeries(self.series)
    
        self.axisX = pg.QValueAxis()
        self.axisY = pg.QValueAxis()
        self.axisX.setTickCount(9)
        self.axisY.setTickCount(9)
        self.axisX.setRange(0, 1)
        self.axisY.setRange(0, 1)
        self.axisX.setLabelsVisible(False)
        self.axisY.setLabelsVisible(False)
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        self.chart.legend().setVisible(False)

        self.chartView = pg.QChartView(self.chart)
        self.ui.verticalLayout.addWidget(self.chartView)

        
    
    def setUiSettings(self):
        # buttons
        self.ui.pushButton_2.setText("Импорт")  
        self.ui.pushButton_3.setText("Экспорт")
        self.ui.pushButton_4.setText("Очистить")
        self.ui.pushButton_5.setText("Рассчитать")

        self.ui.pushButton_5.setStyleSheet("background : rgb(0,125,0); color : white; font-size: 14px; font-weight: bold; font-family: Arial;")
        self.ui.pushButton_2.setStyleSheet("color : white; font-size: 14px; font-weight: bold; font-family: Arial;")
        self.ui.pushButton_3.setStyleSheet("color : white; font-size: 14px; font-weight: bold; font-family: Arial;")
        self.ui.pushButton_4.setStyleSheet("color : white; font-size: 14px; font-weight: bold; font-family: Arial;")

        self.ui.centralwidget.setStyleSheet("background : rgb(75,0,130);")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    sys.exit(app.exec())

