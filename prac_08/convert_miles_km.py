from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """MilesConverterApp is an app for user to convert miles to km."""
    def build(self):
        """Build kivy app from kivy file."""
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_miles_km.kv')

    def handle_calculate(self):
        """Handle calculate button, and output result to label widget """
        miles = self.get_validated_miles()
        result = MILES_TO_KM * miles
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle increment button(up/down 1 each press) and output result to label widget """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Make sure miles input and output are valid."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()