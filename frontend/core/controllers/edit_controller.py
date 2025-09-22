# external/built-in modules/libs
from customtkinter import IntVar

# our modules/libs
from backend import TransactionManager

from frontend.styles import EditStyles  # paddings, dimensions, colors, etc
from frontend.core.models import EditPageModel
from frontend.core.views import EditPageView
from frontend.core.controllers import Controller


# --------------------------------------------------------------------------------------------------------


class EditPageController(Controller[EditPageModel, EditPageView]):
    def __init__(
        self, transaction_manager: TransactionManager, user_id_var: IntVar, master
    ):
        self.model = EditPageModel(
            transaction_manager=transaction_manager, user_id_var=user_id_var
        )
        self.view = EditPageView(
            model=self.model, master=master, fg_color=EditStyles.MAIN_FRAME_FG_COLOR
        )

    @property
    def model(self) -> EditPageModel:
        return self.__model

    @model.setter
    def model(self, value: EditPageModel):
        self.__model = value

    @property
    def view(self) -> EditPageView:
        return self.__view

    @view.setter
    def view(self, value: EditPageView):
        self.__view = value

    def run(self):
        pass

    def update_display(self):
        print("[DEBUG] updating edit page display...")
        for form in self.view.form_per_transaction_type.values():
            form.update_transaction_menu_options_per_type()
            form.transactionMenu.configure(values=form.transaction_options)
            form.transactionMenu.set(form.transaction_options[0])
        self.view.update_idletasks()
        print("[DEBUG] edit page display updated successfully")
