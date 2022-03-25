import sys
from PyQt5.QtWidgets import QWidget, QApplication
from Rankine_GUI import Ui_Form  # from the GUI file your created
from Steam import steam
from Calc_state import Steam_SI as steam

class main_window(QWidget, Ui_Form):
    def __init__(self):
        """
        Constructor for the main window of the application.  This class inherits from QWidget and Ui_Form
        """
        super().__init__()  # run constructor of parent classes
        self.setupUi(self)  # run setupUi() (see Ui_Form)
        self.setWindowTitle('Rankine Cycle Calculator') # set the window title

        self.Steam = steam()  # instantiate a steam object
        # create a list of the check boxes on the main window
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
        Here, we need to scan through the check boxes and ensure that only two are selected a defining properties
        for calculating the state of the steam.  Then set the properties of the steam object and calculate the
        steam state.  Finally, output the results to the line edit widgets.
        :return:
        """
        filled=0
        for f in self.label:
            filled+=1 if f.setEnabled(False) else 0
        if filled != 2:
            return

        self.rankine.p_high = float(self.le_PHigh.text()) if self.le_PHigh.isEnabled() else None
        self.rankine.p_low = float(self.le_PLow.text()) if self.le_PLow.isEnabled() else None
        self.rankine.efficiency = float(self.le_TurbineInletConditiontext()) if self.le_TurbineInletCondition() else None
        self.rankine.state1 = float(self.le_H1.text()) if self.le_H1.isEnabled() else None
        self.rankine.state2 = float(self.le_H2.text()) if self.le_H2.isEnabled() else None
        self.rankine.state3 = float(self.le_H3.text()) if self.le_H3.isEnabled() else None
        self.rankine.state4 = float(self.le_H4.text()) if self.le_H4.isEnabled() else None
        self.rankine.turbine_work = float(self.le_TurbineWork.text()) if self.le_TurbineWork.isEnabled() else None
        self.rankine.pump_work = float(self.le_PumpWork.text()) if self.le_TurbineWork.isEnabled() else None
        self.rankine.heat_added = float(self.le_HeatAdded.text()) if self.le_HeatAdded.isEnabled() else None
        self.rankine.efficiency = float(self.le_Efficiency.text()) if self.le_Efficiency.isEnabled() else None
        self.Steam.calc()
        self.show()

        self.le_PHigh.setText(str(round(self.rankine.p_high, 2)))
        self.le_PLow.setText(str(round(self.rankine.p_low, 2)))
        self.le_TurbineInletCondition.setText(str(round(self.rankine.efficiency, 2)))
        self.le_H1.setText(str(round(self.rankine.state1, 2)))
        self.le_H2.setText(str(round(self.rankine.state2, 2)))
        self.le_H3.setText(str(round(self.rankine.state3, 2)))
        self.le_H4.setText(str(round(self.rankine.state4, 2)))
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