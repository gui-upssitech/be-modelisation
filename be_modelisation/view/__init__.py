from .window_manager import WindowManager

def show_results(livrable, parameters, a, b):
    window_manager = WindowManager(livrable, parameters, a, b)
    window_manager.run()