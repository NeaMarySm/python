import model_mult as model
import view


def run():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.count()
    view.button_click(result)
