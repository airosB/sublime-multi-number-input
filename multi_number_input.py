import sublime_plugin

class MultiNumberInputCommand(sublime_plugin.TextCommand):
    def on_done(self, args):
        args_array = args.split(" by ")
        num = args_array[0]
        by = int(args_array[1]) if 1 < len(args_array) else 1
        edit = self.view.begin_edit()
        for region in self.view.sel():
            self.view.replace(edit, region, str(num))
            num = int(num) + by
        self.view.end_edit(edit)
    def run(self, edit):
        # Show input panel for surround word, then handling input
        self.view.window().show_input_panel('Initial number ex) 1 by 3: ', '1', self.on_done, None, None)
