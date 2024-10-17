from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.gridlayout import MDGridLayout


def linear_search(arr, key):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == key:
            return i, steps  # Indeks topilgan
    return -1, steps  # Indeks topilmagan

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    steps = 0
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid, steps  # Indeks topilgan
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps  # Indeks topilmagan
def block_search(arr, key, block_size):
    n = len(arr)
    steps = 0
    for i in range(0, n, block_size):
        steps += 1
        if arr[min(i + block_size, n) - 1] >= key:
            for j in range(i, min(i + block_size, n)):
                steps += 1
                if arr[j] == key:
                    return j, steps  # Indeks topilgan
    return -1, steps  # Indeks topilmagan

# KivyMD Layout klassi
class SearchComparisonApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"

        # Asosiy layout
        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)

        # Massiv uchun input
        self.array_input = MDTextField(
            hint_text='Enter array (space-separated)',
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5},
            mode="rectangle"
        )
        self.layout.add_widget(self.array_input)

        # Kalit uchun input 
        self.keys_input = MDTextField(
            hint_text='Enter keys (space-separated)',
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5},
            mode="rectangle"
        )
        self.layout.add_widget(self.keys_input)

        # Block_size uchun input
        self.block_size_input = MDTextField(
            hint_text='Enter block size',
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5},
            mode="rectangle"
        )
        self.layout.add_widget(self.block_size_input)

        # Qidiruv tugmasi
        self.search_button = MDRaisedButton(
            text='Perform Search',
            pos_hint={"center_x": 0.5},
            size_hint=(0.5, None),
            height=50
        )
        self.search_button.bind(on_press=self.perform_search)
        self.layout.add_widget(self.search_button)

        # Natijalarni ko'rish uchun ScrollView 
        self.result_scroll = MDScrollView()
        self.result_layout = MDGridLayout(cols=1, adaptive_height=True, padding=10)
        self.result_scroll.add_widget(self.result_layout)
        self.layout.add_widget(self.result_scroll)

        return self.layout

    def perform_search(self, instance):
        try:
            arr = list(map(int, self.array_input.text.split()))
            keys = list(map(int, self.keys_input.text.split()))
            block_size = int(self.block_size_input.text)

            results = []
            for key in keys:
                index1, steps_linear = linear_search(arr, key)
                index2, steps_binary = binary_search(arr, key)
                index3, steps_block = block_search(arr, key, block_size)
                results.append((key, index1, steps_linear, index2, steps_binary, index3, steps_block))

            # Avvalgi natijalarni tozalash
            self.result_layout.clear_widgets()

            # Kardlar orqali natijalarni chop etish
            for i, (key, index1, steps_linear, index2, steps_binary, index3, steps_block) in enumerate(results, start=1):
                result_text = f"Key: {key}\n" \
                              f"Linear Search: {steps_linear} steps\n" \
                              f"Binary Search: {steps_binary} steps\n" \
                              f"Block Search: {steps_block} steps"
                card = MDCard(
                    size_hint=(0.9, None),
                    height=150,
                    pos_hint={"center_x": 0.5},
                    padding=10
                )
                card.add_widget(MDLabel(text=result_text, theme_text_color="Primary"))
                self.result_layout.add_widget(card)

        except ValueError:
            self.result_layout.clear_widgets()
            error_card = MDCard(
                size_hint=(0.9, None),
                height=100,
                pos_hint={"center_x": 0.5},
                padding=10
            )
            error_card.add_widget(MDLabel(text="Invalid input! Please enter valid numbers.", theme_text_color="Error"))
            self.result_layout.add_widget(error_card)

# Ishga tushirish
if __name__ == '__main__':
    SearchComparisonApp().run()
