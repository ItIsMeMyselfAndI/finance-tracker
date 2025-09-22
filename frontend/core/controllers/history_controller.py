# external/built-in modules/libs
from customtkinter import IntVar

# our modules/libs

from backend import TransactionManager  # db manager

from frontend.styles import HistoryStyles  # paddings, dimensions, colors, etc
from frontend.core.models import HistoryPageModel
from frontend.core.views import HistoryPageView
from frontend.core.controllers import Controller


# --------------------------------------------------------------------------------------------------------


class HistoryPageController(Controller[HistoryPageModel, HistoryPageView]):
    def __init__(
        self, transaction_manager: TransactionManager, user_id_var: IntVar, master
    ):
        self.model = HistoryPageModel(
            transaction_manager=transaction_manager, user_id_var=user_id_var
        )
        self.view = HistoryPageView(
            model=self.model, master=master, fg_color=HistoryStyles.MAIN_FRAME_FG_COLOR
        )

    @property
    def model(self) -> HistoryPageModel:
        return self.__model

    @model.setter
    def model(self, value: HistoryPageModel):
        self.__model = value

    @property
    def view(self) -> HistoryPageView:
        return self.__view

    @view.setter
    def view(self, value: HistoryPageView):
        self.__view = value

    def run(self):
        pass

    def update_display(self):
        print("[DEBUG] updating history page display...")
        # destroy prev ver of the table
        for page in self.view.table.body.winfo_children():
            page.destroy()

        self.view.table.body.transactions_per_filter = (
            self.model.load_transactions_per_filter()
        )
        self.view.table.body.filterTransactions()
        self.view.table.body.countFilteredTablePages()
        self.view.table.body.separateFilteredTransactionsPerPage()
        self.view.table.body.updateCurrentTablePage()
        self.view.table.nav._updatePageNumberDisplay()
        self.view.update_idletasks()
        print("[DEBUG] history page display updated successfully")
