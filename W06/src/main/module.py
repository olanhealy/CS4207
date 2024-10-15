class Module:
    def __init__(self, modules_code, modules_done=[]):
        self.module_code = modules_code
        self.modules_done=modules_done or []
