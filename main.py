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

        self.chart = pg.QChart()
        self.chartView = pg.QChartView()
        self.chartView = pg.QChartView(self.chart)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setStandartChart()
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
            self.loadDataOnChart()

    def loadDataOnChart(self):
        self.setStandartChart()
        x_list = [None, None]
        y_list = [None, None]
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor("black"))
        pen.setWidth(2)

        

        for data in self.data:
            name = data[0]
            x = data[1]
            y = data[2]
            count = data[3]

            if x_list[0] == None:
                x_list[0] = x
            else:
                if x < x_list[0]:
                    x_list[0] = x 
            if x_list[1] == None:
                x_list[1] = x
            else:
                if x > x_list[1]:
                    x_list[1] = x             
            if y_list[0] == None:
                y_list[0] = y
            else:
                if y < y_list[0]:
                    y_list[0] = y
            if y_list[1] == None:
                y_list[1] = y
            else:
                if y > y_list[1]:
                    y_list[1] = y

            # text_item = QtWidgets.QGraphicsTextItem(self.chart)
            # text_item.setPlainText(name)
            # text_item.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
            # text_item.setPos(x, y)

            if count < 500000:
                markers_green_series = pg.QScatterSeries()
                markers_green_series.setMarkerShape(pg.QScatterSeries.MarkerShape.MarkerShapeCircle)
                markers_green_series.setMarkerSize(15)
                markers_green_series.setBrush(QtGui.QBrush(QtGui.QColor("green")))
                markers_green_series.setPen(pen)
                markers_green_series.append(x, y)
                self.chart.addSeries(markers_green_series)
            elif count < 1000000:
                markers_red_series = pg.QScatterSeries()
                markers_red_series.setMarkerShape(pg.QScatterSeries.MarkerShape.MarkerShapeCircle)
                markers_red_series.setMarkerSize(25)
                markers_red_series.setBrush(QtGui.QBrush(QtGui.QColor("red")))
                markers_red_series.setPen(pen)
                markers_red_series.append(x,y)
                self.chart.addSeries(markers_red_series)
            else:
                markers_blue_series = pg.QScatterSeries()
                markers_blue_series.setMarkerShape(pg.QScatterSeries.MarkerShape.MarkerShapeCircle)
                markers_blue_series.setMarkerSize(40)
                markers_blue_series.setBrush(QtGui.QBrush(QtGui.QColor("blue")))
                markers_blue_series.setPen(pen)
                markers_blue_series.append(x,y)
                self.chart.addSeries(markers_blue_series)
        else:
            if self.data:
                for axis in self.chart.axes():
                    self.chart.removeAxis(axis)
                axisX = pg.QValueAxis()
                axisY = pg.QValueAxis()
                # axisX.setTickCount(9)
                # axisY.setTickCount(9)
                axisX.setRange(x_list[0], x_list[1])
                axisY.setRange(y_list[0], y_list[1])
                axisX.setLabelsVisible(False)
                axisY.setLabelsVisible(False)
                self.chart.addAxis(axisX, QtCore.Qt.AlignBottom)
                self.chart.addAxis(axisY, QtCore.Qt.AlignLeft)         

    def setStandartChart(self):
        self.chart.removeAllSeries()
        
    
        axisX = pg.QValueAxis()
        axisY = pg.QValueAxis()
        axisX.setTickCount(9)
        axisY.setTickCount(9)
        axisX.setRange(0, 1)
        axisY.setRange(0, 1)
        axisX.setLabelsVisible(False)
        axisY.setLabelsVisible(False)
        self.chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(axisY, QtCore.Qt.AlignLeft)

        self.chart.legend().setVisible(False)
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

