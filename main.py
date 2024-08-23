import flet as ft
import GeometryCalculation

def main(page: ft.Page):
    page.title = "Heat Exchanger manufacturing cost"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def button_clicked_test(e):
        Data_entry.value = f"The value of data table is: '{ds.value}', '{ls.value}', '{ts.value}', '{dte.value}', '{lay.value}', '{ltp.value}', '{Nb.value}',  '{BC.value}', '{NumberPasses.value}', '{Ntp.value}'."
        page.update()

#Navigation Bar section
    page.navigation_bar = ft.NavigationBar( 
            destinations=[
                ft.NavigationBarDestination(label="Data Entry"),
                ft.NavigationBarDestination(label="Fluid Parameters"),
                ft.NavigationBarDestination(label="Raw Material")
                ]
            )
#-------------------------------------#

    Data_entry = ft.Text()
    ds = ft.TextField(label="Shell inside diameter")
    ls = ft.TextField(label="Shell length")
    ts = ft.TextField(label="Thickness of shell")
    dte = ft.TextField(label="Outside diameter of tubes")
    lay = ft.TextField(label="Pitch type")
    ltp = ft.TextField(label="Tube pitch ratio")
    Nb = ft.TextField(label="Number of baffles")
    BC = ft.TextField(label="Baffle cut")
    NumberPasses = ft.TextField(label="Number of passes")
    Ntp = ft.TextField(label="Number of tubes per pass")
   
    testButton = ft.ElevatedButton("test", on_click=button_clicked_test)
    #GeometricCalculation.calculate_shell_thickness(
    page.add(ds, ls, ts, dte, lay, ltp, Nb, BC, NumberPasses, Ntp, testButton, Data_entry)
    


ft.app(main)

