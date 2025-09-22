# external/built-in modules/libs
from customtkinter import IntVar

# our modules/libs
from backend import TransactionManager

from frontend.styles import AddStyles  # paddings, dimensions, colors, etc
from frontend.core.models import AddPageModel
from frontend.core.views import AddPageView
from frontend.core.controllers import Controller


# --------------------------------------------------------------------------------------------------------


class AddPageController(Controller[AddPageModel, AddPageView]):
    def __init__(
        self, transaction_manager: TransactionManager, user_id_var: IntVar, master
    ):
        self.model = AddPageModel(
            transaction_manager=transaction_manager, user_id_var=user_id_var
        )
        self.view = AddPageView(
            model=self.model, master=master, fg_color=AddStyles.MAIN_FRAME_FG_COLOR
        )

    @property
    def model(self) -> AddPageModel:
        return self.__model

    @model.setter
    def model(self, value: AddPageModel):
        self.__model = value

    @property
    def view(self) -> AddPageView:
        return self.__view

    @view.setter
    def view(self, value: AddPageView):
        self.__view = value

    def run(self):
        pass

    def update_display(self):
        # print("[DEBUG] updating edit page display...")
        # print("[DEBUG] edit page display updated successfully")
        pass
