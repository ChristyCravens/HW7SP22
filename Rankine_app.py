import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Rankine_GUI import Ui_Form  # from the GUI file your created
from Calc_state import Steam_SI as steam
from Rankine import rankine

class main_window(QWidget, Ui_Form):
    def __init__(self):
        """
        Constructor for the main window of the application.  This class inherits from QWidget and Ui_Form
        """
        super().__init__()  # run constructor of parent classes
        self.setupUi(self)  # run setupUi() (see Ui_Form)
        self.setWindowTitle('Rankine Cycle Calculator') # set the window title

        self.rankine = rankine()  # instantiate a rankine object
        self.label = [self.le_PHigh, self.le_PLow, self.le_TurbineInletCondition, self.le_TurbineEff, self.le_H1,
                        self.le_H2, self.le_H3, self.le_H4, self.le_HeatAdded, self.le_PumpWork, self.le_Efficiency,
                        self.le_TurbineWork]

        self.assign_widgets()  # connects signals and slots
        self.show()

    def assign_widgets(self):
        # connect clicked signal of pushButton_Calculate to self.Calculate
        self.btn_Calculate.clicked.connect(self.Calculate)

    def Calculate(self):
        """
        Here, we need to scan through the input values to run through the rankine cycle. Finally, output the results to the line edit widgets.
        :return:
        """
        self.rankine.p_high = float(self.le_PHigh.text())*100
        self.rankine.p_low = float(self.le_PLow.text())*100
        self.rankine.eff_turbine = float(self.le_TurbineEff.text())
        self.rankine.quality = float(self.le_TurbineInletCondition.text()) if self.rdo_Quality.isChecked() else None
        self.rankine.t_high = float(self.le_TurbineInletCondition.text()) if self.rdo_THigh.isChecked() else None
        self.rankine.calc_efficiency()

        self.le_H1.setText(str(round(self.rankine.state1.h, 2)))
        self.le_H2.setText(str(round(self.rankine.state2.h, 2)))
        self.le_H3.setText(str(round(self.rankine.state3.h, 2)))
        self.le_H4.setText(str(round(self.rankine.state4.h, 2)))
        self.le_HeatAdded.setText(str(round(self.rankine.heat_added, 2)))
        self.le_PumpWork.setText(str(round(self.rankine.pump_work, 2)))
        self.le_Efficiency.setText(str(round(self.rankine.efficiency, 2)))
        self.le_TurbineWork.setText(str(round(self.rankine.turbine_work, 2)))


        return

    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())