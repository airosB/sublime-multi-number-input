import sublime, sublime_plugin

class MultiNumberInputCommand(sublime_plugin.TextCommand):
    def on_done(self, arg):
        paramsArray = arg.split(" ")
        paramsArray.extend(['', '']) #minimum length is 3
        initial     = int(paramsArray[0]) if paramsArray[0] != '' else 1
        digits      = int(paramsArray[1]) if paramsArray[1] != '' else 1
        interval    = int(paramsArray[2]) if paramsArray[2] != '' else 1
        self.view.run_command('insert_numbers', {'args': [initial, interval, digits]})

    def run(self, edit):
            self.view.window().show_input_panel('Initial Digits Step | ex) 2 5 3: ', '', self.on_done, None, None)


class InsertNumbers(sublime_plugin.TextCommand):
  def run(self, edit, args):
    number = args[0]
    interval = args[1]
    digits = args[2]

    for region in self.view.sel():
        #for negative values
        if number < 0:
            my_digits = digits + 1
        else:
            my_digits = digits

        formatter = '{0:0' + str(my_digits) + 'd}'
        formatted = formatter.format(number)
        self.view.replace(edit, region, str(formatted))
        number = number + interval
