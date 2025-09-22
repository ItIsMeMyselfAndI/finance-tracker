from customtkinter import IntVar

# our modules/libs
from backend import TransactionManager  # db manager

from frontend.styles import HomeStyles  # paddings, dimensions, colors, etc
from frontend.core.models import HomePageModel
from frontend.core.views import HomePageView
from frontend.core.controllers import Controller

# --------------------------------------------------------------------------------------------------------


class HomePageController(Controller[HomePageModel, HomePageView]):
    def __init__(
        self, transaction_manager: TransactionManager, user_id_var: IntVar, master
    ):
        self.model = HomePageModel(
            transaction_manager=transaction_manager, user_id_var=user_id_var
        )
        self.view = HomePageView(
            model=self.model, master=master, fg_color=HomeStyles.SCROLL_FRAME_FG_COLOR
        )

    @property
    def model(self) -> HomePageModel:
        return self.__model

    @model.setter
    def model(self, value: HomePageModel):
        self.__model = value

    @property
    def view(self) -> HomePageView:
        return self.__view

    @view.setter
    def view(self, value: HomePageView):
        self.__view = value

    def run(self):
        pass

    def update_display(self):
        print("\n[DEBUG] updating home page display...")
        # update total balance in header
        self.model.load_amounts()
        self.view.header.amount_label.configure(text=f"₱ {self.model.balance:,}")

        self._update_table()
        self._update_monthly_report()
        self._update_quarterly_report()
        print("[DEBUG] home page display updated successfully")

    def _update_table(self):
        print("[DEBUG] updating recent transaction table...")
        # destroy prev ver of the table
        for page in self.view.recent_table.body.winfo_children():
            page.destroy()

        self.view.recent_table.body.transactions_per_filter = (
            self.model.load_transactions_per_filter()
        )
        self.view.recent_table.body.filterTransactions()
        self.view.recent_table.body.countFilteredTablePages()
        self.view.recent_table.body.separateFilteredTransactionsPerPage()
        self.view.recent_table.body.updateCurrentTablePage()
        self.view.update_idletasks()
        print("[DEBUG] recent transaction table updated successfully")

    def _update_monthly_report(self):
        print("[DEBUG] updating monthly report graphs...")
        self.view.monthly_report.income_canvas.get_tk_widget().destroy()
        self.view.monthly_report.expense_canvas.get_tk_widget().destroy()
        (
            self.view.monthly_report.income_canvas,
            self.view.monthly_report.expense_canvas,
        ) = self.view.monthly_report.display_graphs_section()
        self.view.update_idletasks()
        print("[DEBUG] monthly report graphs updated successfully")

    def _update_quarterly_report(self):
        print("[DEBUG] updating quarterly report graph...")
        self.view.quarterly_report.graph_canvas.get_tk_widget().destroy()
        self.view.quarterly_report.graph_canvas = (
            self.view.quarterly_report.display_graphs_section()
        )
        self.view.update_idletasks()
        print("[DEBUG] quarterly report graph updated successfully")
